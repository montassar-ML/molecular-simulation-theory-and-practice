# 2. Classical molecular dynamics

**Level:** beginner → intermediate. **Outcomes:** interpret trajectories; select a model; organize preparation, production and analysis.

## Definition, history and assumptions

Classical MD advances nuclei or coarse-grained sites under Newton's equations. Simple-fluid studies such as [Rahman's liquid argon](../references.md#rahman1964) demonstrated how microscopic motion generates structure and transport. The potential is a physical approximation, not a numerical implementation detail.

```math
\dot{\mathbf r}_i=\mathbf p_i/m_i,\qquad
\dot{\mathbf p}_i=\mathbf F_i=-\nabla_iU,\qquad
m_i\ddot{\mathbf r}_i=\mathbf F_i.
```

Mass is kg, acceleration m s⁻² and force N. For a time-independent conservative potential, $\dot U=\sum_i\nabla_iU\cdot\mathbf v_i$ cancels $\dot K=\sum_i\mathbf F_i\cdot\mathbf v_i$, so exact dynamics conserves $H=K+U$. Numerical integration, thermostats, changing fields and discontinuous forces modify this argument.

Classical nuclei omit zero-point motion, quantized vibrations and tunneling. An empirical potential approximates electronic response; fixed topology normally cannot describe new bonds. Exact integration cannot remove these limitations.

## Algorithm and preparation

1. Define observables, material and conditions; choose a force field with relevant evidence.
2. Construct coordinates, topology, charges, composition and cell; inspect short contacts.
3. Minimize severe overlaps if needed. Minimization is not thermal equilibration.
4. Draw Maxwell–Boltzmann velocities and remove only intended collective motion.
5. Equilibrate relevant slow variables with suitable ensemble control.
6. Mark production separately and save information required for analysis.
7. Repeat, vary numerical controls and estimate uncertainty before making a comparison.

[Velocity Verlet](04_integrators.md) provides a transparent NVE propagator. Archive seed, engine version, force-field provenance, units, input and restart history. Reinitializing velocities at a restart changes the meaning of a continuous trajectory.

## Periodic boundaries and neighbors

Periodic cells represent an infinite tiling. In an orthorhombic cell the minimum-image displacement is $\Delta x-L_x\operatorname{round}(\Delta x/L_x)$ in each direction. For the simple pair-cutoff model require $r_c<\min(L_x,L_y,L_z)/2$. Triclinic cells need lattice-aware image handling; componentwise rounding in a strongly skewed cell is not generally sufficient.

A neighbor list extends to $r_c+r_{\rm skin}$. If no atom moves more than half the skin before rebuilding, two excluded atoms cannot approach inside the cutoff; cell changes also need accounting. Large skin reduces rebuilds but increases pair work. The teaching Python engine deliberately evaluates all pairs; it is not intended as scalable production software.

Wrapped positions support cell geometry. Unwrapped positions retain image crossings and support displacements. Make molecules whole before calculating their centers of mass. Incorrect image tracking cannot usually be repaired just by storing more frames.

## Scales, resources and software

A few hundred LJ particles are suitable for a laptop. Optimized classical engines can address much larger systems and longer times; thousands to millions of particles and nanosecond-to-microsecond targets are broad planning examples, not guaranteed limits or runtimes. Neighbor memory, reciprocal electrostatics and saved trajectories may dominate costs. Use [measured resource planning](../COMPUTATIONAL_RESOURCES.md).

LAMMPS offers many materials models; GROMACS and OpenMM offer strong molecular workflows. Parameters, constraints, electrostatics, required observables and hardware determine suitability more usefully than a universal ranking.

## Applications and interpretation

A stationary equilibrium trajectory supports structural averages and time correlations consistent with its dynamics. Aggressive random collisions can preserve canonical structure while changing diffusion. Transport analysis needs tested weak coupling or suitable NVE production.

Energy, RDF, coordination, MSD and VACF answer different questions. An RDF peak is enhanced local probability, not a permanent bond. A short-time MSD may be ballistic or caged, not diffusive. Finite size suppresses long-wavelength modes and changes transport.

[Tutorial A](../tutorials/01_lennard_jones/README.md) uses an original force-shifted LJ model for NVT preparation and NVE production. It does not reproduce a published numerical dataset. [Tutorial B](../tutorials/02_solid_state_md/README.md) uses its FCC solid counterpart to contrast bounded vibrations with liquid displacement.

## Guided exercise and checkpoint

Halve the timestep while holding initial state and simulated duration fixed. Plot total energy per particle and measure drift; separately compare RDFs across contiguous production blocks. Which check concerns integration, which sampling, and which says nothing about force-field accuracy?

**Checkpoint:** a sufficiently accurate symplectic NVE method usually shows bounded energy oscillations around a nearby Hamiltonian. Secular heating may indicate bad forces, discontinuous cutoffs, stale neighbors or loose constraints. Two short runs agreeing within noise do not establish convergence.

**Sources:** [Verlet](../references.md#verlet1967), [Rahman](../references.md#rahman1964), [Allen–Tildesley](../references.md#allen2017), [LAMMPS](../references.md#thompson2022).
