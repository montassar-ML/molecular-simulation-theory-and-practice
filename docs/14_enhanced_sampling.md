# 14. Enhanced sampling and free energies

**Level:** advanced. **Outcomes:** distinguish sampling aids from estimators; diagnose overlap and hidden barriers.

## Why bias can help

A trajectory can cross fast vibrations while rarely crossing a basin boundary. Enhanced sampling changes exploration so rare regions receive useful sampling. It does not remove the need for a correct Hamiltonian, representative orthogonal coordinates and uncertainty estimates.

Umbrella sampling, metadynamics and replica exchange use different mechanisms. “Enhanced sampling” is not one ensemble. The estimator must match how the data were generated.

## Probability and free-energy coordinates

For coordinate $s(\mathbf r)$ with probability density $p(s)$ relative to $ds$,

```math
F(s)=-k_BT\ln[p(s)/p_{\rm ref}]+C.
```

Only differences matter, and $p_{\rm ref}$ makes the logarithm dimensionless. Coordinate transformations change the probability measure. For radial separation, $p(r)\propto4\pi r^2g(r)$ in a homogeneous isotropic setting; $-k_BT\ln p(r)$ differs from the radial PMF $-k_BT\ln g(r)$ by the geometric entropy term.

## Umbrella sampling and WHAM

Window $k$ uses $U_k=U+w_k(s)$, often $w_k(s)=\kappa_k(s-s_k)^2/2$. If it samples equilibrium, $p_k(s)=p_0(s)e^{-\beta w_k(s)}/c_k$, where $c_k=\int p_0(s)e^{-\beta w_k(s)}ds$.

For equal-width bins, histogram WHAM solves

```math
p_j=\frac{\sum_k H_{kj}}
{\sum_k n_k\exp[\beta f_k-\beta w_k(s_j)]},
\qquad
e^{-\beta f_k}=\sum_jp_j e^{-\beta w_k(s_j)},\qquad
\sum_jp_j=1 .
```

Here $p_j$ is **bin probability**, $H_{kj}$ retained count, $n_k=\sum_jH_{kj}$, and $f_k=-k_BT\ln c_k$ has energy units. Probability density is $p_j/\Delta s$; equal bin widths change free energies only by a constant. The tutorial uses these equations with log-sum-exp stabilization.

Raw correlated counts provide a teaching point estimate; uncertainty requires time-series treatment or resampling independent blocks/windows. Different window inefficiencies may require effective-sample weighting or appropriately decorrelated input. MBAR uses reduced potentials of all sampled configurations without histogram binning; it also needs overlap and careful correlation handling.

## Metadynamics

Metadynamics deposits a history-dependent bias along selected collective variables. In well-tempered metadynamics the deposition decreases as bias grows, and asymptotically under the method's assumptions

```math
V(s)\simeq-\left(1-\frac1\gamma\right)F(s)+C,\qquad
\gamma=(T+\Delta T)/T>1 .
```

$\gamma$ is dimensionless. Finite-time bias is not automatically a converged free energy. Reweighting needs a method appropriate to the time-dependent bias and its normalization. A hidden slow coordinate can remain unsampled even if the chosen CV looks diffusive.

## Replica exchange and other estimators

Temperature replica exchange swaps configurations between canonical replicas with acceptance
$\min[1,\exp((\beta_i-\beta_j)(U_i-U_j))]$ for the usual proposal and compatible momentum handling. Replicas need energy overlap and round trips; high swap acceptance alone does not guarantee configurational mixing.

Zwanzig free-energy perturbation gives
$\Delta F=-k_BT\ln\langle e^{-\beta(U_1-U_0)}\rangle_0$
for common phase-space measures. It is exact in principle and can have enormous finite-sample bias when rare configurations dominate. Thermodynamic integration uses
$\Delta F=\int_0^1\langle\partial U_\lambda/\partial\lambda\rangle_\lambda d\lambda$.
Numerical quadrature, endpoint behavior and state overlap require checks.

## Resources, applications and limits

A one-dimensional double-well exercise runs on a laptop. Molecular windows or replicas can run independently across CPUs/GPUs; multiply storage and equilibration budgets by window count. PLUMED supplies biases with compatible engines; OpenMM/GROMACS also offer relevant workflows. Coordinate choice can matter more than nominal hardware.

[Tutorial F](../tutorials/06_free_energy/README.md) samples an original double well and compares WHAM to its analytical one-dimensional free energy. It validates an estimator on a toy measure, not molecular reaction rates. The original [metadynamics paper](../references.md#laio2002) includes solvated and conformational applications. Biased crossing times are generally not physical rates without additional justified rate theory.

## Guided exercise

Remove alternate umbrella windows and rerun WHAM. Plot window histograms and the overlap matrix alongside the free energy. Does numerical iteration convergence guarantee a connected or well-sampled estimate?

**Checkpoint:** no. An optimizer can converge despite disconnected information or hidden barriers; uncertainty and independent repeats are essential.

**Sources:** [Torrie–Valleau](../references.md#torrie1977), [WHAM](../references.md#kumar1992), [MBAR](../references.md#shirts2008), [metadynamics](../references.md#laio2002), [well-tempered](../references.md#barducci2008), [replica exchange](../references.md#sugita1999), [Zwanzig](../references.md#zwanzig1954), [Roux](../references.md#roux1995).
