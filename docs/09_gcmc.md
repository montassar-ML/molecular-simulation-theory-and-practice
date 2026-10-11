# 9. Grand Canonical Monte Carlo and adsorption

**Level:** intermediate → advanced. **Outcomes:** derive insertion/deletion factors; connect chemical potential and fugacity; interpret uptake without inventing kinetics.

## Definition and physical setting

GCMC samples a subsystem in equilibrium with a particle and heat reservoir at fixed $\mu,V,T$. An adsorbent exchanges molecules with a gas; particle number fluctuates. The host may be rigid or flexible depending on the Hamiltonian and move set. [RASPA3](../references.md#ran2024) supports relevant ensembles; [Han et al.](../references.md#han2008) provide a COF hydrogen-storage application, and [Wilmer et al.](../references.md#wilmer2012) a MOF screening application.

The key assumption is equilibrium with the specified reservoir. A configuration reached by insertion is not a molecule's physical entry path through a pore mouth.

## Deriving acceptance factors

For monatomic particles define $z=e^{\beta\mu}/\Lambda^3$ in m⁻³. Propose insertion uniformly in the full cell volume $V$ and reverse deletion uniformly among $N+1$ particles. Let $p_+(N)$ and $p_-(N+1)$ be the probabilities of choosing these move types at the respective states. The grand canonical measure and proposal ratio give

```math
a_+=\min\left[1,
\frac{p_-(N+1)}{p_+(N)}
\frac{zV}{N+1}e^{-\beta(U_{N+1}-U_N)}
\right].
```

For deletion, define $\Delta U_-=U_{N-1}-U_N$:

```math
a_-=\min\left[1,
\frac{p_+(N-1)}{p_-(N)}
\frac{N}{zV}e^{-\beta\Delta U_-}
\right].
```

These familiar formulas assume consistent treatment of indistinguishability and proposal bookkeeping; do not add a second factorial ratio. With equal constant insertion/deletion selection probabilities, the prefactors reduce to one. At $N=0$, attempting deletion and rejecting keeps that selection convention. If you instead force insertion at $N=0$, the move-probability ratio changes.

The factors $zV$ and $N$ are dimensionless. In a molecular code, internal partition factors, normalized orientations and Rosenbluth weights enter consistently with the molecule definition. Configurational-bias insertion is not governed by a bare Boltzmann factor alone.

## Pressure, fugacity and reference state

For a monatomic ideal gas, $z=\beta p$. For a real gas, use $z=\beta f$ in the matching convention, with $f=\phi p$. A chemical-potential input includes an energy zero and reference convention; copying it between force fields without adjustment is invalid.

If insertion is biased into an accessible subvolume, its proposal density changes. Replacing $V$ by a guessed pore volume in the standard rule without matching the proposal is wrong. Rejected insertions into the host naturally account for excluded regions when proposing in the full simulation volume.

## Isotherms and reporting

At each pressure or fugacity, prepare, equilibrate, sample loading and energy, and estimate correlated-sample uncertainty. Sweep both increasing and decreasing chemical potential where metastability is plausible; hysteresis alone does not distinguish thermodynamic phase behavior from failed equilibration. Dense pores may need CBMC, fractional-particle moves or other specialized algorithms.

Absolute loading counts adsorbates under the model's definition. Excess loading subtracts a bulk reference: $N_{\rm ex}=N_{\rm abs}-\rho_{\rm bulk}V_{\rm ref}$. State the pore/reference volume convention and bulk equation of state. Convert counts to mol kg⁻¹ using host mass, not total fluctuating mass. Mixture selectivity $S_{a/b}=(x_a/x_b)/(y_a/y_b)$ compares adsorbed and reservoir mole fractions; independent pure-component uptake ratios are not generally mixture selectivity.

## Scales, resources, software and uncertainty

GCMC has no physical timescale. Budget attempted moves, effective samples and wall time. Rigid-host force grids can accelerate energies; a host-flexibility model can change both cost and uptake. Pressure points and seeds offer straightforward parallelism. MFI methane in [Tutorial D](../tutorials/04_gcmc_adsorption/README.md) starts on a laptop; difficult loading regimes may need longer CPU jobs.

Analyze loading traces, histograms, adsorption sites and isotherm error bars. Assess force-field cross terms, framework geometry, defects, activation state, charges, quantum corrections for light gases, reservoir nonideality and finite-cell effects. Rigid-host results cannot establish framework gating unless that flexibility is represented.

## Guided exercise

Run the ideal-gas GCMC sampler and compare mean and variance with $zV$. Then use the public MFI structure to prepare several pressure points and independent seeds. Explain the consequence of recording only accepted insertions/deletions.

**Checkpoint:** the ideal distribution is Poisson. Rejections are residence in Markov-chain state space and must be counted; their omission biases equilibrium occupancy. Neither this residence nor MC sweeps measures real adsorption kinetics.

**Sources:** [Frenkel–Smit](../references.md#frenkel2023), [RASPA3](../references.md#ran2024), [porous-material review](../references.md#han2009).
