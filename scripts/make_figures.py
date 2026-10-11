"""Generate original editable SVG teaching figures; schematic curves labeled."""
from pathlib import Path
import textwrap
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
plt.rcParams.update({"font.family":"DejaVu Serif","font.size":11,
                     "svg.fonttype":"none","axes.spines.top":False,"axes.spines.right":False})
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"figures";OUT.mkdir(exist_ok=True)
navy="#16324f";teal="#257c80";gray="#52616b";orange="#b77931"
def save(fig,name):
    fig.savefig(OUT/(name+".svg"),bbox_inches="tight",facecolor="white")
    fig.savefig(OUT/(name+".png"),dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)
def canvas(title,subtitle="Original schematic — no calculated research results",size=(10,6)):
    fig,ax=plt.subplots(figsize=size);ax.set(xlim=(0,10),ylim=(0,6));ax.axis("off")
    ax.text(.1,5.65,title,fontsize=17,color=navy,weight="bold")
    ax.text(.1,5.25,subtitle,fontsize=9,color=gray)
    return fig,ax
def box(ax,x,y,w,h,text,color=navy):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.035,rounding_size=0.08",
                              facecolor="white",edgecolor=color,linewidth=1.3))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=10,color=color)
def arrow(ax,a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=12,color=gray,linewidth=1.1))
fig,ax=canvas("Molecular simulation: method taxonomy")
box(ax,3.5,4.3,3,.6,"Scientific question")
for x,label in [(0.1,"Equilibrium distributions"),(3.5,"Physical or model dynamics"),(6.9,"Free-energy exploration")]:
    box(ax,x,3.05,3,.7,label);arrow(ax,(5,4.3),(x+1.5,3.75))
box(ax,.1,1.3,3,1.1,"MC · GCMC\nPIMD equilibrium");arrow(ax,(1.6,3.05),(1.6,2.4))
box(ax,3.5,1.3,3,1.1,"Classical · BOMD · CPMD\nReactive · CG · MLIP · KMC");arrow(ax,(5,3.05),(5,2.4))
box(ax,6.9,1.3,3,1.1,"Umbrella · Metadynamics\nReplica exchange");arrow(ax,(8.4,3.05),(8.4,2.4))
ax.text(.15,.45,"Categories overlap: a learned potential can supply forces to classical MD or PIMD.",fontsize=10,color=gray)
save(fig,"01_method_taxonomy")
fig,ax=canvas("MD and equilibrium MC answer different questions")
for x,title,lines in [(.3,"Molecular dynamics",["Force law + integrator","Time-ordered trajectory","Structure + justified dynamics"]),(5.3,"Equilibrium Monte Carlo",["Target measure + proposals","Correlated configuration chain","Equilibrium averages; no physical clock"])]:
    box(ax,x,4.15,4.3,.6,title)
    for i,line in enumerate(lines):
        y=2.95-i*1.05;box(ax,x,y,4.3,.65,line)
        arrow(ax,(x+2.15,y+1.15),(x+2.15,y+.65))
