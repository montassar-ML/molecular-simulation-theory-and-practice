"""Water RDF, molecular COM MSD, coordination, and geometric H bonds.
Requires repository root as working directory. Fixed cubic production cell only.
"""
import argparse,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scripts.numerics import minimum_image,rdf,msd
def main():
    p=argparse.ArgumentParser();p.add_argument("directory",type=Path);a=p.parse_args()
    d=np.load(a.directory/"trajectory.npz");meta=json.loads((a.directory/"run_manifest.json").read_text())
    x=d["positions"];cell=d["box"];box=float(cell[0,0])
    if not np.allclose(cell,np.eye(3)*box):raise ValueError("Only fixed cubic cells supported.")
    atoms=meta["atoms"];O=np.array([at["index"] for at in atoms if at["element"]=="O" and at["residue"]=="HOH"])
    Na=np.array([at["index"] for at in atoms if at["element"]=="Na"],int)
    masses=np.array(meta["mass_dalton"]);com=[]
    for water in meta["waters"]:
        ids=np.array(water);o=next(i for i in ids if atoms[i]["element"]=="O")
        whole=x[:,o:o+1,:]+minimum_image(x[:,ids,:]-x[:,o:o+1,:],box)
        com.append(np.sum(whole*masses[ids][None,:,None],axis=1)/masses[ids].sum())
    com=np.stack(com,axis=1)
    # Infer image crossings between close saved frames. Must verify sampling is frequent enough.
    jumps=minimum_image(np.diff(com,axis=0),box)
    unwrapped=np.concatenate([com[:1],com[:1]+np.cumsum(jumps,axis=0)],axis=0)
    np.savez_compressed(a.directory/"water_com_unwrapped.npz",positions=unwrapped,dt_saved=d["dt_saved"])
    edges=np.linspace(0,box/2,80);r,g=rdf(x,box,edges,O)
    coord=[];hbonds=[]
    for frame in x:
        if len(Na):
            dist=np.linalg.norm(minimum_image(frame[Na,None,:]-frame[O][None,:,:],box),axis=-1)
            coord.append(np.mean(np.sum(dist<.32,axis=1)))
        count=0
        for water in meta["waters"]:
            o=next(i for i in water if atoms[i]["element"]=="O")
            acceptors=O[O!=o]
            oo=minimum_image(frame[acceptors]-frame[o],box)
            acceptors=acceptors[np.linalg.norm(oo,axis=1)<.35]
            for h in [i for i in water if atoms[i]["element"]=="H"]:
                hd=minimum_image(frame[o]-frame[h],box)
                ha=minimum_image(frame[acceptors]-frame[h],box)
                cos=np.sum(ha*hd,axis=1)/(np.linalg.norm(ha,axis=1)*np.linalg.norm(hd))
                count+=np.sum(cos<np.cos(np.deg2rad(150)))
        hbonds.append(count)
    lag=np.arange(max(2,len(x)//3))*float(d["dt_saved"]);m=msd(unwrapped,len(lag)-1)
    fig,ax=plt.subplots(1,3,figsize=(12,3.5))
    ax[0].plot(r,g,label="O–O")
    if len(Na):
        rn,gn=rdf(x,box,edges,Na,O);ax[0].plot(rn,gn,label="Na–O")
    ax[0].set(xlabel="r / nm",ylabel="g(r)");ax[0].legend()
    ax[1].plot(lag,m);ax[1].set(xlabel="lag / ps",ylabel="Water COM MSD / nm²",title="No automatic diffusion fit")
    ax[2].plot(np.arange(len(x))*float(d["dt_saved"]),np.array(hbonds)/len(O))
    ax[2].set(xlabel="t / ps",ylabel="Geometric bonds / water")
    fig.suptitle("Short teaching run; structural and transport convergence unestablished")
    fig.tight_layout();fig.savefig(a.directory/"analysis.svg");fig.savefig(a.directory/"analysis.png",dpi=160)
    summary={"hb_definition":"O-O <0.35 nm, donor-H-acceptor >150 deg",
             "mean_bonds_per_water":float(np.mean(hbonds)/len(O)),
             "Na_O_cutoff_nm":.32,"mean_Na_O_neighbors":float(np.mean(coord)) if coord else None,
             "warning":"Illustrative operational cutoffs; short trajectory, no validated material prediction."}
    (a.directory/"analysis_summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps(summary))
if __name__=="__main__":main()
