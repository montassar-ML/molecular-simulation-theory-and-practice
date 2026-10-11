# Method–application–resource matrix

Established from the [source review](SOURCE_REVIEW.md) before implementation. Resource categories are planning guidance, not capability ceilings or benchmark claims.

| Method | Question and application | Reference anchor | Resource starting point | Interpretation boundary |
|---|---|---|---|---|
| Classical MD | LJ structure/diffusion; FCC vibrations | [Verlet](references.md#verlet1967), [Rahman](references.md#rahman1964) | Laptop toy systems; CPU/GPU for larger fluids | Dynamics belong to potential and coupling |
| BOMD | DFT water forces and rearrangements | [CP2K](references.md#kuhne2020) | Multicore workstation/cluster | Functional, basis, SCF and sampling errors |
| CPMD | Auxiliary orbital and nuclear propagation | [Car–Parrinello](references.md#car1985) | Suitable CPU/GPU engine | Fictitious electrons are not real-time electrons |
| Reactive MD | Bond rearrangement | [ReaxFF](references.md#van_duin2001) | Workstation/cluster | Element coverage does not validate barriers |
| Coarse-grained MD | Polymer relaxation | [Kremer–Grest](references.md#kremer1990) | Laptop to GPU | Lost detail; no universal time rescaling |
| Equilibrium MC | Liquid configurational equilibrium | [Metropolis](references.md#metropolis1953), [Hastings](references.md#hastings1970) | Laptop or CPU replicas | Sweeps are not physical time |
| GCMC | Methane in public MFI; MOF/COF adsorption | [RASPA3](references.md#ran2024), [Han](references.md#han2008) | Laptop pilot; CPU isotherm jobs | Equilibrium uptake is not transport |
| KMC | Surface reaction kinetics | [Reuter](references.md#reuter2004) | Small catalogue on laptop; expensive rate calculations | Time depends on rates and event completeness |
| Enhanced sampling | Double-well free energy | [Umbrella](references.md#torrie1977), [WHAM](references.md#kumar1992) | Laptop toy; parallel molecular windows | Bias removal and hidden barriers |
| PIMD | Equilibrium nuclear quantum effects | [Review](references.md#markland2018) | Multiple force replicas | Beads are imaginary-time objects |
| MLIP-MD | Learned-force solid-state dynamics | [CHGNet](references.md#chen2023), [Review](references.md#deringer2019) | GPU often useful; reference DFT separate | Average error does not establish transferability |

For adsorption and transport, combine GCMC equilibrium loadings with independently converged MD at those loadings, or construct a separate validated KMC model. Use the [resource worksheet](COMPUTATIONAL_RESOURCES.md) to replace generic expectations with measurements.
