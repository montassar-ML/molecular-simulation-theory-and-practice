"""Small, transparent teaching algorithms; not production simulation engines.
LJ: equal masses, reduced units, fixed cubic box, force-shifted cutoff.
RDF: finite-N ideal-gas normalization. See docs/CONVENTIONS.md.
"""
import numpy as np
from scipy.special import logsumexp
from scipy.stats import t as student_t

def minimum_image(delta, box):
    box = np.asarray(box, dtype=float)
    if np.any(box <= 0):
        raise ValueError("Box lengths must be positive.")
    return np.asarray(delta) - box * np.rint(np.asarray(delta) / box)

def lj_pair(r, cutoff=2.0):
    """Return force-shifted LJ pair energy and outward radial force."""
    r = np.asarray(r, dtype=float)
    if np.any(r <= 0) or cutoff <= 0:
        raise ValueError("Positive separations and cutoff required.")
    inv = 1.0 / r
    u = 4 * (inv**12 - inv**6)
    f = 24 * (2 * inv**13 - inv**7)
    uc = 4 * (cutoff**-12 - cutoff**-6)
    fc = 24 * (2 * cutoff**-13 - cutoff**-7)
    inside = r < cutoff
    return np.where(inside, u-uc+(r-cutoff)*fc, 0.0), np.where(inside, f-fc, 0.0)

def lj_forces(positions, box, cutoff=2.0):
    x = np.asarray(positions, dtype=float)
    if x.ndim != 2 or x.shape[1] != 3:
        raise ValueError("positions must have shape (particles,3).")
    if not 0 < cutoff < float(box)/2:
        raise ValueError("Require 0 < cutoff < half the cubic box length.")
    i, j = np.triu_indices(len(x), k=1)
    dr = minimum_image(x[i]-x[j], box)
    r = np.linalg.norm(dr, axis=1)
    if np.any(r < 1e-8):
        raise ValueError("Overlapping particles.")
    mask = r < cutoff
    i, j, dr, r = i[mask], j[mask], dr[mask], r[mask]
    u, f = lj_pair(r, cutoff)
    fij = (f/r)[:, None]*dr
    force = np.zeros_like(x)
    np.add.at(force, i, fij)
    np.add.at(force, j, -fij)
    virial = np.sum(dr*fij)
    return float(u.sum()), force, float(virial)

def fcc(ncells=3, density=0.75):
    if ncells < 1 or density <= 0:
        raise ValueError("Positive cell count and density required.")
    basis = np.array([[0,0,0],[0,.5,.5],[.5,0,.5],[.5,.5,0]])
    a = (4/density)**(1/3)
    cells = np.indices((ncells,)*3).reshape(3,-1).T
    return ((cells[:,None,:]+basis).reshape(-1,3)*a, ncells*a)

def velocity_verlet(x, v, force, box, dt, cutoff):
    v = v + 0.5*dt*force
    x = x + dt*v  # deliberately unwrapped; forces apply minimum images
    u, force, virial = lj_forces(x, box, cutoff)
    v = v + 0.5*dt*force
    return x, v, force, u, virial

def baoab(x, v, force, box, dt, cutoff, temperature, gamma, rng):
    v = v + 0.5*dt*force
    x = x + 0.5*dt*v
    c = np.exp(-gamma*dt)
    noise = rng.normal(size=v.shape)
    noise -= noise.mean(axis=0)  # equal-mass COM-constrained canonical subspace
    v = c*v + np.sqrt((1-c*c)*temperature)*noise
    x = x + 0.5*dt*v
    u, force, virial = lj_forces(x, box, cutoff)
    v = v + 0.5*dt*force
    return x, v, force, u, virial

def run_lj(ncells=3, density=0.75, temperature=1.2, cutoff=2.0,
           dt=.004, equil=1000, steps=4000, stride=10, seed=2026):
    if min(dt,temperature,steps,stride) <= 0 or equil < 0:
        raise ValueError("Invalid simulation length, step or temperature.")
    x, box = fcc(ncells,density)
    rng = np.random.default_rng(seed)
    v = rng.normal(scale=np.sqrt(temperature),size=x.shape)
    v -= v.mean(axis=0)
    u, force, virial = lj_forces(x,box,cutoff)
    preparation = []
    ndof = 3*len(x)-3
    for step in range(equil):
        x,v,force,u,virial = baoab(x,v,force,box,dt,cutoff,temperature,1.0,rng)
        if step % stride == 0:
            preparation.append([step*dt,u/len(x),np.sum(v*v)/ndof])
    coords, velocities, thermo = [], [], []
    for step in range(steps+1):
        if step % stride == 0:
            kin = .5*np.sum(v*v)
            coords.append(x.copy()); velocities.append(v.copy())
            thermo.append([step*dt,u/len(x),kin/len(x),(u+kin)/len(x),
                           2*kin/ndof,(2*kin+virial)/(3*box**3)])
        if step < steps:
            x,v,force,u,virial=velocity_verlet(x,v,force,box,dt,cutoff)
    return dict(positions=np.array(coords),velocities=np.array(velocities),
                thermo=np.array(thermo),preparation=np.array(preparation),
                box=np.array(box),dt_saved=np.array(dt*stride))

