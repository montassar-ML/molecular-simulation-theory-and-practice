# 17. Observables: from coordinates to scientific statements

**Level:** intermediate → research. **Outcomes:** select estimators, units, sampling requirements and defensible interpretations. Read [conventions](CONVENTIONS.md).

## Energetic and mechanical observables

Energy is a model quantity. A total energy in eV for one engine cannot be compared to a molar kJ value or a different energy zero without conversion. Energy per particle helps compare sizes but does not remove model differences.

For equal-time velocities relative to the intended streaming/center-of-mass motion,

```math
K=\frac12\sum_i m_i|\mathbf v_i|^2,\qquad
T_{\rm inst}=\frac{2K}{f_{\rm dof}k_B}.
```

Subtract independent constraints and removed collective degrees of freedom from $f_{\rm dof}$. For unequal masses, center-of-mass subtraction is mass weighted. Equipartition is a classical equilibrium statement; it is not a universal temperature estimator for nonequilibrium or quantum subsystems.

For a three-dimensional pairwise system with the stated virial convention,

```math
p_{\rm inst}=\frac1{3V}
\left[\sum_i m_i|\mathbf v_i|^2+
\sum_{i<j}\mathbf r_{ij}\cdot\mathbf F_{ij}\right].
```

This follows from the mechanical virial or a volume derivative. Both terms have energy units, so $p$ is J m⁻³ = Pa. Constraints, many-body potentials, reciprocal-space electrostatics, tails and external fields require their corresponding contributions. In a constrained finite system, do not automatically replace the kinetic sum by $3Nk_BT$.

The pressure tensor has kinetic dyadics and pair virial dyadics divided by $V$. Some engines return its negative as stress. Isotropic scalar pressure is one-third the trace; a slab or stressed crystal needs tensor interpretation.

## RDF: probability relative to a reference

In a homogeneous isotropic three-dimensional system, a shell from $r_j$ to $r_{j+1}$ has volume $\Delta V_j=(4\pi/3)(r_{j+1}^3-r_j^3)$. For disjoint species $a,b$, let $C_{ab,j}$ count all pairs with $i\in a,j\in b$ in the shell, once each.

```math
g_{ab}(r_j)=\frac{V\langle C_{ab,j}\rangle}
{N_aN_b\Delta V_j},\qquad a\ne b.
```

For identical species, if $C_{aa,j}^{\rm unord}$ counts $i<j$ once,

```math
g_{aa}(r_j)=
\frac{2V\langle C_{aa,j}^{\rm unord}\rangle}
{N_a(N_a-1)\Delta V_j}.
```

The factor two changes unordered to ordered pairs; self pairs are excluded. These ratios are dimensionless and yield unity for a finite ideal gas. Molecular intramolecular exclusions change the reference pair count. If $N$ or $V$ fluctuates, normalize per frame or derive a consistent ensemble-weighted estimator rather than inserting mean density blindly.

For a cubic minimum-image implementation restrict $r<L/2$. Bulk spherical normalization is generally unsuitable for pores and interfaces with inaccessible shell volume. A radial peak is structural probability, not automatically a chemical bond.

With the finite-$N$ identical-species convention, coordination number inside $r_c$ is

```math
n_{ab}(r_c)=4\pi\rho_b^{\rm ref}
\int_0^{r_c}r^2g_{ab}(r)\,dr,\qquad
\rho_b^{\rm ref}=
\begin{cases}
N_b/V,&a\ne b,\\
(N_a-1)/V,&a=b.
\end{cases}
```

The integral has volume units; the count is dimensionless. A first-minimum cutoff is conventional and should be tested for sensitivity. Count neighbors directly as a cross-check.

## MSD, diffusion and the Einstein relation

For unwrapped trajectories and stationary time origins,

```math
{\rm MSD}(t)=\frac1N\sum_i
\left\langle|\mathbf r_i(t_0+t)-\mathbf r_i(t_0)|^2\right\rangle_{t_0}.
```

Use whole-molecule centers of mass for molecular diffusion. Wrapped coordinates produce false bounded motion or jumps. In a changing cell, unwrapping and separating affine box motion require more care than a fixed-cell cumulative minimum image.

For $d$ independent isotropic diffusive dimensions,

