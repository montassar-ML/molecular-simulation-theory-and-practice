# 5. Ensembles and statistical weights

**Level:** intermediate. **Outcomes:** choose reservoir variables; derive sampling weights; interpret finite-system fluctuations.

| Ensemble | Imposed variables | Fluctuating quantities | Typical question |
|---|---|---|---|
| NVE | $N,V,E$ | Kinetic temperature, instantaneous pressure | Conservative dynamics and transport |
| NVT | $N,V,T$ | Energy and pressure | Structure at specified density |
| NPT | $N,p,T$ | Energy, volume and pressure estimator | Equilibrium density, compressibility |
| Grand canonical | $\mu,V,T$ | Particle number and energy | Adsorption from a reservoir |

## Controls and estimators are different

A constant-temperature ensemble means a fixed bath temperature and a specified distribution of subsystem states. Instantaneous kinetic temperature still fluctuates. Similarly a barostat controls a cell distribution; it does not force every microscopic pressure reading to equal the target.

NVE states lie on an energy shell, $\pi_E(\Gamma)\propto\delta[E-H(\Gamma)]$. Canonical states have $\pi_T=e^{-\beta H}/Z$. The same structure can have nonzero weight in both; the global energy distribution differs.

## NPT and the volume Jacobian

In Cartesian coordinates, a configurational NPT measure is proportional to $e^{-\beta[U+p_{\rm ext}V]}d\mathbf r^N dV$. Under isotropic scaling $\mathbf r_i=V^{1/3}\mathbf s_i$, the Jacobian is $V^N$:

```math
\pi(\mathbf s^N,V)\propto V^N
e^{-\beta[U(\mathbf s^N;V)+p_{\rm ext}V]}.
```

For a symmetric proposal **in $V$**, the Metropolis acceptance becomes

```math
a=\min\left[1,e^{-\beta(\Delta U+p_{\rm ext}\Delta V)}
(V'/V)^N\right].
```

A proposal symmetric in $\ln V$ instead contributes another $V'/V$ from its forward/reverse proposal ratio, giving exponent $N+1$ in this parameterization. Rigid molecular center-of-mass scaling changes the number of scaled translational objects. Derive the appropriate Jacobian rather than copying the atomic exponent.

In correctly sampled isotropic NPT,

```math
\kappa_T=\frac{\langle V^2\rangle-\langle V\rangle^2}
{k_BT\langle V\rangle}.
```

The dimension is inverse pressure. A weak-coupling barostat that suppresses volume fluctuations can give a plausible density and an incorrect compressibility.

## Grand canonical measure

For monatomic particles,

```math
\Xi(\mu,V,T)=\sum_{N=0}^{\infty}
\frac{e^{\beta\mu N}}{N!\Lambda^{3N}}
\int_V e^{-\beta U_N}d\mathbf r^N.
```

Let $z=e^{\beta\mu}/\Lambda^3$ (inverse volume). An ideal gas has $\Xi=e^{zV}$ and a Poisson number distribution with mean and variance $zV$. More generally $\operatorname{var}(N)=k_BT(\partial\langle N\rangle/\partial\mu)_{V,T}$.

Internal molecular partition functions and orientation conventions affect activity definitions. For the corresponding monatomic reservoir convention, $z=\beta f$, where fugacity $f=\phi p$ has pressure units. Pressure equals fugacity only in an ideal-gas approximation. [GCMC](09_gcmc.md) uses these factors explicitly.

## Ensemble equivalence has limits

Many local observables approach ensemble equivalence for large homogeneous stable phases. Small systems, coexistence, long-range interactions and constraints can make differences significant. Global fluctuation formulas remain ensemble specific: an NVE trajectory with negligible energy variance cannot estimate canonical heat capacity by the NVT energy-variance formula.

Choose an ensemble from the experimental constraint and intended estimand, then choose an algorithm that samples its measure. Matching a label in an input file does not validate the implemented distribution.

## Guided exercise

For an ideal gas, the scalar-volume NPT density is proportional to $V^N e^{-\beta pV}$. Integrate to find its mean and mode.

**Checkpoint:** mean $(N+1)k_BT/p$; mode $Nk_BT/p$ for $N>0$. The finite-system difference vanishes relatively as $N$ grows. This is a measure-dependent finite-size result, not a violation of thermodynamics.

**Sources:** [Frenkel–Smit](../references.md#frenkel2023), [Allen–Tildesley](../references.md#allen2017), [Andersen](../references.md#andersen1980).
