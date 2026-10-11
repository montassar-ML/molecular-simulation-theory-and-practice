# Learning roadmap and assessments

This sequence can support a semester or self-paced study. Session lengths depend on prior background; no fixed completion-time promise is made.

| Module | Reading | Exercise / artifact | Completion criterion |
|---|---|---|---|
| 1. States and probability | 1, conventions | Boltzmann-degeneracy exercise; Notebook 1 | Derive normalized populations and define the measure |
| 2. Forces and integration | 2–4 | LJ force-gradient and timestep tests | Distinguish stable from accurate integration |
| 3. Ensembles and preparation | 5–7 | Kinetic distribution and equilibration memo | Explain controls, fluctuations and slow variables |
| 4. Structure and transport | 17 | Case A/B, Notebook 2 | Correct RDF/MSD normalization and units |
| 5. Statistical evidence | 18, 22 | Notebook 3, block/replica analysis | Explain effective sample size and failure of stationarity |
| 6. Stochastic methods | 8–10 | Notebook 4; ideal GCMC and two-state KMC | Derive acceptance and time-weighted populations |
| 7. Water and adsorption | Cases C/D, 21 | Model provenance and isotherm protocol | Separate uptake, mobility and force-field assumptions |
| 8. Electronic forces | 11, 11B, Case E | SCF/basis/grid/timestep test design | Separate BO, CP and quantum-nuclear ideas |
| 9. Reactive and reduced models | 12–13 | Reaction-domain and coarse-graining audit | Identify lost physics and needed references |
| 10. Free-energy methods | 14, Case F | Notebook 5 and overlap diagnostics | Derive bias removal; challenge a false-convergence claim |
| 11. Quantum nuclei and MLIPs | 15–16 | Notebook 6 and optional model card | State equilibrium/dynamics and interpolation/extrapolation limits |
| 12. Resources and capstone | 19–22, resource worksheet | Research protocol with literature map | Match question, method, resources, evidence and claim |

## Assessment rubric

Use four dimensions rather than rewarding impressive snapshots:

- **Physical reasoning:** correct model, ensemble, assumptions and observable.
- **Numerical/statistical evidence:** meaningful convergence tests and uncertainty.
- **Reproducibility:** complete inputs, units, versions, seeds and analysis.
- **Interpretation:** supported claims, appropriate literature and explicit limitations.

A strong capstone can identify that a proposed calculation cannot answer the original question. For example, an equilibrium adsorption isotherm cannot directly determine a membrane permeation rate.

## Capstone prompt

Choose a public toy or documented open structure. Define one falsifiable question; select a method; justify a force model; identify the quantity to estimate; plan numerical and statistical checks; run an affordable pilot; estimate full resources from measured costs; and cite foundation, synthesis and application literature.

Report completed work separately from proposed work. No private data, undisclosed force-field files or claimed calculations without logs. Refer to [CONTRIBUTING](CONTRIBUTING.md) for an inspectable submission format.
