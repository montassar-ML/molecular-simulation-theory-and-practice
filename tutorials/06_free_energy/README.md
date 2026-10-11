# Case F — Umbrella sampling and WHAM

**Level:** intermediate → advanced. **Resources:** laptop; core Python dependencies only.  
**Execution:** the original one-dimensional sampler and WHAM estimator were executed; analytic-limit tests pass.

## Objectives, theory and model

Recover a known free-energy curve from biased windows, diagnose overlap and distinguish numerical solver convergence from sampling convergence.

The reduced-unit model is $U(x)=4(x^2-1)^2$, with $k_BT=1$ and coordinate measure $dx$. Thirteen harmonic umbrellas with centers from −1.5 to 1.5 and strength 12 sample the double well using symmetric random-walk Metropolis moves. Rejected states are retained. Because there are no hidden coordinates, the equilibrium free energy along $x$ is exactly $U(x)$ plus a constant. This is synthetic teaching physics, not a molecular reaction.

## Run

From repository root:

```bash
python -m scripts.free_energy --steps 30000 --burn 5000 --out outputs/free_energy
```

The seed is explicit. Independent random streams are constructed per window. Output: `windows.npz` (window traces, histograms, analytical curve, estimated probability/free energy and bias centers), `run_manifest.json` and SVG/PNG plots. [Notebook 5](../../notebooks/05_umbrella_wham.ipynb) gives an interactive version.

## Estimator and diagnostics

The code solves equal-bin-width WHAM in log space. It checks that all windows contain samples and that their occupied-bin overlap graph is connected. It returns bin probabilities and free energies. It does not claim automatic statistical uncertainty or molecular rates.

Plot each histogram, inspect gaps, compare reconstructed and analytical curves where sampling is adequate, and repeat with different seeds/lengths/bin widths. Sparse tails are unreliable; do not extrapolate an accurate barrier from an apparently smooth tail. An analytical-histogram unit test verifies the WHAM equations independently of stochastic sampling.

## Convergence and interpretation

Correlated window samples require blocking/decorrelation and a suitable uncertainty estimator. Resample independent blocks or independently equilibrated replicas and rerun the full estimator. The raw-count teaching point estimate does not implement a complete production uncertainty workflow. Disconnecting windows must be diagnosed before interpreting offset differences.

A real molecular umbrella has hidden coordinates; overlap in the plotted CV alone is insufficient. Radial coordinates require geometric-measure awareness. PMF barriers are not automatically transition-state free energies or rate constants; biased crossing times are generally nonphysical.

**Exercise:** remove alternate windows and explain what happens to overlap, estimator stability and uncertainty. Then make the proposals very small: high acceptance can coexist with poor mixing.

**Troubleshooting:** disconnected overlap means add informative windows/sampling; nonconvergence may require better overlap or numerical investigation. Never fix it by inventing offsets between unconnected regions.

**Literature:** [Umbrella sampling](../../references.md#torrie1977), [WHAM](../../references.md#kumar1992), [MBAR](../../references.md#shirts2008), [free-energy chapter](../../docs/14_enhanced_sampling.md).
