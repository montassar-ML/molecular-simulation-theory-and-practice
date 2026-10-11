# Optional Case G — MLIP model audit and deployment design

**Level:** research. **Status:** guided research-design exercise; **no runnable pretrained-model case is claimed**. No weights/reference dataset are bundled.

## Objectives and scope

Select a legally usable model, establish whether its training domain covers a chosen solid-state question, and design validation before MD. This optional case is intentionally distinct from the six supplied computational cases.

Start with [CHGNet](../../references.md#chen2023), [MACE-MP](../../references.md#batatia2025) or a task-specific published potential. A public code license does not automatically license every model weight or training dataset. Obtain the exact model card, parameter file, data terms and compatible package version before making a runnable project.

## Guided workflow

1. Define composition, charge/spin, phase, temperature, pressure, defects and target observable.
2. Record model/version/hash and its reference electronic-structure level.
3. Check coverage and construct held-out challenge structures.
4. Compare energies, forces, stress and selected barriers/properties with reference calculations.
5. Test energy–force consistency, stable NVE dynamics and integration convergence.
6. Define an out-of-domain alert and the action taken on triggering it.
7. Budget reference data, inference, validation trajectories and uncertainty independently.

## Deliverable and resources

Produce a model card and decision memo, not fabricated MD output. Suggested columns: domain evidence, independent test, observed error, deployment condition, unresolved risk. Use a workstation/GPU only after compatibility and memory have been measured. Reference DFT may require a separate cluster budget.

**Exercise:** explain why a model with low force RMSE could still miss a migration barrier, and why committee agreement may fail to detect shared extrapolation.

**References:** [MLIP chapter](../../docs/16_ml_potentials.md), [Deringer review](../../references.md#deringer2019), [2026 foundation-model review](../../references.md#foundation2026).
