# 3. Force fields and potential-energy models

**Level:** intermediate. **Outcomes:** connect energy terms to physical approximations; distinguish convergence from parameter validity.

## The potential defines the simulated material

A force field is more than element parameters. Atom types, exclusions, 1–4 scaling, constraints, mixing rules, electrostatic boundaries and cutoffs jointly define it. Combining components from unrelated parameterizations can invalidate their original calibration.

A common fixed-topology molecular form is

```math
U=\sum_b\frac{k_b}{2}(r-r_0)^2+
\sum_a\frac{k_\theta}{2}(\theta-\theta_0)^2+
\sum_t\sum_n k_n[1+\cos(n\phi-\delta_n)]+U_{\rm nb}.
```

$k_b$ is J m⁻², angles are radians, $k_\theta,k_n$ are energies and $\delta_n$ is a phase. Engines may omit $1/2$ and use a different numerical force constant. Improper torsions constrain out-of-plane preferences. Read the exact functional form before transferring parameters.

## Lennard-Jones energy and force

```math
u(r)=4\epsilon[(\sigma/r)^{12}-(\sigma/r)^6],\qquad
\mathbf F_{ij}=24\epsilon[2(\sigma/r_{ij})^{12}-(\sigma/r_{ij})^6]
\frac{\mathbf r_{ij}}{r_{ij}^2}.
```

The force follows by differentiation with $\mathbf r_{ij}=\mathbf r_i-\mathbf r_j$. Its dimension is energy/length. The minimum is $r=2^{1/6}\sigma$, with energy $-\epsilon$; closer particles repel. The inverse-twelfth repulsion is convenient, not an exact electron-overlap law.

Lorentz–Berthelot rules use $\sigma_{ab}=(\sigma_a+\sigma_b)/2$, $\epsilon_{ab}=\sqrt{\epsilon_a\epsilon_b}$. These are assumptions; adsorption cross terms may need independent fitting.

## Cutoffs change the Hamiltonian

Truncation sets the potential to zero beyond $r_c$. Potential shifting makes energy continuous but leaves a force discontinuity. The tutorial uses force shifting:

```math
u_{\rm FS}(r)=u(r)-u(r_c)-(r-r_c)u'(r_c)\quad(r<r_c),
\qquad u_{\rm FS}=0\quad(r\ge r_c).
```

Then $f_{\rm FS}(r)=-u'(r)+u'(r_c)$ vanishes continuously at the boundary. This modifies forces throughout the cutoff sphere and defines a different fluid from unshifted LJ. Smooth switching is another model convention.

For homogeneous isotropic fluids with $g(r)\simeq1$ beyond the cutoff, integrating the omitted unshifted LJ tail yields

```math
\frac{U_{\rm tail}}N=2\pi\rho\int_{r_c}^{\infty}r^2u(r)\,dr
=8\pi\rho\epsilon\left[\frac{\sigma^{12}}{9r_c^9}
-\frac{\sigma^6}{3r_c^3}\right].
```

This correction is not automatically suitable for pores, interfaces or force-shifted models. Pressure needs its own virial correction. The toy runs apply none.

## Electrostatics

Point charges in vacuum interact via $q_iq_j/(4\pi\epsilon_0r)$. Explicit-solvent models generally do not add a bulk dielectric factor: solvent charges already generate screening, unless the parameterization explicitly specifies otherwise.

Periodic Coulomb sums require a summation convention. Ewald splits real-space short-range and reciprocal-space smooth contributions with self and boundary corrections. PME/PPPM use interpolation and FFTs; [Darden et al.](../references.md#darden1993) establish a mesh method. Validate real cutoff, reciprocal mesh, error tolerance, net charge and boundary treatment together. A uniform compensating background in charged periodic cells is not a physical counterion atmosphere. Slabs require appropriate treatment of image interactions across vacuum.

## Constraints, polarization and reactivity

Constraints fix selected distances and remove kinetic degrees of freedom. SHAKE/RATTLE-type iterations require tolerances; loose constraints can cause drift. Rigid water permits larger timesteps but removes vibrational modes.

Polarizable force fields add induced dipoles, Drude oscillators or fluctuating charges. Their extra response variables bring convergence or timestep requirements and require a compatible parameter set. Polarization improves one approximation; it does not certify all properties.

Reactive models such as [ReaxFF](12_reactive_md.md) use environment-dependent bond order. Their reaction barriers and products need validation. A nonreactive fixed topology cannot generally describe bond breaking. Metals often need EAM or related many-body descriptions; covalent solids need suitable angular or bond-order physics. An LJ crystal is a teaching solid, not a faithful metal.

## Guided exercise

For aqueous ions near an oxide, make a provenance table for water, ions, surface, charges, cross interactions and constraints. Identify which calibration and independent tests support the combined model.

**Checkpoint:** bulk-water accuracy and plausible snapshots do not establish surface transferability. Check ion hydration/coordination and surface–water binding at relevant conditions. Separate parameter uncertainty from numerical electrostatics convergence.

**Sources:** [Allen–Tildesley](../references.md#allen2017), [Darden](../references.md#darden1993), [Ryckaert](../references.md#ryckaert1977), [Daw–Baskes](../references.md#daw1984), [Vega–Abascal](../references.md#vega2011).
