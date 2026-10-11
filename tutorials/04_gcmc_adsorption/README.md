# Case D — GCMC adsorption in public MFI zeolite

**Level:** intermediate → advanced. **Resources:** laptop CPU pilot; longer independent pressure/seed jobs as needed. RASPA3 installation required for the atomistic example.  
**Execution:** ideal-gas GCMC was executed and tested. The MFI RASPA3 input is an **unexecuted teaching input** in this environment.

## Objectives and model

Connect chemical potential/fugacity, insertion/deletion and equilibrium loading. Build an isotherm without treating MC sweeps as kinetics.

The bundled `MFI_SI.cif` is the public all-silica MFI example from RASPA3, pinned to commit `564b89329c1fd302b12c382995ad08d25d2c41ba`. The MIT license and source checksums are in [provenance](../../data/THIRD_PARTY_PROVENANCE.json). This is a zeolite teaching case; it is not mislabeled as a MOF/COF.

The rigid 2×2×2 framework interacts with one-site neutral methane using the upstream example LJ parameters and Lorentz–Berthelot mixing. The force field specifies a 12 Å cutoff, potential shifting and no tail corrections. Framework charges are present in the file but `ChargeMethod: None` disables Coulomb interactions in this neutral methane exercise. Those settings are not transferable to charged adsorbates or water without redesign.

Parameters $(\epsilon/k_B\ {\rm in\ K},\sigma\ {\rm in\ Å})$: O (53.0, 3.30), Si (22.0, 2.30), CH₄ (158.5, 3.72), as preserved from the upstream example. The teaching copy corrects its Si pseudo-atom element/display label from Al to Si; numerical LJ parameters are unchanged; the cutoff is explicitly set to 12 Å. [Bai et al.](../../references.md#bai2013) supports the zeolite parameter provenance; the bundled methane source string is preserved rather than relabeled as a different force field.

## Run and expected files

Install a compatible RASPA3 build using its [official instructions](https://github.com/iRASPA/RASPA3). From the case's `raspa3` directory:

```bash
raspa3
```

The input uses the pinned source's `NumberOfProductionCycles` schema. Check the executable name and schema against your installed build; some older documentation uses different cycle keys. The `RandomSeed` keyword was also checked in the pinned source's `src/raspakit/input_reader.cpp`. Record the version and confirm that startup output recognizes initialization/production lengths, host, component, move weights and pressure.

From repository root, prepare three low-pressure points and three seeds each:

```bash
python tutorials/04_gcmc_adsorption/make_isotherm.py
```

This creates `outputs/mfi_isotherm/P..._rep...` directories without overwriting existing ones. Run RASPA3 inside each. The pilot assumes fugacity coefficient 1; that is an explicit ideal-reservoir approximation over the chosen teaching range, not a high-pressure equation of state. For an extended pressure range calculate appropriate fugacities.

Preserve complete engine logs, loading block statistics, initialization history and input/version metadata. Exact output filenames vary by RASPA3 release; do not parse a guessed column as uptake. The course does not bundle invented MFI results.

## Analysis and validation

Check loading/energy traces, independent seed agreement, move acceptance, host geometry and minimum-image/cutoff requirements. Confirm the 2×2×2 cell exceeds twice the actual force-field cutoff in each direction. Increase initialization and production until relevant block/replica uncertainties stabilize. Inspect low-insertion acceptance at dense loading; longer runs alone may be inefficient.

Plot absolute loading with uncertainty versus **fugacity or explicitly approximated pressure**. State units and framework mass. Excess adsorption additionally needs a bulk density and reference pore-volume definition. Mixture selectivity requires a mixture model or justified adsorption theory, not a ratio of unrelated single-gas capacities.

## Guided exercise

First open [Notebook 4](../../notebooks/04_mc_gcmc_kmc.ipynb) and verify the ideal-gas Poisson limit. Then construct an MFI isotherm table with columns: pressure, fugacity convention, temperature, replica, initialization/production cycles, mean absolute loading, uncertainty method and evidence of stationarity. Leave result fields empty until execution.

**Troubleshooting:** missing CIF/component files require correct working directory; unknown JSON keys require matching version/schema. Implausible uptake requires checking units, parameters, fugacity, supercell/cutoff and sampling. A smooth isotherm is not proof of accurate parameters.

**Literature:** [GCMC theory](../../docs/09_gcmc.md), [RASPA3](../../references.md#ran2024), [TraPPE-zeo](../../references.md#bai2013), [MOF/COF review](../../references.md#han2009).
