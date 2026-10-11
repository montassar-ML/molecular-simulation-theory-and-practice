# 1. Statistical mechanics: from states to observables

**Level:** beginner → intermediate. **Prerequisites:** elementary calculus, probability and mechanics.  
**Outcomes:** distinguish states and averages; derive canonical probabilities; connect fluctuations and response.

## Why one structure is not a liquid

An optimized geometry is one point on an energy surface. A liquid property concerns a distribution of positions and momenta. A *microstate* specifies microscopic variables; a *macrostate* specifies quantities such as $N,V,E$ and admits many microstates. Phase space is the $6N$-dimensional position–momentum space before constraints.

For Hamiltonian $H(\mathbf r^N,\mathbf p^N)$, a probability density $\pi$ obeys $\int\pi\,d\Gamma=1$. For indistinguishable monatomic particles use $d\Gamma=d\mathbf r^N d\mathbf p^N/(N!h^{3N})$. The measure makes the partition function dimensionless. Constraints require a compatible constrained measure.

## Deriving the canonical distribution

Put a small system in weak thermal contact with a large isolated reservoir. When the system has energy $E$, the reservoir has $E_{\rm tot}-E$. Its compatible microstate count determines the system's probability. Expand the reservoir entropy with $(\partial S/\partial E)_{V,N}=1/T$:

```math
S_R(E_{\rm tot}-E)\simeq S_R(E_{\rm tot})-\frac E T,
\qquad
\pi(\Gamma)=\frac{e^{-\beta H(\Gamma)}}Z,\qquad
Z=\int e^{-\beta H}d\Gamma .
```

This assumes an equilibrated, effectively infinite reservoir and negligible interaction energy between reservoir and system. Two nondegenerate levels separated by $\Delta E$ have probability ratio $e^{-\beta\Delta E}$. With degeneracies $g_1,g_2$, multiply by $g_2/g_1$: energy alone does not determine populations.

Integrating separable quadratic momenta gives

```math
Z(N,V,T)=\frac1{N!\Lambda^{3N}}\int_V e^{-\beta U(\mathbf r^N)}d\mathbf r^N,
\qquad \Lambda=\frac h{\sqrt{2\pi m k_BT}}.
```

$U$ is total configurational energy in J and $\Lambda$ a length. The integral's length$^{3N}$ dimension cancels. Mixtures need a factorial and wavelength for each species. Electronic excitation and quantum exchange are absent.

## Averages, free energy and response

An observable is a function $A(\Gamma)$. Its expectation and Helmholtz free energy are

```math
\langle A\rangle=\frac{\int A e^{-\beta H}d\Gamma}{Z},
\qquad F=-k_BT\ln Z,\qquad
\langle H\rangle=-\left(\frac{\partial\ln Z}{\partial\beta}\right)_{N,V}.
```

Differentiating each Boltzmann weight gives $-H$; differentiating the normalization subtracts the mean contribution. Therefore $-\partial\langle H\rangle/\partial\beta=\langle H^2\rangle-\langle H\rangle^2$. For a temperature-independent Hamiltonian,

```math
C_V=\left(\frac{\partial\langle H\rangle}{\partial T}\right)_{N,V}
=\frac{\langle H^2\rangle-\langle H\rangle^2}{k_BT^2}.
```

J² divided by J K gives J K⁻¹. A thermostat can give the correct mean temperature yet suppress the fluctuations required for heat capacity. Distribution correctness is therefore a physical requirement, not a cosmetic detail.

Set $U=0$ as a check. Then $Z=V^N/(N!\Lambda^{3N})$, $p=k_BT(\partial\ln Z/\partial V)=Nk_BT/V$, and $\langle K\rangle=3Nk_BT/2$ for unconstrained particles. Removing center-of-mass motion changes the finite-system kinetic degree count.

## Ergodicity and practical sampling

The ergodic hypothesis relates long-time and ensemble averages under suitable dynamics. It does not certify a finite trajectory. A trajectory trapped in one basin may show flat energy and tiny local error bars while missing a competing basin. Stationarity, slow-coordinate transitions, replicas initialized in different basins, and agreement among estimators test different aspects of sampling; none proves global ergodicity.

The sample mean $\overline A=M^{-1}\sum_{n=1}^M A_n$ estimates the ensemble mean when sampling is representative. Correlation reduces information: saving every femtosecond does not make configurations independent. [Chapter 18](18_uncertainty_convergence.md) explains effective sample size.

NVE fixes $N,V,E$; NVT exchanges energy; NPT additionally exchanges volume work; grand canonical sampling exchanges particles and energy at fixed $\mu,V,T$. Local averages can become similar in large homogeneous systems while global fluctuations remain ensemble dependent. [Chapter 5](05_ensembles.md) makes these measures explicit.

## Exercise and checkpoint

One state has energy zero and three states have energy $\epsilon$. Derive the excited-state probability for $x=\beta\epsilon$ and its limits. **Checkpoint:** $P_{\rm exc}=3e^{-x}/(1+3e^{-x})$, approaching $3/4$ at high temperature and zero at low temperature. The high-temperature limit counts states, not energy levels.

Two runs have flat energy but different persistent basin populations. Are both equilibrated? **Checkpoint:** a flat trace addresses drift, not equilibrium weights or basin exchange.

**Reading:** [Allen–Tildesley](../references.md#allen2017), [Frenkel–Smit](../references.md#frenkel2023), [Grossfield et al.](../references.md#grossfield2018). See [conventions](CONVENTIONS.md).