def rdf(positions, box, edges, species_a=None, species_b=None):
    """Cubic fixed box. Same-species if species_b is None; otherwise disjoint."""
    x = np.asarray(positions,float)
    if x.ndim==2:x=x[None,...]
    edges=np.asarray(edges,float)
    if x.ndim!=3 or x.shape[-1]!=3 or len(x)==0:
        raise ValueError("Use frames x particles x 3.")
    if len(edges)<2 or edges[0]<0 or np.any(np.diff(edges)<=0) or edges[-1]>box/2:
        raise ValueError("Increasing radial edges within half the box required.")
    n=x.shape[1]
    a=np.arange(n) if species_a is None else np.asarray(species_a,int)
    if len(np.unique(a))!=len(a) or np.any((a<0)|(a>=n)):
        raise ValueError("Invalid or repeated species indices.")
    if species_b is None:
        if len(a)<2:raise ValueError("At least two particles required.")
        ia,ja=np.triu_indices(len(a),1); i,j=a[ia],a[ja]
        pairs=len(a)*(len(a)-1)/2
    else:
        b=np.asarray(species_b,int)
        if len(a)==0 or len(b)==0 or len(np.unique(b))!=len(b) or np.any((b<0)|(b>=n)) or np.intersect1d(a,b).size:
            raise ValueError("Cross species must be valid, nonempty and disjoint.")
        i,j=np.repeat(a,len(b)),np.tile(b,len(a))
        pairs=len(a)*len(b)
    counts=np.zeros(len(edges)-1)
    for frame in x:
        d=np.linalg.norm(minimum_image(frame[i]-frame[j],box),axis=1)
        counts+=np.histogram(d,bins=edges)[0]
    shell=4*np.pi/3*np.diff(edges**3)
    return (edges[1:]+edges[:-1])/2, counts/(len(x)*pairs*shell/box**3)

def msd(positions, max_lag=None, dimensions=(0,1,2)):
    """All-time-origin MSD; input must already be correctly unwrapped."""
    x=np.asarray(positions,float)
    if x.ndim!=3 or x.shape[-1]!=3 or len(x)<2:
        raise ValueError("Need at least two frames with shape (frames,particles,3).")
    dimensions=tuple(dimensions)
    if not dimensions or len(set(dimensions))!=len(dimensions) or not set(dimensions)<=set(range(3)):
        raise ValueError("Unique Cartesian dimensions required.")
    m=len(x)-1 if max_lag is None else int(max_lag)
    if not 1<=m<len(x):raise ValueError("Invalid maximum lag.")
    out=np.zeros(m+1)
    for lag in range(1,m+1):
        dx=(x[lag:]-x[:-lag])[...,list(dimensions)]
        out[lag]=np.mean(np.sum(dx*dx,axis=-1))
    return out

def vacf(velocities, max_lag=None):
    v=np.asarray(velocities,float)
    m=len(v)-1 if max_lag is None else int(max_lag)
    if v.ndim!=3 or not 0<=m<len(v):raise ValueError("Invalid velocity array/lag.")
    return np.array([np.mean(np.sum(v[:len(v)-k]*v[k:],axis=-1))
                     for k in range(m+1)])

def diffusion_slope(time, mean_square, start, stop, dimensions=3):
    """Point estimate only; correlated MSD lag residuals do not supply a valid SE."""
    t=np.asarray(time,float); y=np.asarray(mean_square,float)
    use=(t>=start)&(t<=stop)
    if dimensions not in (1,2,3) or use.sum()<3 or stop<=start:
        raise ValueError("Need >=3 points and valid interval/dimension.")
    slope,intercept=np.polyfit(t[use],y[use],1)
    return float(slope/(2*dimensions)),float(intercept)

