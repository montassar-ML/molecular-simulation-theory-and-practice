# Computational resources and planning worksheet

[Course home](README.md) · [Performance theory](docs/19_computational_performance.md)

Resource needs come from the Hamiltonian, algorithm, accuracy, sample size and output policy together. The ranges below are **illustrative planning envelopes**, not measured benchmarks, purchase specifications or hard limits. RAM must be measured for the actual software build and input.

| Method | Example system | System size | Simulation timescale | CPU/GPU requirements | RAM | Storage | Expected computational cost | Important limitations |
|---|---|---|---|---|---|---|---|---|
| Toy classical MD | Python LJ liquid | 108 atoms by default | 16 reduced time units in default production | One CPU; no GPU required | Modest; all-pair arrays scale quadratically | Small NPZ/CSV | Directly executable laptop exercise | Not a scalable engine or converged bulk-property run |
| Optimized classical MD | Water/electrolyte | Illustratively $10^3$–$10^6$ atoms | ps–µs targets depending on question | CPU or supported GPU engine; benchmark | Often near-linear with particles and neighbors | Output often dominates | Steps × measured step time × replicas | Electrostatics, constraints and hardware affect throughput |
| Solid-state MD | FCC Cu/EMT | 108 atoms supplied | 1 ps default production | Laptop CPU for exercise; larger work scales | Measure calculator/neighbor peak | Trajectory plus thermo | Short diagnostic before longer runs | EMT domain and fixed volume |
| Reactive MD | Oxidation/decomposition | Illustratively $10^3$–$10^5$ atoms | ps–ns targets | Multicore CPU; supported GPU styles only | Neighbor/bond-order/charge arrays | Frequent event data can be large | More work per step and often shorter step than simple MD | Chemistry/charge convergence dominate validity |
| Coarse-grained MD | Polymer melt | Illustratively $10^3$–$10^6$ beads | Model time; physical mapping required | Laptop to GPU/cluster | Beads/neighbors plus topology | Less detail per frame; long runs add up | Benchmark chosen mapping | Speedup does not imply correct kinetics |
| Equilibrium MC/GCMC | Methane in MFI | Variable guest count; rigid 2×2×2 host | **No physical time** | CPU pilot; parallel pressure points/seeds | Host, guests, grids if used | Loading logs small; density grids optional | Effective samples per wall time | Dense insertion, metastability, host assumptions |
| KMC | Surface reaction lattice | Events/sites, not only atoms | Emergent rate-based time | Laptop small catalogue; expensive DFT rates separate | Catalogue and local event structures | Event logs/checkpoints | Events to reach required physical time | Fast futile events and missing rates |
| BOMD/CPMD | Small water cell | 24 atoms supplied; larger research cells conditional | 0.1 ps supplied diagnostic; often ps targets | Multicore workstation/cluster; build-specific GPU | Basis, matrices, grids; may grow faster than atom count | Orbitals/restarts can outweigh trajectory | Electronic steps × MD steps | SCF/functional errors and short sampling |
| Enhanced sampling | Windows/replicas | Base model × windows | Per-window duration, not unbiased event time | Independent CPU/GPU jobs | Sum concurrent replicas | Sum window outputs | Preparation plus production for every window | Hidden barriers and overlap |
| PIMD | Quantum-nuclear water | Physical atoms × beads | Sampling time, not exact real time | Parallel force clients; cluster for DFT forces | Beads and electronic clients | Bead trajectories multiply output | Roughly bead force work before optimization | Bead convergence and estimator conventions |
| MLIP-MD | Learned solid/fluid forces | Model-dependent | MD duration in deployment domain | CPU possible; GPU often useful | Model activations and neighbor graphs | Reference data, model files, trajectories | Include reference DFT and training budget | Domain shift and shared reference bias |

## Hardware tiers

| Tier | Reasonable starting use | What to measure before expanding |
|---|---|---|
| Laptop/personal desktop | All Python notebooks, LJ/MC/free-energy toys, small ASE/OpenMM pilots | Memory headroom, wall time, thermal throttling, storage |
| Small workstation | Several small replicas; classical model development | Job concurrency versus per-job performance |
| Multicore workstation | Moderate classical systems, small AIMD | MPI/OpenMP balance, memory bandwidth and SCF memory |
| Single GPU workstation | Compatible classical or MLIP production | GPU memory, transfer/CPU bottlenecks, supported interactions |
| University CPU cluster | Independent GCMC points, AIMD, large CPU simulations | Scheduler limits, scaling, node memory, filesystem load |
| University GPU cluster | Supported large classical/MLIP runs and many replicas | Interconnect, GPU mapping, multi-node efficiency |
| Large HPC infrastructure | Very large coupled problems or ensembles | Scientific need for scale, queue cost, fault tolerance and checkpoints |

A larger allocation can be slower if communication or synchronization dominates. Increasing independent replicas may improve scientific information more than doubling ranks on one already saturated trajectory.

## Step and storage arithmetic

For desired duration $t_{\rm sim}$ and timestep $\Delta t$ in the same units,

```math
N_{\rm step}=\left\lceil t_{\rm sim}/\Delta t\right\rceil,\qquad
N_{\rm frame}=\left\lfloor N_{\rm step}/s\right\rfloor+1,
\qquad
S_{\rm raw}=N_{\rm rep}N_{\rm frame}N_{\rm atom}\,d\,b\,n_{\rm array}.
```

$s$ is output stride, $d=3$, $b$ bytes/scalar and $n_{\rm array}$ counts coordinates, velocities and/or forces. This is a raw numerical payload, excluding topology, frame headers, cell matrices, metadata, restart files and compression.

**Illustrative arithmetic only:** 100,000 atoms for 10 ns at 2 fs needs 5,000,000 integration steps. Saving coordinates every 1,000 steps gives 5,001 frames. At 4 bytes/scalar, raw coordinates occupy 6,001,200,000 bytes ≈ 6.00 GB or 5.59 GiB per replica. This says nothing about wall time or compressed format size.

Measure $t_{\rm step}$ after warm-up under actual settings. Project $t_{\rm wall}\approx N_{\rm step}t_{\rm step}+t_{\rm setup}+t_{\rm I/O}$. CPU-core hours are wall hours × allocated CPU cores; GPU-device hours are wall hours × allocated GPUs. Summed replica hours are not elapsed wall time when replicas run concurrently.

## Fill-in worksheet

| Field | Your measured/planned value |
|---|---|
| Question, target observable and required precision | |
| Model, parameter hash, engine/version and units | |
| Atoms/beads/basis size; cell and cutoff | |
| Equilibration and production duration or MC cycles | |
| Timestep; integration/SCF tolerances | |
| Replicas/windows/pressure points | |
| CPU ranks × threads; GPU type/count | |
| Pilot setup time and measured steady step time | |
| Peak resident RAM; GPU memory | |
| Output stride; measured bytes/frame | |
| Checkpoint size/interval and restart test | |
| Projection and explicitly assumed safety margin | |
| Queue limits and recovery plan | |
| Convergence test most likely to change this budget | |

Run from repository root:

```bash
python -m scripts.resource_estimator --atoms 100000 --duration-ps 10000 --dt-fs 2 --stride 1000
```

Add `--seconds-per-step` only after measuring it. [Notebook 6](notebooks/06_resources_and_quantum.ipynb) explores storage and the separate quantum-oscillator teaching example.

For CP2K, benchmark one electronic step and a short trajectory because the number of SCF iterations changes with geometry. For GCMC, measure effective occupancy samples per wall time; proposals per second without mixing information can be misleading.
