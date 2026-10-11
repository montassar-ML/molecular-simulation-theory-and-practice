# Symbols, measures, units, and reporting conventions

[Course home](../README.md) · [Statistical mechanics](01_statistical_mechanics.md)

Theory uses SI unless explicitly stated otherwise. Engine inputs use their documented native units. Energies in equations are per configuration or particle, not per mole; replace $k_B$ by $R$ when using molar energies consistently.

| Symbol | Definition | SI unit |
|---|---|---|
| $N,V,T,p$ | Particle number, volume, thermodynamic temperature, pressure | 1, m³, K, Pa |
| $\mathbf r_i,\mathbf v_i,\mathbf p_i,m_i$ | Position, velocity, momentum, mass | m, m s⁻¹, kg m s⁻¹, kg |
| $U,K,H$ | Potential energy, kinetic energy, Hamiltonian $H=K+U$ | J |
| $\mathbf F_i=-\nabla_iU$ | Force on particle $i$ | N |
| $\beta=1/(k_BT)$ | Inverse thermal energy | J⁻¹ |
| $\mu,f,z$ | Chemical potential, fugacity, activity density $z=e^{\beta\mu}/\Lambda^3$ for monatomic particles | J, Pa, m⁻³ |
| $\Lambda=h/\sqrt{2\pi m k_BT}$ | Translational thermal wavelength | m |
| $d,f_{\rm dof}$ | Spatial dimension; active quadratic kinetic degrees of freedom | 1 |
| $\rho=N/V$ | Number density, not mass density | m⁻³ |
| $\epsilon,\sigma,\tau$ | LJ energy, length, time; $\tau=\sigma\sqrt{m/\epsilon}$ | J, m, s |

Reduced LJ variables: $r^*=r/\sigma$, $U^*=U/\epsilon$, $T^*=k_BT/\epsilon$, $t^*=t/\tau$, $\rho^*=\rho\sigma^3$, $p^*=p\sigma^3/\epsilon$. Tutorials A/B set $\sigma=\epsilon=m=k_B=1$. They are not measured argon data. Their fixed-center-of-mass temperature uses $3N-3$ degrees of freedom.

Use $\mathbf r_{ij}=\mathbf r_i-\mathbf r_j$, with $\mathbf F_{ij}$ the force on $i$ due to $j$. The virial $\sum_{i<j}\mathbf r_{ij}\cdot\mathbf F_{ij}$ is positive for repulsion. Pressure is positive in compression. Some engines report tensile-positive stress, the negative pressure tensor. Constraints and reciprocal-space forces contribute to the virial.

A coordinate-space canonical density is defined with respect to $d\mathbf r^N$; a full partition function also includes momenta and indistinguishability. Variable-$N$ derivations must track factorials, volume and proposal probabilities together.

The RDF uses finite-$N$ normalization: ordered identical-species pair counts are divided by $N_a(N_a-1)\Delta V/V$, so an ideal gas gives $g_{aa}=1$. Disjoint cross species use $N_aN_b\Delta V/V$. Some engines use $N_a^2$, giving an ideal-gas plateau $1-1/N_a$; convert explicitly.

Diffusion uses unwrapped particle or whole-molecule center-of-mass coordinates in a fixed cell, stationary equilibrium without bulk flow, and an explicitly selected $d$-dimensional subspace. General anisotropy requires a tensor. Physical time requires a justified dynamical propagator.

For normalized autocorrelation $\rho_A(k)$, define $g=1+2\sum_{k\ge1}\rho_A(k)$ and $\tau_{\rm int}=\Delta t\,g/2$, giving $N_{\rm eff}=M/g$. Definitions without the half-lag term also exist; quote yours.

Every plotted line is identified as simulation output, analytical reference, or schematic. Illustrative hardware numbers are arithmetic assumptions, not measured benchmarks.
