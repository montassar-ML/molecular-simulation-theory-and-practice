"""Original solvated-water/NaCl teaching run. Optional dependency: OpenMM.
NPT preparation, then fixed-cell NVE production. Short defaults are diagnostics.
"""
import argparse,json,random
from pathlib import Path
import numpy as np
import openmm as mm
from openmm import app,unit
def main():
    p=argparse.ArgumentParser();p.add_argument("--out",type=Path,default=Path("outputs/water"))
    p.add_argument("--equil",type=int,default=1000);p.add_argument("--steps",type=int,default=2000)
    p.add_argument("--stride",type=int,default=10);p.add_argument("--seed",type=int,default=2026)
    p.add_argument("--salt-molar",type=float,default=.15);p.add_argument("--box-nm",type=float,default=3.0)
    p.add_argument("--platform",default="CPU");p.add_argument("--threads",default="2")
    a=p.parse_args()
    if min(a.steps,a.equil,a.stride)<=0 or a.box_nm<=1.8 or a.salt_molar<0:raise ValueError("Invalid settings.")
    a.out.mkdir(parents=True,exist_ok=True);random.seed(a.seed)
    ff=app.ForceField("amber14-all.xml","amber14/tip3p.xml")
    model=app.Modeller(app.Topology(),[])
    model.addSolvent(ff,model="tip3p",boxSize=mm.Vec3(a.box_nm,a.box_nm,a.box_nm)*unit.nanometer,
                     ionicStrength=a.salt_molar*unit.molar,positiveIon="Na+",negativeIon="Cl-")
    system=ff.createSystem(model.topology,nonbondedMethod=app.PME,
                          nonbondedCutoff=.9*unit.nanometer,constraints=app.HBonds,rigidWater=True,
                          ewaldErrorTolerance=1e-5,removeCMMotion=True)
    barostat=mm.MonteCarloBarostat(1*unit.bar,300*unit.kelvin,25);barostat.setRandomNumberSeed(a.seed+1)
    baro_index=system.addForce(barostat)
    langevin=mm.LangevinMiddleIntegrator(300*unit.kelvin,1/unit.picosecond,.002*unit.picosecond)
    langevin.setRandomNumberSeed(a.seed);langevin.setConstraintTolerance(1e-6)
    platform=mm.Platform.getPlatformByName(a.platform)
    props={"Threads":a.threads} if a.platform=="CPU" else {}
    prep=app.Simulation(model.topology,system,langevin,platform,props)
    prep.context.setPositions(model.positions);prep.minimizeEnergy(maxIterations=1000)
    prep.context.setVelocitiesToTemperature(300*unit.kelvin,a.seed)
    prep.reporters.append(app.StateDataReporter(str(a.out/"equilibration.csv"),max(1,a.stride),
                         step=True,potentialEnergy=True,temperature=True,density=True,volume=True))
    prep.step(a.equil)
    state=prep.context.getState(getPositions=True,getVelocities=True)
    box=state.getPeriodicBoxVectors()
    pos=state.getPositions();vel=state.getVelocities()
    del prep,langevin
    system.removeForce(baro_index)
    # Remove periodic COM-velocity removal so production follows a fixed Hamiltonian.
    for index in reversed(range(system.getNumForces())):
        if isinstance(system.getForce(index),mm.CMMotionRemover):system.removeForce(index)
    masses=np.array([system.getParticleMass(i).value_in_unit(unit.dalton) for i in range(system.getNumParticles())])
    velocities=np.array(vel.value_in_unit(unit.nanometer/unit.picosecond))
    velocities-=np.sum(masses[:,None]*velocities,axis=0)/masses.sum()
    system.setDefaultPeriodicBoxVectors(*box)
    integrator=mm.VerletIntegrator(.002*unit.picosecond);integrator.setConstraintTolerance(1e-6)
    sim=app.Simulation(model.topology,system,integrator,platform,props)
    sim.context.setPositions(pos);sim.context.setVelocities(velocities*unit.nanometer/unit.picosecond)
    frames=[];thermo=[]
    ndof=3*len(masses)-system.getNumConstraints()-3
    for step in range(a.steps+1):
        if step%a.stride==0:
            s=sim.context.getState(getPositions=True,getEnergy=True,enforcePeriodicBox=False)
            frames.append(s.getPositions(asNumpy=True).value_in_unit(unit.nanometer))
            u=s.getPotentialEnergy().value_in_unit(unit.kilojoule_per_mole)
            k=s.getKineticEnergy().value_in_unit(unit.kilojoule_per_mole)
            thermo.append([step*.002,u,k,u+k,2*k/(ndof*.00831446261815324)])
        if step<a.steps:sim.step(1)
    boxarr=np.array([[q.value_in_unit(unit.nanometer) for q in vec] for vec in box])
    atoms=[{"index":atom.index,"name":atom.name,"element":atom.element.symbol,
            "residue":atom.residue.name,"resid":atom.residue.index} for atom in model.topology.atoms()]
    waters=[[atom.index for atom in res.atoms()] for res in model.topology.residues() if res.name=="HOH"]
    meta={**vars(a),"out":str(a.out),"openmm_version":mm.__version__,"atoms":atoms,
          "waters":waters,"mass_dalton":masses.tolist(),"units":{"position":"nm","time":"ps","energy":"kJ/mol"},
          "production":"NVE after NPT preparation; no thermostat/barostat",
          "force_field":["amber14-all.xml","amber14/tip3p.xml"],"cutoff_nm":.9,
          "constraints":"HBonds and rigidWater","dt_ps":.002,
          "status":"executed short teaching trajectory, not converged water/electrolyte properties"}
    np.savez_compressed(a.out/"trajectory.npz",positions=np.array(frames),box=boxarr,
                        dt_saved=np.array(.002*a.stride),thermo=np.array(thermo))
    (a.out/"run_manifest.json").write_text(json.dumps(meta,indent=2)+"\n")
    model.topology.setPeriodicBoxVectors(box)
    with (a.out/"initial_production.pdb").open("w") as fh:app.PDBFile.writeFile(model.topology,pos,fh)
    (a.out/"system.xml").write_text(mm.XmlSerializer.serialize(system))
    sim.saveCheckpoint(str(a.out/"checkpoint.chk"))
    np.savetxt(a.out/"thermo.csv",thermo,delimiter=",",header="time_ps,U_kJmol,K_kJmol,E_kJmol,T_K",comments="")
    print(json.dumps({"atoms":len(atoms),"waters":len(waters),"ions":len(atoms)-3*len(waters),
                      "steps":a.steps,"output":str(a.out),"openmm":mm.__version__}))
if __name__=="__main__":main()
