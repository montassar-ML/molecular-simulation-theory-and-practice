# 19. Computational performance and HPC

**Level:** intermediate → research. **Outcomes:** measure useful performance and distinguish hardware throughput from scientific efficiency.

## What scales with atom count?

A naive pair calculation costs $O(N^2)$. At fixed density and short cutoff, each particle has approximately $(4\pi/3)\rho r_c^3$ neighbors. Linked cells and reusable neighbor lists can make force work near-linear in $N$, with a prefactor growing roughly with cutoff volume. The Python LJ utility is deliberately all-pairs and should not be used to claim engine scaling.

Mesh electrostatics adds FFT and interpolation work, often described as $O(N\log N)$ under suitable mesh scaling. Communication and decomposition affect actual runtime. Reactive charge equilibration, many-body terms, ML neighbor graphs and electronic structure introduce different costs. Conventional dense DFT steps can have cubic matrix-operation costs; sparse or linear-scaling approaches need favorable localization and implementation conditions.

## MPI, OpenMP and GPUs

MPI distributes memory and work across processes, often with domain decomposition. Ghost atoms, reciprocal-space transforms and collective operations communicate across ranks. OpenMP threads share an address space within a node. Hybrid MPI/OpenMP can reduce replicated data and communication, but thread contention and affinity matter.

GPUs accelerate supported computational kernels, not automatically every command in an input. An unsupported interaction or expensive host/device transfer can dominate. Benchmark the complete workflow, including constraint solving, neighbor construction, output and any bias plugin. Mixed precision can improve speed but requires validation for the intended observable.

Use one thread budget per actual core allocation; nested BLAS and OpenMP threading can oversubscribe. Record affinity, compiler, precision, MPI/library versions and accelerator package. Portable performance claims need those details.

## Strong and weak scaling

Strong scaling keeps the problem fixed while changing workers. Relative to baseline $p_0$,

```math
S(p;p_0)=\frac{t(p_0)}{t(p)},\qquad
E(p;p_0)=\frac{S(p;p_0)}{p/p_0}.
```

Weak scaling grows work proportionally to workers and compares elapsed time at approximately constant work per worker. Ideal weak scaling has constant time, but changing physical size can change algorithmic behavior and sampling requirements.

For serial fraction $f_s$, the simple Amdahl model gives $S(p)\le1/[f_s+(1-f_s)/p]$ relative to one worker, under its assumptions. It is explanatory, not a substitute for a benchmark. More ranks can increase total allocation cost while shortening wall time only slightly.

## Benchmark protocol

1. Choose a representative equilibrated state and actual production settings.
2. Separate initialization, compilation, neighbor warm-up and steady execution.
3. Run a fixed physical workload long enough to time reliably; repeat timings.
4. Keep the model and accuracy constant across hardware comparisons.
5. Record peak host/device memory, output volume and phase timing.
6. Check that energies/forces/statistical observables remain consistent.
7. Report wall time, throughput and allocation cost, plus uncertainty/variation.

For stochastic sampling, report effective independent information per wall time where possible. A move set can have slower proposals and faster convergence. For MD, a larger timestep that changes the property is not a valid speedup.

## Storage and resilience

Choose output intervals based on analysis bandwidth. VACFs need fine velocity sampling; long-time diffusion may permit coarser coordinate saving if unwrapping remains reliable. Event detection may need higher frequency than visualization. Store checkpoint state separately from analysis trajectories and test a restart before a long allocation.

Trajectory payload estimates are in [the worksheet](../COMPUTATIONAL_RESOURCES.md). Measure actual bytes/frame because compression, precision and metadata differ. Avoid tiny synchronous writes from every rank to a shared filesystem. Checkpoints should preserve thermostat/barostat/solver state when needed for a valid continuation.

## Guided exercise

Given timings $t(p)$ measured on your own system, plot wall time, strong-scaling efficiency and core-hour cost. Choose an allocation that satisfies both the scientific deadline and resource budget. Then compare using the extra cores for independent replicas.

**Checkpoint:** the fastest wall-time allocation is not necessarily the most informative or efficient. A claimed speedup must name baseline hardware, model, precision and workload.

**Sources:** [LAMMPS](../references.md#thompson2022), [GROMACS](../references.md#abraham2015), [CP2K](../references.md#kuhne2020), [official acceleration documentation](https://docs.lammps.org/Speed_packages.html), [GROMACS performance guide](https://manual.gromacs.org/current/user-guide/mdrun-performance.html).
