"""Generate an original ordered 8-water teaching cell and CP2K inputs.
Not an equilibrated liquid. Data/basis files come from the user's CP2K installation.
"""
from pathlib import Path
import numpy as np
box=6.214  # Angstrom; approximately liquid-like number density, only 8 molecules
rng=np.random.default_rng(2026)
template=np.array([[0.,0.,0.],[.9572,0,0],[-.239987,.926627,0.]])
lines=[]
for center in (np.indices((2,2,2)).reshape(3,-1).T+.5)*(box/2):
    q,_=np.linalg.qr(rng.normal(size=(3,3)))
    if np.linalg.det(q)<0:q[:,0]*=-1
    for symbol,xyz in zip(["O","H","H"],template@q+center):
        lines.append(f"{symbol} "+" ".join(f"{v:.8f}" for v in xyz))
Path("water8.xyz").write_text("24\nOriginal ordered teaching start; not equilibrated liquid\n"+"\n".join(lines)+"\n")
print("Wrote water8.xyz; minimize and equilibrate before any liquid interpretation.")