def autocorrelation(series):
    x=np.asarray(series,float)
    if x.ndim!=1 or len(x)<4 or not np.all(np.isfinite(x)):
        raise ValueError("Need >=4 finite scalar samples.")
    x=x-x.mean()
    if np.dot(x,x)==0:raise ValueError("Constant series has undefined normalized ACF.")
    n=len(x); fft=np.fft.rfft(x,n=2*n)
    cov=np.fft.irfft(fft*np.conjugate(fft),n=2*n)[:n]/np.arange(n,0,-1)
    return cov/cov[0]

def statistical_inefficiency(series):
    rho=autocorrelation(series)
    nonpos=np.flatnonzero(rho[1:]<=0)
    end=int(nonpos[0]+1) if len(nonpos) else len(rho)
    return max(1.0,float(1+2*rho[1:end].sum()))

def block_summary(series, block_size, confidence=.95):
    x=np.asarray(series,float); b=int(block_size)
    if x.ndim!=1 or not np.all(np.isfinite(x)) or b<1 or not 0<confidence<1:
        raise ValueError("Invalid scalar series, block size or confidence.")
    nblocks=len(x)//b
    if nblocks<4:raise ValueError("At least four blocks required; more is preferable.")
    means=x[:nblocks*b].reshape(nblocks,b).mean(axis=1)
    se=means.std(ddof=1)/np.sqrt(nblocks)
    half=student_t.ppf((1+confidence)/2,nblocks-1)*se
    return dict(mean=float(means.mean()),se=float(se),ci_low=float(means.mean()-half),
                ci_high=float(means.mean()+half),blocks=nblocks,block_size=b,
                discarded_tail=len(x)-nblocks*b,confidence=confidence)

def ideal_gcmc(activity=0.5, volume=10.0, steps=100000, burn=5000, seed=7):
    """Equal insert/delete selection including attempted deletion at N=0."""
    if min(activity,volume,steps)<=0 or not 0<=burn<steps:raise ValueError("Invalid GCMC settings.")
    rng=np.random.default_rng(seed); n=0; out=[]
    logzv=np.log(activity*volume)
    for step in range(steps):
        if rng.random()<.5:
            if np.log(rng.random())<min(0.,logzv-np.log(n+1)):n+=1
        elif n and np.log(rng.random())<min(0.,np.log(n)-logzv):n-=1
        if step>=burn:out.append(n)
    return np.array(out)

def two_state_kmc(a=2.0,b=1.0,tmax=1000.0,seed=1):
    if min(a,b,tmax)<=0:raise ValueError("Positive rates and observation time required.")
    rng=np.random.default_rng(seed); now=0.; state=0; states=[]; durations=[]
    while now<tmax:
        wait=rng.exponential(1/(a if state==0 else b))
        duration=min(wait,tmax-now)
        states.append(state);durations.append(duration)
        now+=duration;state=1-state
    return np.array(states),np.array(durations)

def wham(histograms, bias, beta=1.0, tolerance=1e-10, max_iter=50000):
    """Equal-width binned WHAM, bin probabilities, common beta; no SE estimator."""
    h=np.asarray(histograms,float); w=np.asarray(bias,float)
    if h.ndim!=2 or h.shape!=w.shape or np.any(h<0) or beta<=0:
        raise ValueError("Nonnegative histograms and matching bias array required.")
    n=h.sum(axis=1); total=h.sum(axis=0); visited=total>0
    if np.any(n<=0):raise ValueError("Every window needs observations.")
    # Require a connected graph of shared occupied bins.
    overlap=(h>0).astype(int)@(h>0).astype(int).T
    reached={0}
    while True:
        new=reached|{j for i in reached for j in range(len(n)) if overlap[i,j]>0}
        if new==reached:break
        reached=new
    if len(reached)!=len(n):raise ValueError("Disconnected histogram overlap.")
    f=np.zeros(len(n)); logp=np.full(h.shape[1],-np.inf)
    for iteration in range(max_iter):
        denom=logsumexp(np.log(n)[:,None]+beta*f[:,None]-beta*w,axis=0)
        logp[visited]=np.log(total[visited])-denom[visited]
        logp-=logsumexp(logp)
        newf=-logsumexp(logp[None,:]-beta*w,axis=1)/beta
        newf-=newf[0]
        if np.max(np.abs(newf-f))<tolerance:
            return np.exp(logp),newf,iteration+1
        f=newf
    raise RuntimeError("WHAM did not converge.")
