# 8. Equilibrium Monte Carlo

**Level:** intermediate. **Outcomes:** derive acceptance probabilities; distinguish a Markov chain from molecular motion.

## Definition and history

Monte Carlo estimates equilibrium expectations using random configurations. Markov-chain Monte Carlo constructs a correlated sequence with a chosen stationary distribution. The [Metropolis algorithm](../references.md#metropolis1953) and [Hastings generalization](../references.md#hastings1970) are foundational. Ordinary MC transitions are computational proposals; they are not Newtonian trajectories.

A liquid can be sampled by translating one molecule, rotating it, regrowing a chain or exchanging replicas. Such moves need not resemble actual motion, provided they sample the intended measure.

## Detailed balance and the general rule

Let $\pi(x)$ be a target probability density, $q(y|x)$ a proposal density and $a(x\to y)$ its acceptance probability. Detailed balance requires equality of equilibrium probability fluxes:

```math
\pi(x)q(y|x)a(x\to y)
=\pi(y)q(x|y)a(y\to x).
```

The Metropolis–Hastings choice satisfies it:

```math
a(x\to y)=\min\left[
1,\frac{\pi(y)q(x|y)}{\pi(x)q(y|x)}
\right].
```

All densities must be defined with compatible measures. The ratio is dimensionless. For canonical coordinates and a symmetric proposal, the normalizer cancels and $a=\min[1,e^{-\beta\Delta U}]$. Asymmetric proposals require the $q$ ratio; “accept with Boltzmann factor” is not generally sufficient.

Detailed balance is sufficient for stationarity, not necessary for all correct samplers. Irreducibility and suitable aperiodicity are also needed for convergence from arbitrary starts. Rejection self-transitions often provide aperiodicity, but disconnected configuration sectors remain a problem.

## Algorithm

Choose a state and record its energy. Propose a move, compute the local or total energy change, draw a uniform random number, and accept if its logarithm is below the log acceptance ratio. Otherwise retain the old state. **Record retained states after rejections too.** Keeping only accepted states overweights easily escaped regions and samples a different distribution.

Adapt proposal widths during preparation, then freeze them for ordinary production unless using a theoretically valid adaptive method. A high acceptance can mean tiny ineffective moves; low acceptance can mean large rejected moves. Neither rate alone measures independent information per computational cost.

## Assumptions, resources and scales

The target equilibrium distribution and model Hamiltonian must be physically appropriate. MC can treat classical or specialized quantum equilibrium models, but this chapter uses classical coordinates. It has configuration count or sweeps, not a molecular timescale. A sweep convention should specify attempted moves per particle; particle number changes complicate the convention in GCMC.

A small LJ or oscillator MC model runs on a laptop. Long polymers, dense insertion problems, host flexibility and first-principles energies can make individual proposals expensive. Independent chains parallelize easily; a single chain can have sequential bottlenecks. RASPA3, FEASST and specialized codes support different move sets. An engine's support for both MC and MD does not make its MC histories dynamical.

## Analysis and application

Average energies, RDFs and equilibrium populations using correlated-sample uncertainty. Compare with MD at the same potential, density, temperature and cutoff convention. Their structural distributions should agree after convergence; trajectory-dependent observables need not.

The executable harmonic MC extension in the notebook checks $\langle x^2\rangle=k_BT/k$ for $U=kx^2/2$. A liquid application uses translation moves and RDFs. [Jorgensen et al.](../references.md#jorgensen1983) used equilibrium sampling to compare water models, illustrating that different models can predict different structures under the same nominal thermodynamic conditions.

## Limitations and exercise

Hidden barriers and disconnected proposals can prevent representative sampling. Correlation and initialization bias survive millions of rejected or microscopic moves. Agreement of two chains started in the same basin is weak evidence.

**Exercise:** use a position-dependent proposal width in a harmonic well. First ignore the proposal ratio, then include the Gaussian forward/reverse densities. Compare the histogram to the analytical Gaussian. **Checkpoint:** symmetry of an increment distribution around each current point does not imply $q(y|x)=q(x|y)$ when its width varies with $x$.

Explain why a plot of particle displacement against MC sweeps is not a diffusion measurement. The proposal width is freely chosen and does not define a physical clock.

**Sources:** [Metropolis](../references.md#metropolis1953), [Hastings](../references.md#hastings1970), [Frenkel–Smit](../references.md#frenkel2023), [Grossfield](../references.md#grossfield2018).
