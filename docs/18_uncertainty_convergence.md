# 18. Statistical uncertainty and convergence

**Level:** intermediate → research. **Outcomes:** quantify correlation, build defensible intervals and distinguish four sources of error.

## Five different claims

| Claim | Question | Evidence |
|---|---|---|
| Algorithmic correctness | Does code implement its equations? | Analytic limits, detailed balance, finite-difference forces, independent implementations |
| Numerical convergence | Are discretization/solver choices adequate? | Timestep, cutoff/grid, SCF, constraints, bead-number tests |
| Statistical convergence | Is the estimated ensemble quantity precise and representative? | Slow-variable sampling, independent starts, blocking, replicas |
| Model accuracy | Is the Hamiltonian/domain suitable? | Independent reference structures, energies, barriers and properties |
| Experimental agreement | Does this model match measured conditions? | Correct composition, uncertainty, ensemble and measurement definition |

One successful test does not imply the others. Precise sampling of an incorrect potential can produce a precisely wrong answer.

## Autocorrelation and effective sample size

For stationary scalar observations $A_n$ separated by $\Delta t$, define $C(k)=\langle(A_n-\mu)(A_{n+k}-\mu)\rangle$ and $\rho(k)=C(k)/C(0)$. Expanding the variance of the mean as a double covariance sum gives the finite-$M$ identity

```math
\operatorname{var}(\overline A)=
\frac{\sigma_A^2}{M}
\left[1+2\sum_{k=1}^{M-1}\left(1-\frac kM\right)\rho(k)\right].
```

If correlation decays well before the run ends, define $g=1+2\sum_{k\ge1}\rho(k)$, $N_{\rm eff}=M/g$, and $\operatorname{SE}(\overline A)\simeq\sigma_A/\sqrt{N_{\rm eff}}$. $g$ is dimensionless. With this course's convention, $\tau_{\rm int}=\Delta t\,g/2$.

Estimated long-lag correlations are noisy. Summing them to the end of a short series can give nonsense. Windowing/initial-positive-sequence and related estimators trade bias and variance. The supplied utility uses a conservative first-nonpositive cutoff and clamps $g\ge1$; it is a teaching diagnostic that does not exploit negative correlation or guarantee reliable estimates for multiscale/nonstationary data. Compare blocking and replicas.

## Blocking

Divide post-equilibration data into $B$ contiguous equal blocks of length $L$. If blocks are approximately independent, estimate the standard error from block means:

```math
{\rm SE}_{\rm block}=
\frac{s_{\bar A_b}}{\sqrt B},\qquad
s_{\bar A_b}^2=\frac1{B-1}\sum_b(\bar A_b-\bar A)^2.
```

Increase block length and inspect whether SE stabilizes while retaining enough blocks. Too-small blocks underestimate uncertainty; too-few blocks make the variance itself uncertain. A plateau that appears after only two blocks is not persuasive.

A nominal 95% interval is $\bar A\pm t_{0.975,B-1}{\rm SE}_{\rm block}$ when block means are approximately independent and compatible with the Student model. Report $L,B$, discarded data and assumptions. Bootstrapping individual correlated frames is wrong; resample independent blocks or replicas using an appropriate scheme.

## Replicas and nonlinear quantities

For $R$ genuinely independent identically prepared run estimates $D_r$, their standard deviation divided by $\sqrt R$ estimates the uncertainty in their mean, with Student intervals when justified. Between-replica scatter can reveal initialization dependence invisible within one run.

For nonlinear quantities such as diffusion slopes, free-energy differences and selectivity ratios, propagate uncertainty by rerunning the **entire estimator** on blocks or replicas. Slopes at adjacent MSD lags share time origins; treating every lag as independent understates uncertainty. Free-energy windows need overlap and correlated-sample treatment, not just tiny optimizer residuals.

Rare-event counts may need Poisson or survival methods rather than Gaussian intervals. Zero observed events does not establish zero rate. A censored residence time needs censoring-aware analysis.

## Sampling quality before arithmetic

No uncertainty formula rescues a chain that never visits a relevant basin. Check stationarity of slow observables, replica agreement from different starts, transitions and robustness to analysis windows. A low apparent autocorrelation within one basin does not measure the unobserved exchange time.

Report uncertainty as standard error or interval, specify coverage and method, and separate statistical from model/systematic uncertainty. Do not combine unrelated uncertainties by quadrature unless the assumptions for doing so are justified.

## Guided exercise

Generate an AR(1) series $x_n=\phi x_{n-1}+\epsilon_n$ for $|\phi|<1$. Its normalized correlation is $\phi^k$ and $g=(1+\phi)/(1-\phi)$. Compare naive, autocorrelation and block SE estimates. Repeat with several independent seeds.

**Checkpoint:** for $\phi=0.9$, the theoretical $g=19$; a finite-run estimate will fluctuate. This is an analytical benchmark for a stochastic teaching process, not molecular evidence. Increasing save frequency at fixed observation time does not proportionally increase effective information.

**Sources:** [Grossfield et al.](../references.md#grossfield2018), [Flyvbjerg–Petersen](../references.md#flyvbjerg1989), [Chodera](../references.md#chodera2016). [Notebook](../notebooks/03_uncertainty.ipynb).
