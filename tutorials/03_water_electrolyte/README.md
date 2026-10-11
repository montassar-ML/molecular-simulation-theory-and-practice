# Case C — Water and electrolyte

**Level:** intermediate. **Resources:** CPU laptop/workstation; OpenMM plus core requirements. GPU use is optional and platform dependent.  
**Execution:** a 2,653-atom short CPU run was executed (883 waters and four ions). This is a preparation/analysis smoke test, not a converged transport result.

## Objectives and physical model

Examine hydrogen-bond geometry, O–O and Na–O structure, ion coordination and molecular diffusion. Understand why electrostatics, water model, ion parameters and periodic treatment must be consistent.

The script loads OpenMM's `amber14-all.xml` and `amber14/tip3p.xml`, so water and ions follow the bundled compatible parameter definitions. It creates an approximately 3 nm cubic TIP3P water box with nominal 0.15 mol L⁻¹ NaCl. Discrete ion counts make realized concentration differ slightly from nominal. It uses PME, 0.9 nm real-space cutoff, rigid water/H-bond constraints and a 2 fs step.

The NPT preparation uses a Langevin thermostat and MC barostat at 300 K and 1 bar. Production switches to a fixed cell with Verlet NVE and removes center-of-mass momentum once. No reaction/proton-transfer capability is claimed for this fixed-topology model.

## Reproduce

From repository root:

```bash
python -m pip install openmm
python tutorials/03_water_electrolyte/run_openmm.py --out outputs/water
python tutorials/03_water_electrolyte/analyze.py outputs/water
```

Defaults are 1,000 preparation steps and 2,000 production steps (4 ps production), deliberately too short for precise liquid transport. Use `--salt-molar 0` for pure water; extend runs and vary `--seed` for an actual study. A supported GPU platform can be selected with `--platform CUDA` or another installed platform. The recorded smoke test used CPU, not GPU.

Outputs: `initial_production.pdb`, `system.xml`, checkpoint, preparation/production CSV, `trajectory.npz`, manifest, analysis SVG/PNG and `analysis_summary.json`. The serialized system preserves the actual parameterized Hamiltonian, but the exact environment should also be recorded.

## Analysis assumptions

The supplied analysis supports a **fixed cubic** production cell. It makes each water whole around oxygen, computes mass-weighted centers, and reconstructs image crossings from consecutive saved frames. This is valid only when saved displacements can be uniquely unwrapped; increase output frequency/check image logic for other conditions.

O–O RDF uses the same-species finite-$N$ convention; Na–O uses disjoint cross-species normalization. The 0.32 nm Na–O coordination cutoff is illustrative; choose a physically justified first-shell boundary and report sensitivity.

A geometric hydrogen bond is counted when O–O <0.35 nm and donor–H–acceptor angle >150°. These operational criteria are not universal chemical bond definitions. The count is bonds per water (each donor–acceptor assignment counted once), not the number of incident bonds per water, which counts both ends. No hydrogen-bond lifetime is inferred from the short run.

## Validation and expected plots

Inspect density during NPT, energy drift during NVE, O–O/Na–O RDFs, water COM MSD and hydrogen-bond time series. Compare longer independent runs, alternative output intervals and box sizes. Test PME tolerance/cutoff and timestep without changing the underlying force field unintentionally. Compare density and RDF against the **same model and conditions**, then against experiment with model limitations stated.

Diffusion needs a resolved linear regime, enough time origins, finite-size assessment and replica/block intervals. Conductivity also depends on ion cross correlations; Nernst–Einstein self-diffusion estimates omit those terms.

## Troubleshooting and exercise

Missing template: confirm matching water/ion XML files and residue names. Instability: inspect contacts, constraints and timestep. Wrong temperature: check degrees of freedom and units. Unphysical MSD: check molecular reconstruction, unwrapping and fixed cell.

**Exercise:** compare pure water and salt solution after equal-quality equilibration, not merely equal duration. Report realized ion count/concentration and uncertainties. Explain why this model cannot answer whether a proton transfers between waters.

**Literature:** [Jorgensen water models](../../references.md#jorgensen1983), [water-model review](../../references.md#vega2011), [finite-size diffusion](../../references.md#yeh2004), [ion correlations](../../references.md#france2019), [OpenMM](../../references.md#eastman2017).
