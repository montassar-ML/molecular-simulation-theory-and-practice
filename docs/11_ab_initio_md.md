# 11. Born–Oppenheimer ab initio molecular dynamics

**Level:** advanced. **Prerequisites:** MD, basic electronic structure. **Outcomes:** connect electronic minimization to forces; separate electronic, nuclear and sampling errors.

## Definition and historical setting

Born–Oppenheimer MD (BOMD) evaluates an electronic ground-state energy for each nuclear configuration and integrates nuclear motion on that surface. [Car–Parrinello](11b_car_parrinello_md.md) offered a different coupled propagation strategy; the two are not interchangeable labels. The [Quickstep paper](../references.md#vandevondele2005) and [CP2K review](../references.md#kuhne2020) describe efficient Gaussian/plane-wave implementations used for many condensed-phase applications.

The Born–Oppenheimer approximation separates fast electrons and slower nuclei. Ordinary BOMD treats nuclei classically unless combined with a quantum-nuclear method. “Ab initio” does not mean free of exchange-correlation, basis, finite-size or sampling approximations.

## Governing equations

```math
E_{\rm BO}(\mathbf R)=\min_{\Psi}
\langle\Psi|\hat H_e(\mathbf R)|\Psi\rangle+E_{\rm NN}(\mathbf R),
\qquad
M_I\ddot{\mathbf R}_I=-\nabla_I E_{\rm BO}.
```

$\Psi$ is a normalized many-electron state, $\hat H_e$ the electronic Hamiltonian at fixed nuclei and $E_{\rm NN}$ nuclear repulsion. In Kohn–Sham DFT, the minimization is over admissible density/orbitals using an approximate functional. Energies are J (often reported in hartree/eV), forces J m⁻¹, masses kg.

Force evaluation needs consistency with the basis and variational conditions. Atom-centered basis derivatives create Pulay contributions. Incomplete SCF convergence gives noisy or biased forces and can produce energy drift. A stable SCF residual at one geometry does not establish adequate force accuracy across a trajectory.

## Algorithm and model selection

At each step, predict a density/orbitals, solve the electronic problem to tolerance, evaluate energy and forces, integrate nuclei, and update the electronic guess. Wavefunction extrapolation reduces cost but must preserve robust convergence. Inspect difficult frames rather than silently accepting failed electronic iterations.

Choose functional, dispersion treatment, pseudopotentials, basis, integration grid, periodicity, spin, charge and k-point treatment from the system. A Gamma-point liquid cell is a common approximation, not a universal choice. Hybrid functionals increase cost and can change forces; dispersion corrections are part of the Hamiltonian. A metallic system may need smearing and more careful orbital treatment.

Check basis and grid at fixed geometries, then SCF tolerance and timestep in short NVE trajectories. Nuclear timestep convergence cannot compensate for a poor density functional. [Gillan, Alfè and Michaelides](../references.md#michaelides2016) review water's sensitivity to electronic-structure choices.

## Applications, scales and resources

Suitable questions include local liquid structure, solvation, interfacial rearrangement, reactive configurations and training data for learned potentials. A small cell with tens of molecules and femtosecond-scale steps is a teaching starting point. Picosecond-to-tens-of-picoseconds targets and tens-to-hundreds of atoms are broad conventional planning examples; larger/longer work depends on algorithm and hardware.

Each step contains an electronic calculation, often multiple SCF iterations. Dense diagonalization can scale cubically in basis size, while specialized sparse/linear-scaling methods require favorable conditions. Memory can grow quadratically in orbital/basis dimensions; grids and parallel matrix storage matter. CPU/GPU acceleration is build- and workload-dependent. Benchmark the actual cell and convergence settings.

CP2K, suitable plane-wave electronic-structure codes, and force-driver frameworks are common choices. [Tutorial E](../tutorials/05_aimd_water/README.md) supplies a small water input and deterministic geometry generator. It is an **unexecuted teaching input** here; no DFT trajectory or water property is claimed.

## Analysis and limitations

Use RDFs, hydrogen-bond geometry, energy/temperature, coordination changes and charge/electronic descriptors appropriate to the method. A bond-distance crossing can be a transient vibration; chemical assignments require consistent criteria. Short trajectories often under-sample diffusion and rare reactions. A reaction never observed is not evidence that its barrier is prohibitive.

BOMD normally follows one adiabatic electronic surface. Excited-state dynamics, nonadiabatic transitions, spin changes and electron transfer under applied potential may require additional theories. Treating a charged slab with a neutralizing background is not automatically a realistic electrochemical interface.

## Guided exercise

On several fixed water snapshots, tighten SCF tolerance and increase basis/grid quality separately. Compare force differences as well as total energies. Then test $\Delta t$ and $\Delta t/2$ with the same well-converged electronic setup.

**Checkpoint:** constant total-energy offsets between bases may be less important to dynamics than force errors; drift can arise from both integration and electronic nonconvergence. No single tolerance is universally sufficient.

**Sources:** [Quickstep](../references.md#vandevondele2005), [CP2K](../references.md#kuhne2020), [DFT water perspective](../references.md#michaelides2016).