```math
D=\lim_{t\to\infty}\frac{{\rm MSD}(t)}{2dt}
=\frac1{2d}\frac{d\,{\rm MSD}}{dt}\quad\hbox{in a linear diffusive regime}.
```

$D$ has m² s⁻¹. The three-dimensional prefactor is $1/6$, one-dimensional is $1/2$. For an anisotropic medium, $D_{\alpha\beta}=\lim\langle\Delta r_\alpha\Delta r_\beta\rangle/(2t)$. A confined direction can plateau and should not be folded into an assumed bulk 3D slope.

To see the origin of $2d$, use $\Delta\mathbf r(t)=\int_0^t\mathbf v(s)ds$ and equilibrium stationarity:

```math
{\rm MSD}(t)=2\int_0^t(t-s)C_v(s)\,ds,\qquad
C_v(s)=\frac1N\sum_i\langle\mathbf v_i(0)\cdot\mathbf v_i(s)\rangle .
```

At long times, if the velocity correlation integral converges,

```math
D=\frac1d\int_0^\infty C_v(s)\,ds.
```

This is the velocity Green–Kubo form. $C_v$ has units m² s⁻²; integration gives diffusion units. At short times $C_v\simeq\langle v^2\rangle$ and MSD is ballistic, proportional to $t^2$. Caging can create an intermediate plateau.

Choose a slope interval after ballistic/caged regimes and before too few time origins dominate. Report fit-window sensitivity, block/replica uncertainty and the number of independent trajectories. Adjacent MSD lags share data; ordinary least-squares slope standard errors are not reliable trajectory uncertainty. The supplied slope utility deliberately reports a point estimate only.

