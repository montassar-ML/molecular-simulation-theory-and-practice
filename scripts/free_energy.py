"""Independent umbrella MC windows and binned WHAM for a 1D double well.
x and U are reduced units; kBT=1. This is a synthetic model, not molecular data.
"""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scripts.numerics import wham
def potential(x):return 4*(x*x-1)**2
def run(steps=30000,burn=5000,seed=2026):
    if not 0<=burn<steps:raise ValueError("Invalid burn-in.")
    centers=np.linspace(-1.5,1.5,13); kappa=12.;edges=np.linspace(-2,2,161)
    mids=(edges[:-1]+edges[1:])/2;hist=[];series=[];accept=[]
    for index,center in enumerate(centers):
        rng=np.random.default_rng(np.random.SeedSequence([seed,index]))
        x=float(center);samples=[];count=0
        def e(q):return potential(q)+.5*kappa*(q-center)**2
        for i in range(steps):
            y=x+rng.uniform(-.4,.4)
            if np.log(rng.random())<min(0.,-(e(y)-e(x))):
                x=y;count+=1
            if i>=burn:samples.append(x)
        hist.append(np.histogram(samples,bins=edges)[0]);series.append(samples);accept.append(count/steps)
    hist=np.array(hist);bias=.5*kappa*(mids[None,:]-centers[:,None])**2
    p,f,it=wham(hist,bias)
    fe=np.full(len(p),np.nan);occupied=p>0
    fe[occupied]=-np.log(p[occupied]/np.diff(edges)[occupied]);fe-=np.nanmin(fe)
    exact=potential(mids);exact-=exact.min()
    return dict(x=mids,free_energy=fe,analytical=exact,histograms=hist,
                centers=centers,samples=np.array(series),acceptance=np.array(accept),
                iterations=np.array(it),probability=p)
def main():
    p=argparse.ArgumentParser();p.add_argument("--steps",type=int,default=30000)
    p.add_argument("--burn",type=int,default=5000);p.add_argument("--seed",type=int,default=2026)
    p.add_argument("--out",type=Path,default=Path("outputs/free_energy"));a=p.parse_args()
    a.out.mkdir(parents=True,exist_ok=True);d=run(a.steps,a.burn,a.seed)
    np.savez_compressed(a.out/"windows.npz",**d)
    fig,axs=plt.subplots(1,2,figsize=(10,4))
    axs[0].plot(d["x"],d["analytical"],label="Analytical toy potential")
    axs[0].plot(d["x"],d["free_energy"],label="WHAM estimate")
    axs[0].set(xlabel="x (reduced)",ylabel="F/kBT + constant",ylim=(0,10));axs[0].legend()
    for h in d["histograms"]:axs[1].plot(d["x"],h/h.sum())
    axs[1].set(xlabel="x (reduced)",ylabel="Window bin probability",title="Overlap diagnostic")
    fig.suptitle("Executed 1D teaching model; no molecular rate claim")
    fig.tight_layout();fig.savefig(a.out/"free_energy.svg");fig.savefig(a.out/"free_energy.png",dpi=160)
    meta={"steps_per_window":a.steps,"burn_per_window":a.burn,"seed":a.seed,
          "windows":len(d["centers"]),"wham_iterations":int(d["iterations"]),
          "status":"executed toy MC; WHAM point estimate, no automatic uncertainty"}
    (a.out/"run_manifest.json").write_text(json.dumps(meta,indent=2)+"\n");print(json.dumps(meta))
if __name__=="__main__":main()
