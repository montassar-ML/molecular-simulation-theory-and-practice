"""Optional original FCC copper/EMT exercise; requires ASE, not a production fit."""
import argparse,json
from pathlib import Path
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution,Stationary
from ase.io.trajectory import Trajectory
from ase import units
import ase,numpy as np
def main():
    p=argparse.ArgumentParser();p.add_argument("--out",type=Path,default=Path("outputs/copper"))
    p.add_argument("--steps",type=int,default=1000);p.add_argument("--equil",type=int,default=500)
    p.add_argument("--temperature",type=float,default=300);a=p.parse_args()
    a.out.mkdir(parents=True,exist_ok=True)
    atoms=bulk("Cu","fcc",a=3.6,cubic=True).repeat((3,3,3));atoms.calc=EMT()
    rng=np.random.default_rng(2026)
    MaxwellBoltzmannDistribution(atoms,temperature_K=a.temperature,rng=rng);Stationary(atoms)
    # Unconstrained COM during thermostatting; remove COM once before NVE.
    eq=Langevin(atoms,1*units.fs,temperature_K=a.temperature,friction=.01/units.fs,fixcm=False,rng=rng)
    eq.run(a.equil);Stationary(atoms,preserve_temperature=False)
    dyn=VelocityVerlet(atoms,1*units.fs)
    traj=Trajectory(str(a.out/"copper.traj"),"w",atoms);trace=[]
    def sample():
        traj.write();trace.append([dyn.get_time()/units.fs,atoms.get_potential_energy(),
                                   atoms.get_kinetic_energy(),atoms.get_temperature()])
    dyn.attach(sample,interval=10);dyn.run(a.steps);traj.close()
    np.savetxt(a.out/"thermo.csv",trace,delimiter=",",header="time_fs,U_eV,K_eV,T_ASE_K",comments="")
    meta={"ase":ase.__version__,"atoms":len(atoms),"model":"ASE EMT Cu","lattice_A":3.6,
          "dt_fs":1,"steps":a.steps,"equil":a.equil,"temperature_target_K":a.temperature,
          "status":"short teaching run; fixed lattice is not equilibrium thermal expansion"}
    (a.out/"run_manifest.json").write_text(json.dumps(meta,indent=2)+"\n");print(json.dumps(meta))
if __name__=="__main__":main()
