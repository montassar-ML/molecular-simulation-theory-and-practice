# 10. Kinetic Monte Carlo

**Level:** advanced. **Outcomes:** derive a rate-based clock; identify missing-event and rate-model errors.

## Definition and distinction from equilibrium MC

KMC simulates a continuous-time stochastic state model with event rates. It can connect atomistic barriers to long-time reactions or hopping when the states and rates constitute an appropriate Markov description. It does not turn an arbitrary equilibrium MC sequence into physical time.

[Bortz, Kalos and Lebowitz](../references.md#bortz1975) introduced a rejection-free approach for spin systems; [Gillespie](../references.md#gillespie1977) developed exact sampling of a specified chemical master equation. “Exact” refers to that stochastic model, not to the accuracy of its rates relative to a real material.

## Master equation and waiting time

For state probabilities $P_i(t)$ and transition rates $k_{ij}$ from $i$ to $j$,

```math
\frac{dP_i}{dt}=\sum_{j\ne i}[P_j k_{ji}-P_i k_{ij}].
```

Rates have units s⁻¹. In current state $i$, total escape rate is $R_i=\sum_jk_{ij}$. The survival probability solves $\dot S=-R_iS$, hence $S(t)=e^{-R_it}$. Draw two independent uniform variables $u_1,u_2\in(0,1)$:

```math
\Delta t=-\frac{\ln u_1}{R_i},\qquad
P(\hbox{choose }i\to j)=k_{ij}/R_i.
```

Select the event whose cumulative rate interval contains $u_2R_i$, update the state and affected rates, then advance the clock. If $R_i=0$, the state is absorbing within the current catalogue; a zero division is not an acceptable fallback.

## Rate construction

Transition-state theory often gives

```math
k_{ij}(T)=\kappa_{ij}\frac{k_BT}{h}
e^{-\Delta G^\ddagger_{ij}/(k_BT)}.
```

$\kappa$ accounts for recrossing or other corrections under the rate model. Barrier free energies include entropic contributions and depend on reference states. A bare electronic barrier is not automatically a free-energy barrier. Adsorption rates may depend on pressure and impingement; local interactions make rates environment dependent.

At equilibrium a reversible catalogue should obey $\pi_i k_{ij}=\pi_jk_{ji}$. Driven reservoirs can create nonequilibrium steady states with nonzero cycles. Consistency between forward/reverse rates and thermodynamics is essential.

## Assumptions, scales and resources

The state definition must separate fast within-state relaxation from slow events. Exponential waiting times assume memoryless escape with fixed current rates. Correlated recrossings, hidden variables and a changing environment can violate this assumption.

KMC reaches a duration set by sampled rates, not by a femtosecond integrator step. It can span long physical times for slow events, but rapid unproductive events can dominate computational work. Small lattice models run on a laptop. Building a large DFT barrier catalogue, tracking complex environments and parallelizing causally connected events can require HPC. There is no universal time acceleration.

## Application and analysis

[Reuter, Frenkel and Scheffler](../references.md#reuter2004) combined first-principles information with statistical modeling of heterogeneous catalysis. The lesson is to connect environment-dependent events and steady-state populations; this does not justify reusing rates for a different catalyst.

Analyze occupation probabilities, event counts, steady-state turnover, diffusion from rate-based displacements and residence-time distributions. Observables need **time-weighted** averages: for piecewise-constant $A$, $\overline A=\sum_n A_n\Delta t_n/\sum_n\Delta t_n$. Averaging over events alone overweights rapidly escaping states.

## Guided exercise

Implement two states with rates $k_{01}=a$ and $k_{10}=b$. Estimate time fractions and waiting times.

**Checkpoint:** $P_1=a/(a+b)$, $P_0=b/(a+b)$; mean waiting times are $1/a$ and $1/b$. Event counts alternate and would misleadingly suggest equal populations. Increase every rate by a common factor: populations stay unchanged but physical relaxation time changes.

For a surface network, remove one plausible desorption event and predict the consequence. A missing event can create a false absorbing state or alter steady-state selectivity even when all retained barriers are accurate.

**Sources:** [Bortz](../references.md#bortz1975), [Gillespie](../references.md#gillespie1977), [Reuter](../references.md#reuter2004). See the [KMC notebook](../notebooks/04_mc_gcmc_kmc.ipynb).
