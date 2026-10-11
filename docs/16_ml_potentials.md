# 16. Molecular dynamics with machine-learning potentials

**Level:** advanced → research. **Outcomes:** design reference data, validation and deployment checks; separate learned accuracy from reference accuracy.

## Definition and development

An ML interatomic potential maps a structure and relevant state variables to energy and/or forces. Energy-conserving models usually compute forces by differentiation of a learned scalar energy. [Behler–Parrinello](../references.md#behler2007) established a neural-network representation of high-dimensional surfaces. [Deringer et al.](../references.md#deringer2019) review materials applications. Recent [CHGNet](../references.md#chen2023), [MACE-MP](../references.md#batatia2025) and [foundation-model reviews](../references.md#foundation2026) expand scope but do not eliminate out-of-domain errors.

A local energy model often has $E_\theta=\sum_i\varepsilon_\theta(\mathcal N_i)$, where $\mathcal N_i$ describes an atomic neighborhood. Symmetries, cutoffs, charge/spin information and long-range terms define its expressivity. Locality can fail for long-range electrostatics or changing electronic states unless represented appropriately.

## Training objective and units

A typical schematic objective is

```math
L(\theta)=w_E\,{\rm MSE}(E_\theta-E_{\rm ref})
+w_F\,{\rm MSE}(-\nabla E_\theta-\mathbf F_{\rm ref})
+w_S\,{\rm MSE}(S_\theta-S_{\rm ref}).
```

Energy, forces and stress have different units; the weights and normalization must make comparisons intentional. Per-atom versus total energy errors answer different questions. Stress conventions and cell derivatives must match labels.

Reference calculations have their own functional, basis, SCF, charge and spin approximations. A model accurately reproducing them inherits their systematic error. Learning cannot create information absent from its reference domain.

## Data and algorithm

Define deployment conditions before collecting data. Include equilibrium configurations, relevant strain, surfaces, defects, high-energy contacts, competing phases and reaction environments where needed. Use consistent reference settings and reject failed calculations.

Split data by trajectory, structural family, composition or physical regime rather than random adjacent frames, which leak near-duplicates. Hold out challenge sets beyond interpolation. Train, evaluate energies/forces/stress, test invariances, then run conservative dynamics and property-specific validation.

Active learning proposes new states where a model is uncertain, requests reliable reference labels, and retrains under version control. Committee disagreement, extrapolation scores and descriptor distances are useful alerts, not calibrated proofs of correctness. Correlated models can agree confidently and be wrong.

## Deployment checks

Record model file hash, model version, training provenance, reference Hamiltonian, element/charge domain, units, software version, neighbor cutoff and device precision. Check finite-difference energy–force consistency, short NVE drift, force/strain stability and the intended property against held-out reference information. A low test RMSE does not guarantee a correct melting point, barrier or diffusion coefficient.

If instability appears, distinguish integration error from missing repulsive training coverage. Thermostatting away a catastrophic energy injection hides the failure. Stop or flag out-of-domain states and inspect them before treating their trajectory as physical evidence.

## Applications, scales and resources

Learned models can extend reference-quality-like sampling within validated domains. [Cheng et al.](../references.md#cheng2019) used a learned intermediate to access water/ice free energies with reference corrections and quantum effects. [CHGNet](../references.md#chen2023) presents solid-state applications. These demonstrations do not validate those models for arbitrary aqueous ions, surfaces or reactions.

GPU inference often helps, but graph construction, model size, neighbor density and communication matter. Dataset generation may cost more than training. Budget reference DFT, storage, training/validation and production separately; do not quote a universal DFT speedup.

The optional [MLIP exercise](../tutorials/07_mlip_md/README.md) is a model-audit project rather than a downloaded-weight runnable claim. No external pretrained weights or reference dataset are redistributed or claimed executed.

## Guided exercise

Design a validation split for a potential intended for ion diffusion through a solid. Include a held-out temperature, defect concentration and strained structure. Explain why randomly holding out 10% of consecutive frames may overstate generalization. Specify an uncertainty trigger and a safe response to it.

**Checkpoint:** trajectories and local environments, not filenames alone, define leakage. Use independent configurations and targeted barriers/transport tests, and distinguish predicted uncertainty from observed error.

**Sources:** [Behler–Parrinello](../references.md#behler2007), [Deringer](../references.md#deringer2019), [CHGNet](../references.md#chen2023), [MACE-MP](../references.md#batatia2025), [2026 review](../references.md#foundation2026).
