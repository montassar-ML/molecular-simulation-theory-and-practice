# 4. Integration, stability and time resolution

**Level:** intermediate. **Outcomes:** derive Verlet; separate stability, accuracy and faithful dynamics.

## Taylor expansion and velocity Verlet

Add expansions of $\mathbf r(t+\Delta t)$ and $\mathbf r(t-\Delta t)$ to cancel odd derivatives:

```math
\mathbf r_{n+1}=2\mathbf r_n-\mathbf r_{n-1}
+\mathbf a_n\Delta t^2+O(\Delta t^4).
```

The equivalent velocity-Verlet kick–drift–kick form is

```math
\begin{aligned}
\mathbf v_{n+1/2}&=\mathbf v_n+\Delta t\,\mathbf F_n/(2m),\\
\mathbf r_{n+1}&=\mathbf r_n+\Delta t\,\mathbf v_{n+1/2},\\
\mathbf v_{n+1}&=\mathbf v_{n+1/2}+\Delta t\,\mathbf F_{n+1}/(2m).
\end{aligned}
```

Assume a separable Hamiltonian, position-dependent conservative forces and constant timestep. Global position and velocity errors are second order. The symmetric composition is reversible and symplectic, which helps long-time energy behavior but cannot repair an incorrect force.

Leapfrog stores half-step velocities: $\mathbf v_{n+1/2}=\mathbf v_{n-1/2}+\mathbf F_n\Delta t/m$, then drifts positions. Reconstructed full-step velocities and kinetic-energy estimators must follow the correct staggering. Different instantaneous temperature definitions cannot be compared blindly.

## Stability versus accuracy

For $\ddot x=-\omega^2x$, seek the Verlet solution $x_n=e^{in\theta}$. Substitution yields

```math
\cos\theta=1-\frac{(\omega\Delta t)^2}{2}.
```

Stable oscillations require $\omega\Delta t<2$; accurate periods require a much smaller step. A bounded trajectory can have incorrect vibrational frequencies. Flexible bonds, close repulsive contacts, fictitious CPMD electrons and ring-polymer springs may set the fastest timescale.

Halving $\Delta t$ doubles force evaluations for the same physical duration. Compare conservation and target statistics, not just successful termination. Chaotic trajectories diverge microscopically even when both integrations are accurate; use ensemble comparisons.

## Langevin propagation

```math
d\mathbf v_i=
(\mathbf F_i/m_i-\gamma\mathbf v_i)\,dt+
\sqrt{2\gamma k_BT/m_i}\,d\mathbf W_i.
```

$\gamma$ has units s⁻¹; independent Wiener increments have variance $dt$. BAOAB uses half force kick (B), half drift (A), exact Ornstein–Uhlenbeck velocity update (O), then half drift and kick. The O step is $\mathbf v\leftarrow c\mathbf v+\sqrt{(1-c^2)k_BT/m}\boldsymbol\xi$ with $c=e^{-\gamma\Delta t}$.

The tutorial projects noise onto the zero-center-of-mass subspace for equal masses and uses $3N-3$ kinetic degrees of freedom. Finite timestep still creates discretization bias. Noise and drag must satisfy fluctuation–dissipation balance; arbitrary added noise does not sample the specified temperature. Friction changes dynamics even when equilibrium structure is correct.

## Beyond the basic integrator

Explicit Euler poorly conserves oscillator energy and is a useful counterexample. Multiple-time-step methods can reduce expensive force evaluations but introduce resonances unless force splitting and timesteps are appropriate. Constraints and cell dynamics require compatible algorithms. Appending ad hoc volume rescaling to NVE does not produce correct NPT sampling.

Monitor constraint residuals, potential continuity, neighbor updates, SCF force consistency for AIMD, and the engine's appropriate conserved quantity. Thermostatted subsystem energy is expected to change, so an NVE drift criterion cannot simply be imposed on NVT data.

## Exercise and checkpoint

Integrate a harmonic oscillator at steps $0.1/\omega$, $1/\omega$ and $2.1/\omega$. Plot energy and phase portrait; predict instability. Then compare an analytical pair force against finite differences before integrating LJ particles.

**Checkpoint:** $1/\omega$ can be stable but have substantial phase error; $2.1/\omega$ is beyond the stability bound. Force finite differences and integration convergence test distinct components.

**Sources:** [Verlet](../references.md#verlet1967), [Allen–Tildesley](../references.md#allen2017), [Langevin splitting](../references.md#leimkuhler2013). [Tutorial A](../tutorials/01_lennard_jones/README.md).
