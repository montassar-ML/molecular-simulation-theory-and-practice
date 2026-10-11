# 11B. Car–Parrinello molecular dynamics

**Level:** advanced. **Outcomes:** explain fictitious electronic dynamics and adiabatic separation; distinguish CPMD from BOMD and real-time electronic propagation.

## Definition and foundations

[Car and Parrinello (1985)](../references.md#car1985) introduced coupled nuclear and orbital dynamics through an extended Lagrangian. Instead of independently minimizing the electronic state at every step, CPMD evolves auxiliary orbital variables while aiming to keep them near the instantaneous ground-state manifold.

A schematic orthonormal-orbital Lagrangian is

```math
\mathcal L=
\frac12\sum_I M_I\dot{\mathbf R}_I^2+
\frac{\mu_e}{2}\sum_n\langle\dot\psi_n|\dot\psi_n\rangle
-E_{\rm KS}[\{\psi_n\},\mathbf R]
+\sum_{mn}\Lambda_{mn}
(\langle\psi_m|\psi_n\rangle-\delta_{mn}).
```

$\mu_e$ is a fictitious inertia, not electron mass. $\Lambda_{mn}$ enforce orbital orthonormality. Factors can be absorbed into the definition of $\mu_e$ in different conventions. Varying this Lagrangian yields nuclear forces from the orbital-dependent energy and auxiliary equations of the form $\mu_e\ddot\psi_n=-\delta E_{\rm KS}/\delta\psi_n^*+\sum_m\Lambda_{nm}\psi_m$, with matching variational convention.

The conserved extended energy contains nuclear kinetic, fictitious electronic kinetic and electronic potential contributions. It is not simply the physical nuclear Hamiltonian.

## Algorithm and assumptions

Initialize minimized orbitals, choose a sufficiently small fictitious inertia and timestep, propagate orbitals/nuclei with orthonormality constraints, and monitor energy exchange. The goal is adiabatic separation: auxiliary electronic frequencies should be fast relative to nuclear motion so orbital excitations do not accumulate.

A finite electronic gap helps separation. Metallic or small-gap systems can be problematic. Large fictitious inertia can increase coupling and effective mass effects; tiny inertia requires small timesteps. The best setting cannot be inferred from atom count alone.

Orbitals in CPMD are not propagated by the physical time-dependent Schrödinger equation. Their kinetic energy does not represent an electronic temperature in the usual thermodynamic sense. CPMD trajectories do not directly predict electronic excitation dynamics.

## Comparison with BOMD

| Choice | BOMD | CPMD |
|---|---|---|
| Electronic step | Ground-state solve each nuclear step | Auxiliary orbital propagation |
| Main numerical controls | SCF/basis/grid and nuclear timestep | Fictitious inertia, electronic preparation, separation and timestep |
| Energy diagnostic | Physical BO energy in suitable NVE | Extended energy plus electronic/nuclear energy exchange |
| Failure mode | Inconsistent/noisy SCF forces | Loss of adiabatic separation; fictitious heating |

Both retain functional, basis, finite-size and sampling errors. “CP2K” is a software name, not a synonym for CPMD: the supplied CP2K exercise is Born–Oppenheimer MD.

## Systems, scales and resources

Liquids and insulating condensed phases historically motivated CPMD. Computational resources are similar in class to electronic-structure MD, but per-step cost and required step count differ. It is not universally cheaper than modern BOMD. Suitable CPMD implementations, pseudopotentials and integration schemes must be selected explicitly.

Budget electronic orbital storage, constraint/orthonormalization work and more frequent steps where needed. A multicore workstation can support a small teaching system; research studies often need clusters. Spatial and temporal reach depends on basis size and electronic structure, not a fixed method-wide ceiling.

## Analysis and scientific limits

Structural observables and nuclear time correlations need convergence with respect to fictitious inertia and other controls. Monitor electronic kinetic energy and nuclear–electronic exchange. A constant extended energy alone does not demonstrate that nuclei stay on the desired BO surface.

The original paper establishes the method's research value; this course does not supply an executed CPMD simulation. For current work compare with BOMD forces on representative CPMD snapshots and, where possible, with independently converged short BOMD trajectories.

## Guided exercise

For a hypothetical set of CPMD runs at decreasing fictitious inertia, specify plots needed to assess the limit: extended-energy drift, auxiliary kinetic energy, nuclear temperature, force differences to ground-state calculations, and a structural/dynamical observable. Why is agreement of RDFs alone insufficient for validating vibrational dynamics?

**Checkpoint:** equilibrium structure may be insensitive to a mass renormalization that shifts dynamical frequencies.

**Sources:** [Car–Parrinello](../references.md#car1985), [CP2K review](../references.md#kuhne2020), [Allen–Tildesley](../references.md#allen2017).
