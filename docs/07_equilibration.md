# 7. Preparation, equilibration and production

**Level:** beginner → research. **Outcomes:** base equilibration decisions on relevant observables and preserve their provenance.

## Equilibrium is not an elapsed-time setting

Energy may settle quickly while ions remain in their initial coordination environments or a polymer retains its initial shape. A flat energy trace does not establish equilibrium of these slower coordinates. Relaxation times depend on the question, composition, phase and initialization.

Minimization removes local force imbalance; it samples neither finite-temperature equilibrium nor basin weights. A minimized solid can still have incorrect thermal stress. A density plateau can coexist with a trapped topology.

Record source geometry, modifications, atom types, charges, cell, composition, parameters, minimization, velocity seed, ensemble history and restarts. Mark the production boundary and the evidence for it. Do not silently concatenate duplicated restart frames or reinitialize velocities when claiming a continuous trajectory.

## Diagnose stationarity and representation separately

Inspect raw series, cumulative means and contiguous block means of energy, density and at least one slow structural variable. Compare early and late production. Start replicas from distinct states where feasible and assess basin populations and transitions.

Automated equilibration detection can optimize effective sample size after discarding a prefix for a chosen scalar series ([Chodera](../references.md#chodera2016)). It cannot detect a phase never visited. Record the decision rule, preserve the full trace, and avoid choosing a discard solely because it gives a desired result.

Initial restraints can help relax solvent but alter the Hamiltonian. Remove them before unrestrained production or explicitly include them in the reported model. Gradual heating and pressure relaxation should be documented as preparation, not pooled with a stationary production ensemble.

## Sampling design

Independent replicas help identify persistent initialization dependence and quantify between-run uncertainty. Replicas sharing one unequilibrated structure may inherit a common bias. Increasing output frequency gives more correlated frames, not more physical coverage.

For rare processes, longer runs, diverse initial basins, enhanced sampling or a narrower estimand may be appropriate. If no transition occurs, report what was observed and its duration; assigning zero rate or infinite lifetime requires an additional statistical argument.

Choose a stopping criterion from the precision needed to resolve the scientific comparison. Report total and discarded duration, output interval, number of replicas, stationarity diagnostics, slow-coordinate behavior and uncertainty method separately. Once model uncertainty dominates, more trajectory time may not improve the claim; when sampling dominates, agreement with one experiment can still be accidental.

## Guided exercise

Three runs show stable energy and density, but two stay in basin A and one in B. Is averaging the three equally justified?

**Checkpoint:** only if their weights are independently justified. First establish whether basin exchange matters to the observable; then seek sampling or free-energy information about the relative populations. A stable trace is evidence about local stationarity, not correct global weights.

Write an equilibration statement for Tutorial A using its actual trace and one limitation. The packaged short run is not long enough to certify precise bulk-liquid diffusion.

**Sources:** [Grossfield](../references.md#grossfield2018), [Chodera](../references.md#chodera2016), [Flyvbjerg–Petersen](../references.md#flyvbjerg1989). Continue to [uncertainty](18_uncertainty_convergence.md).
