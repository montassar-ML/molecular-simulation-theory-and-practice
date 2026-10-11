# 15. Path-integral molecular dynamics

**Level:** advanced. **Outcomes:** derive the ring-polymer mapping and distinguish equilibrium quantum sampling from real-time dynamics.

## Definition and foundation

PIMD samples quantum equilibrium nuclear statistics through a classical-like extended ring polymer. The starting object is the quantum partition function $Z=\operatorname{Tr}e^{-\beta\hat H}$, not Newtonian dynamics. [Ceperley](../references.md#ceperley1995) reviews path integrals in condensed matter; [Markland–Ceriotti](../references.md#markland2018) discuss chemical applications.

For distinguishable nuclei with $\hat H=\hat T+\hat V$, a Trotter splitting into $P$ imaginary-time slices gives, up to known prefactors,

```math
Z_P\propto\int \prod_{s=1}^P d\mathbf R^{(s)}
\exp\left[-\frac{\beta}{P}\sum_{s=1}^P
\left\{V(\mathbf R^{(s)})+
\sum_i\frac12m_i\omega_P^2
|\mathbf R_i^{(s)}-\mathbf R_i^{(s+1)}|^2\right\}\right],
\quad \omega_P=\frac{P}{\beta\hbar}.
```

Bead $P+1$ is bead 1. One equivalent implementation samples this bracketed ring-polymer Hamiltonian at inverse temperature $\beta/P$; another rescales the potential/kinetic conventions to temperature $T$. Mixing the two conventions creates wrong spring strengths. Spring energy has units J.

## Meaning of beads and estimators

Beads represent imaginary-time path points of the **same** nucleus, not independent molecules. In the $P\to\infty$ limit, the appropriate estimators recover quantum equilibrium properties under the chosen Hamiltonian. The primitive discretization is approximate at finite $P$.

Position-dependent observables can be estimated by bead averages. Kinetic energy is not obtained by equating auxiliary bead velocities with physical nuclear velocities. Thermodynamic and centroid-virial estimators have different variances. Nuclear permutation exchange is omitted in ordinary distinguishable-particle molecular PIMD; special low-temperature systems require it.

## Algorithm and assumptions

Replicate coordinates into a ring, add harmonic springs, select suitable masses/normal-mode propagation and thermostats, evaluate physical forces for each bead, and converge bead count. Fast internal spring modes can limit naive timesteps; normal-mode and multiple-time-step schemes help under their assumptions.

The required number of beads grows with inverse temperature and relevant quantum frequencies. A rule based only on atom count is meaningless. Converge the target observable with $P$, timestep, potential accuracy and trajectory length separately.

## Dynamics is a separate problem

The artificial MD used to sample the ring polymer does not generate exact real-time quantum trajectories. RPMD, CMD and thermostatted variants are approximate dynamical theories with specific strengths and artifacts. Calling a bead MSD an exact quantum diffusion coefficient is incorrect. A PIMD equilibrium distribution can still reveal isotope effects or changes in hydrogen-bond structure without making a dynamical claim.

## Applications, software and resources

Light nuclei, hydrogen bonds, isotope effects, zero-point motion and low-temperature materials motivate PIMD. [Cheng et al.](../references.md#cheng2019) combined quantum-nuclear sampling, learned potentials and free-energy methods for water/ice thermodynamics. Their specific model and convergence work are not replaced by simply choosing many beads.

i-PI acts as a driver connected to force providers; compatible classical or electronic engines supply forces. Small harmonic models are laptop work. Realistic PIMD roughly multiplies force work by bead count before contraction/parallel optimization; electronic forces often require clusters. Bead replicas offer parallelism but communication, memory and load balance matter.

## Guided exercise

For a one-dimensional quantum harmonic oscillator, compare classical variance with

```math
\langle x^2\rangle_{\rm Q}
=\frac{\hbar}{2m\omega}
\coth\left(\frac{\beta\hbar\omega}{2}\right).
```

Both sides have length² units. Show the high-temperature limit $k_BT/(m\omega^2)$ and the nonzero low-temperature zero-point limit. Plot as a function of $\beta\hbar\omega$ in the notebook.

**Checkpoint:** quantum delocalization can persist at zero temperature. This variance says nothing by itself about exact dynamical correlation functions.

**Sources:** [Ceperley](../references.md#ceperley1995), [Markland–Ceriotti](../references.md#markland2018), [i-PI](../references.md#kapil2019), [Cheng](../references.md#cheng2019).
