"""Make diagnostic plots; never silently selects a diffusion fit window."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scripts.numerics import rdf,msd,vacf
def main():
    p=argparse.ArgumentParser();p.add_argument("trajectory",type=Path)
    a=p.parse_args();data=np.load(a.trajectory);out=a.trajectory.parent
    x=data["positions"];box=float(data["box"]);dt=float(data["dt_saved"]);th=data["thermo"]
    r,g=rdf(x,box,np.linspace(0,box/2,65))
    maxlag=max(1,len(x)//3); lag=np.arange(maxlag+1)*dt
    m=msd(x,maxlag); c=vacf(data["velocities"],maxlag)
    fig,axs=plt.subplots(2,3,figsize=(12,7))
    axs[0,0].plot(th[:,0],th[:,3]);axs[0,0].set(xlabel="t*",ylabel="E*/N",title="NVE energy")
    axs[0,1].plot(th[:,0],th[:,4]);axs[0,1].set(xlabel="t*",ylabel="T*",title="Temperature")
    axs[0,2].plot(r,g);axs[0,2].set(xlabel="r/σ",ylabel="g(r)",title="Finite-N RDF")
    axs[1,0].plot(lag,m);axs[1,0].set(xlabel="lag t*",ylabel="MSD/σ²",title="No automatic diffusion fit")
    axs[1,1].loglog(lag[1:],m[1:]);axs[1,1].set(xlabel="lag t*",ylabel="MSD/σ²",title="Regime diagnosis")
    axs[1,2].plot(lag,c);axs[1,2].set(xlabel="lag t*",ylabel="VACF",title="Thermostat-free production")
    fig.suptitle("Executed toy simulation — convergence must be assessed")
    fig.tight_layout();fig.savefig(out/"diagnostics.svg");fig.savefig(out/"diagnostics.png",dpi=160);plt.close(fig)
    np.savetxt(out/"rdf.csv",np.c_[r,g],delimiter=",",header="r_reduced,g",comments="")
    np.savetxt(out/"dynamics.csv",np.c_[lag,m,c],delimiter=",",header="lag,MSD,VACF",comments="")
    print(out/"diagnostics.svg")
if __name__=="__main__":main()
