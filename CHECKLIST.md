# Scientific and reproducibility checklist

## Before computing

- [ ] Question and target observable are explicit.
- [ ] Method provides the required distribution or justified dynamics.
- [ ] Model parameters and structure have traceable provenance and compatible terms.
- [ ] Units, charges, masses, topology, cell and boundary conditions are checked.
- [ ] Numerical convergence controls and slow variables are identified.
- [ ] Resource pilot, storage policy and restart plan are recorded.

## During preparation and production

- [ ] Contacts, forces, SCF/constraints and integration are stable.
- [ ] Equilibration is assessed using relevant slow variables.
- [ ] Production boundaries, restarts and seeds are recorded.
- [ ] Output is frequent enough for the intended estimator.
- [ ] Independent starts or replicas address metastability where needed.
- [ ] Engine/model versions and actual accepted settings are archived.

## Before interpretation

- [ ] RDF self/cross normalization and geometry are correct.
- [ ] MSD uses correct unwrapping, physical time and dimensionality.
- [ ] Fit/integration windows and finite-size sensitivity are assessed.
- [ ] Correlation, blocking/replica uncertainty and confidence assumptions are reported.
- [ ] Bias removal and overlap match the sampling procedure.
- [ ] Model accuracy is evaluated separately from numerical/statistical convergence.
- [ ] MC/GCMC is not interpreted as direct molecular kinetics.
- [ ] PIMD bead propagation is not called exact quantum real-time dynamics.
- [ ] Reactive/MLIP domains support the claimed chemistry.

## Before sharing

- [ ] No credentials, private identifiers, unpublished data or licensed binaries.
- [ ] External assets retain license notices and provenance.
- [ ] Code, notebook outputs and figures distinguish executed and schematic content.
- [ ] References support the actual claims and contain verified metadata.
- [ ] Limitations and failed/environment-dependent checks are documented.
