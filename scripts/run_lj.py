"""Run original force-shifted LJ liquid or solid teaching model."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scripts.numerics import run_lj
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--phase",choices=["liquid","solid"],default="liquid")
    p.add_argument("--steps",type=int,default=4000)
    p.add_argument("--equil",type=int,default=1000)
    p.add_argument("--dt",type=float,default=.004)
    p.add_argument("--stride",type=int,default=10)
    p.add_argument("--seed",type=int,default=2026)
    p.add_argument("--ncells",type=int,default=3)
    p.add_argument("--temperature",type=float)
    p.add_argument("--out",type=Path,default=Path("outputs/lj"))
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    density=.75 if a.phase=="liquid" else .95
    temp=a.temperature if a.temperature is not None else (1.2 if a.phase=="liquid" else .15)
    started=time.perf_counter()
    result=run_lj(ncells=a.ncells,density=density,temperature=temp,steps=a.steps,
                  equil=a.equil,dt=a.dt,stride=a.stride,seed=a.seed)
    np.savez_compressed(a.out/"trajectory.npz",**result)
    np.savetxt(a.out/"thermo.csv",result["thermo"],delimiter=",",
               header="time,U_per_particle,K_per_particle,E_per_particle,T,pressure",comments="")
    manifest={**vars(a),"out":str(a.out),"temperature":temp,"density":density,
              "cutoff":2.0,"potential":"force-shifted Lennard-Jones",
              "units":"reduced LJ","status":"executed teaching simulation; not a converged material property",
              "elapsed_seconds":time.perf_counter()-started,"numpy":np.__version__}
    (a.out/"run_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print(json.dumps(manifest,indent=2))
if __name__=="__main__":main()