save(fig,"02_md_vs_mc")
fig,ax=canvas("Statistical ensembles and reservoir exchange")
for i,(name,fixed,exchange) in enumerate([
("NVE","N, V, E","Isolated: no exchange"),("NVT","N, V, T","Heat"),
("NPT","N, p, T","Heat + volume work"),("Grand canonical","μ, V, T","Heat + particles")]):
    x=.3+(i%2)*5;y=2.8-(i//2)*2.1
    box(ax,x,y,4.3,1.7,f"{name}\nControlled: {fixed}\nExchange: {exchange}",teal if i%2 else navy)
save(fig,"03_ensembles")
fig,ax=canvas("Force-field components: terms and assumptions")
for i,(name,note) in enumerate([("Bond stretching","Near-equilibrium bond length"),("Angle bending","Local angular preference"),("Torsion","Conformational preference"),("Nonbonded dispersion","LJ or another fitted form"),("Electrostatics","Charges; long-range treatment"),("Additional response","Polarization / reactive / many-body")]):
    x=.3+(i%2)*5;y=3.8-(i//2)*1.35
    box(ax,x,y,4.3,1.,name+"\n"+note)
ax.text(.3,.3,"Fixed topology does not generally permit bond breaking or bond formation.",color=gray,fontsize=10)
save(fig,"04_force_field_components")
fig,ax=canvas("A simulation workflow built around evidence")
labels=[("Question","Observable and precision"),("Model","Domain and parameters"),("Numerics","Integrator and convergence"),
        ("Preparation","Slow-variable equilibration"),("Production","Independent information"),("Interpretation","Uncertainty and limitations")]
coords=[(.25,3.6),(3.55,3.6),(6.85,3.6),(6.85,1.6),(3.55,1.6),(.25,1.6)]
for (x,y),(a,b) in zip(coords,labels):box(ax,x,y,2.85,1,a+"\n"+b)
for i in range(5):
    x,y=coords[i];u,v=coords[i+1]
    arrow(ax,(x+2.85,y+.5) if u>x else ((x+1.425,y) if v<y else (x,y+.5)),
          (u,v+.5) if u>x else ((u+1.425,v+1) if v<y else (u+2.85,v+.5)))
ax.text(.25,.5,"Unexpected result → revisit model, numerics and sampling separately.",color=gray)
save(fig,"05_md_workflow")
r=np.linspace(.98,3,500);u=4*(r**-12-r**-6);f=24*(2*r**-13-r**-7)
fig,axs=plt.subplots(1,2,figsize=(10,4))
axs[0].plot(r,u,color=navy);axs[0].axhline(0,color=gray,lw=.7);axs[0].set(xlabel="r / σ",ylabel="u / ε",ylim=(-1.3,2.5),title="Analytical LJ energy")
axs[1].plot(r,f,color=teal);axs[1].axhline(0,color=gray,lw=.7);axs[1].set(xlabel="r / σ",ylabel="Radial force × σ / ε",ylim=(-4,8),title="Force = −du/dr")
fig.suptitle("Analytical untruncated pair model; not simulation data");fig.tight_layout()
save(fig,"06_potential_and_force")
t=np.logspace(-2,3,400);m=t*t/(1+t)
fig,ax=plt.subplots(figsize=(8,4.6))
ax.loglog(t,m,color=navy,label="Illustrative crossover curve")
ax.loglog(t[:85],t[:85]**2*10,"--",color=gray,label="Guide slope 2")
ax.loglog(t[-100:],t[-100:]*.5,"--",color=teal,label="Guide slope 1")
ax.set(xlabel="Lag time (arbitrary units)",ylabel="MSD (arbitrary units)",title="MSD interpretation — schematic, no measured D")
ax.legend();fig.tight_layout();save(fig,"07_msd_interpretation")
r=np.linspace(.1,4,400);g=(1-np.exp(-(r/.9)**15))*(1+2*np.exp(-((r-1.12)/.15)**2)+.6*np.exp(-((r-2)/.25)**2))
fig,ax=plt.subplots(figsize=(8,4.6));ax.plot(r,g,color=navy);ax.axhline(1,color=gray,ls="--")
ax.set(xlabel="Separation (arbitrary units)",ylabel="g(r)",title="RDF interpretation — schematic, not a simulated liquid")
ax.annotate("Excluded region",xy=(.5,.1),xytext=(.4,1.2),arrowprops={"arrowstyle":"->","color":gray})
ax.annotate("Enhanced first-shell probability",xy=(1.12,2.7),xytext=(1.7,2.8),arrowprops={"arrowstyle":"->","color":gray})
fig.tight_layout();save(fig,"08_rdf_interpretation")
fig,ax=canvas("GCMC: equilibrium with a particle reservoir")
box(ax,.3,3.5,3.1,1,"Reservoir μ or fugacity\nTemperature T")
box(ax,5.4,3.5,4.1,1,"Host + fluctuating guests\nFixed simulation volume")
arrow(ax,(3.4,4),(5.4,4))
box(ax,.3,1.55,4.1,1,"Propose insert / delete / move\nInclude reverse-proposal factors")
box(ax,5.4,1.55,4.1,1,"Accept or retain old state\nRecord every sampling step")
arrow(ax,(7.45,3.5),(2.35,2.55));arrow(ax,(4.4,2.05),(5.4,2.05))
ax.text(.3,.6,"Average loading + uncertainty → isotherm. MC steps do not give diffusion kinetics.",fontsize=10,color=gray)
save(fig,"09_gcmc_workflow")
fig,ax=canvas("Born–Oppenheimer versus Car–Parrinello MD")
for x,title,body in [(.3,"BOMD","Solve electronic ground state\nEvaluate forces\nAdvance nuclei\nControl SCF force error"),
                      (5.3,"CPMD","Propagate auxiliary orbitals + nuclei\nMaintain orthonormality\nControl fictitious inertia\nCheck adiabatic separation")]:
    box(ax,x,3.9,4.3,.7,title);box(ax,x,1.5,4.3,2,body)
ax.text(.3,.5,"CPMD auxiliary orbital motion is not physical real-time electron dynamics.",fontsize=10,color=gray)
save(fig,"10_bomd_vs_cpmd")
x=np.linspace(-1.7,1.7,400);u=4*(x*x-1)**2
fig,axs=plt.subplots(1,2,figsize=(10,4.3));axs[0].plot(x,u,color=navy)
axs[0].set(xlabel="x (reduced)",ylabel="U / kBT",ylim=(0,10),title="Analytical double-well model")
for c in [-1.,-.5,0,.5,1.]:axs[1].plot(x,np.exp(-(u+6*(x-c)**2)),lw=1.1)
axs[1].set(xlabel="x (reduced)",ylabel="Unnormalized biased weight",title="Analytical umbrella weights")
fig.suptitle("Known toy landscape — these curves are analytical, not sampled output")
fig.tight_layout();save(fig,"11_free_energy_landscape")
fig,ax=canvas("Accessible scales depend on the computational model")
rows=[("Classical / coarse-grained","Many inexpensive force steps; model-dependent time mapping"),
("Electronic-structure MD","Electronic solve per step; small timestep and matrix/grid costs"),
("MLIP-MD","Inference per step; reference data and domain validation separate"),
("PIMD / enhanced sampling","Multiple beads, windows or replicas multiply base work"),
("MC / GCMC / KMC","Equilibrium MC has no physical clock; KMC uses specified rates")]
for i,(a,b) in enumerate(rows):
    y=4.15-i*.85;ax.text(.3,y,a,weight="bold",color=navy,fontsize=10)
    ax.text(.3,y-.31,b,color=gray,fontsize=9)
ax.text(.3,.1,"No universal atom-count, timescale or speedup ranking; benchmark the actual workload.",fontsize=9,color=teal)
save(fig,"12_scales_and_costs")
print("Generated 12 original SVG/PNG figures.")