For a homogeneous isotropic liquid in a cubic periodic box, [Yeh–Hummer](../references.md#yeh2004) provide the leading hydrodynamic correction
$D_\infty\simeq D_{\rm PBC}+2.837297\,k_BT/(6\pi\eta L)$.
$\eta$ is shear viscosity (Pa s). This is not a universal correction for anisotropic pores, slabs or arbitrary thermostats; explicit size tests remain important.

## Green–Kubo transport

Using off-diagonal **intensive** pressure $P_{xy}$ in stationary equilibrium,

```math
\eta=\frac{V}{k_BT}\int_0^\infty
\langle\delta P_{xy}(0)\delta P_{xy}(t)\rangle\,dt .
```

Pa² s multiplied by m³/J gives Pa s. Average symmetry-equivalent components only when justified. A noisy integral plateau needs block/replica assessment; integrating noise indefinitely is not convergence.

For a three-dimensional isotropic material with **total extensive heat current** $\mathbf J_Q$ (energy × velocity, J m s⁻¹),

```math
\kappa=\frac1{3Vk_BT^2}\int_0^\infty
\langle\mathbf J_Q(0)\cdot\mathbf J_Q(t)\rangle\,dt .
```

The result is W m⁻¹ K⁻¹. If the engine returns heat-flux density $\mathbf j_Q=\mathbf J_Q/V$, the prefactor becomes $V/(3k_BT^2)$. Multicomponent fluids require appropriate convective/enthalpy subtraction and coupled transport definitions. Energy partition for many-body interactions must match a valid heat-current implementation.

Electrical conductivity similarly uses total charge current $\mathbf J_e=\sum_iq_i\mathbf v_i$:
$\sigma_{\rm el}=(3Vk_BT)^{-1}\int\langle\mathbf J_e(0)\cdot\mathbf J_e(t)\rangle dt$.
The Nernst–Einstein approximation $(Vk_BT)^{-1}\sum_sN_sq_s^2D_s$ omits distinct-ion correlations. Self diffusion alone does not generally determine concentrated-electrolyte conductivity.

## Observable-to-interpretation guide

The formulas below supplement the derivations above. Every row states a plot and a limitation; “equilibrium” means independently assessed stationarity and representation.

| Property and estimator | Meaning and requirements | Valid interpretation / main limitation | Recommended plot |
|---|---|---|---|
| $U$, $E=U+K$ | Model energies; consistent zero and units | NVE drift diagnoses numerical issues; NVT $E$ need not be constant | Energy/particle versus time |
| $T=2K/(f_{\rm dof}k_B)$ | Classical kinetic temperature; correct degrees of freedom | Mean alone does not certify canonical sampling | Trace and distribution |
| Pressure/stress virial | Mechanical response; all force/constraint terms | Sign and volume conventions matter; instantaneous noise is normal | Tensor components and block means |
| $\rho_m=\sum m_i/V$ | Mass density; equilibrated cell/composition | Correct density alone does not validate structure | Density versus time/temperature |
| $g_{ab}(r)$ | Relative pair structure; suitable geometry normalization | Peak is not a permanent bond; confined shells differ from bulk | Species-resolved RDF |
| $n_{ab}(r)$ | Neighbor count; declared cutoff | Cutoff sensitivity and integration normalization | Cumulative coordination |
| MSD, $D$ | Displacements and long-time transport | Physical time, unwrapping, linear regime, finite size | Log–log MSD and fit interval |
| $C_v(t)$ | Velocity memory; frequent velocity saving | Thermostats and output spacing alter integral | VACF and running integral |
| Residence survival $S(t)$ | Continuous persistence in a defined region | Region, recrossing and censoring conventions matter | Survival and uncertainty band |
| Hydrogen-bond count $\sum h_{ij}$ | Geometric donor/acceptor criterion | Distance/angle definitions are operational, not universal bond energies | Count, geometry distribution, lifetime |
| $\rho(z)=\langle N(z)\rangle/(A\Delta z)$ | Interfacial layering; aligned surface and correct area | Drifting interfaces smear profiles; pore accessibility matters | Number/mass profile |
| $\langle P_2(\cos\theta)\rangle$, $P_2=(3\cos^2\theta-1)/2$ | Orientational order relative to a stated normal | Axis choice and angle-measure normalization matter | Orientation versus position |
| $\langle N\rangle(f,T)$ | Equilibrium absolute uptake | Host state, fugacity and excess/absolute conventions | Isotherm with error bars |
| $S_{a/b}=(x_a/x_b)/(y_a/y_b)$ | Mixture enrichment | Pure-component ratio is not mixture selectivity | Selectivity versus loading |
| $F(s)=-k_BT\ln p(s)+C$ | Coordinate free energy, with implicit reference density | Jacobian and bias removal; not automatically an activation rate | PMF and overlap diagnostics |
| $\eta$, $\kappa$ | Collective transport from current correlations | Long tails, current definition and size convergence | Running Green–Kubo integrals |
| $E_{\rm ads}=E_{\rm host+guest}-E_{\rm host}-E_{\rm guest}$ | Chosen static adsorption energy; consistent reference geometries | Not a finite-temperature adsorption free energy | Site energies and reference definitions |
| Surface tension $\gamma_s=(L_z/2)[P_{zz}-(P_{xx}+P_{yy})/2]$ | Planar two-interface slab, suitable mechanics | Factor two assumes two equivalent interfaces; finite size/tails | Block estimates and size series |
| Persistent reactive event count | Model-resolved bond changes | Requires reactive Hamiltonian, criteria, enough events | Species populations and event timelines |

For intermittent residence correlation use $\langle h(0)h(t)\rangle/\langle h\rangle$; returns are allowed. Continuous survival requires the occupant to remain throughout the interval. Their integrals are different quantities. An integral lifetime is finite only when the chosen survival function decays sufficiently and observation/censoring is handled.

Hydrogen-bond criteria should name donor, acceptor, distance threshold, angular convention and periodic treatment. Values such as 3.5 Å and a 150° donor–H–acceptor angle can be illustrative operational choices, not universal definitions. Test sensitivity.

## Guided exercise

Analyze the same LJ trajectory with wrapped and unwrapped coordinates and compare MSDs. Independently count neighbors and integrate the RDF. Explain any factor-of-two or finite-$N$ discrepancy. Then justify why those atomistic coordinates cannot yield hydrogen-bond statistics.

**Sources:** [Allen–Tildesley](../references.md#allen2017), [Green](../references.md#green1954), [Kubo](../references.md#kubo1957), [Yeh–Hummer](../references.md#yeh2004), [Roux](../references.md#roux1995), [electrolyte correlations](../references.md#france2019), [MDAnalysis](../references.md#michaud2011).
