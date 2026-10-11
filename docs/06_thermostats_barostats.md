# 6. Thermostats and barostats

**Level:** intermediate. **Outcomes:** separate equilibrium distribution, relaxation speed and dynamical effects.

## A thermostat changes the propagator

The kinetic estimator $T_{\rm inst}=2K/(f_{\rm dof}k_B)$ fluctuates in equilibrium. Removing every fluctuation is not better temperature sampling.

| Method | Principle | Distribution and dynamics |
|---|---|---|
| Berendsen temperature coupling | Deterministic relaxation toward target | Does not give the full canonical fluctuation distribution; useful relaxation does not establish NVT production validity |
| Andersen | Random Maxwellian velocity replacements | Canonical stationary measure with suitable implementation; collisions disrupt momentum transport |
| Langevin | Friction and matching noise | Canonical in the appropriate limit; friction changes time correlations |
| Nosé–Hoover / chains | Deterministic auxiliary feedback | Canonical invariant measure but ergodicity is not automatic; coupling affects spectra |
| Stochastic velocity rescaling | Stochastic global kinetic control | Designed for canonical kinetic statistics; still test dynamics |

For one Nosé–Hoover variable a schematic continuous form is

```math
\dot{\mathbf p}_i=\mathbf F_i-\zeta\mathbf p_i,\qquad
\dot\zeta=(2K-f_{\rm dof}k_BT)/Q.
```

$\zeta$ has units s⁻¹ and $Q$ units J s². The parameter sets a coupling timescale. Chains improve thermostat-variable sampling but do not guarantee that a molecular system crosses configurational barriers. Small harmonic systems demonstrate why an invariant measure alone is insufficient evidence of ergodicity.

## Pressure control

Berendsen pressure coupling relaxes the cell but does not produce rigorous NPT volume fluctuations. Parrinello–Rahman approaches make the cell matrix dynamic, allowing anisotropic deformation. Modern extended-system implementations need the correct measure and integration corrections; the historical name does not uniquely identify every implementation.

Andersen piston methods and MC volume proposals offer alternatives. The MC barostat accepts energy plus pressure-work changes with a Jacobian and proposal ratio. It samples equilibrium but its rescaling moves are not a physical mechanism of molecular transport.

Isotropic liquids, semi-isotropic membranes, stressed crystals and slabs with vacuum require different cell controls. Applying bulk-pressure coupling to a vacuum direction can collapse a surface cell. In a flexible crystal cell, monitor shear, stress sign, symmetry and mechanical stability.

## Coupling strength and equipartition

There is no universal damping time. Begin from the engine's appropriate documented scheme, then vary coupling while measuring the intended property. A thermostat harmless for the RDF can change the VACF. Strong feedback may conceal bad equipartition between solvent, solute and stiff internal modes. Constraint and collective-motion removal change the degree count.

Monitor subsystem temperatures, cell shape, density, kinetic-energy distributions and appropriate extended conserved quantities. Thermostatting only a selected group can intentionally or accidentally create a nonequilibrium situation; specify which.

A common design equilibrates density in NPT and then uses NVT or NVE production. This is not universally optimal: density uncertainty and ensemble effects remain, and a compressibility calculation requires volume fluctuations. Transport should be checked for coupling sensitivity or obtained from suitable conservative production.

## Guided exercise

Compare exact kinetic-energy rescaling each step with a canonical distribution. Which statistic can agree while another fails?

**Checkpoint:** the mean kinetic temperature can match exactly while $\operatorname{var}(K)$ is zero instead of $f_{\rm dof}(k_BT)^2/2$ for independent canonical quadratic modes. Examine distributions rather than just average temperatures.

**Sources:** [Berendsen](../references.md#berendsen1984), [Andersen](../references.md#andersen1980), [Nosé](../references.md#nose1984), [Hoover](../references.md#hoover1985), [Parrinello–Rahman](../references.md#parrinello1981), [Bussi](../references.md#bussi2007).
