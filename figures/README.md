# Original educational figures

All figures have editable SVG text and reproducible [Python source](../scripts/make_figures.py). White backgrounds, restrained colors and serif typography are intentional. PNG copies are for convenient preview.

| Figure | Interpretation |
|---|---|
| [1. Taxonomy](01_method_taxonomy.svg) | Schematic organization; categories can overlap |
| [2. MD versus MC](02_md_vs_mc.svg) | Dynamical trajectory versus equilibrium chain |
| [3. Ensembles](03_ensembles.svg) | Controlled variables and reservoir exchanges |
| [4. Force-field components](04_force_field_components.svg) | Conceptual terms, not a complete functional form |
| [5. Workflow](05_md_workflow.svg) | Evidence-guided stages |
| [6. LJ potential and force](06_potential_and_force.svg) | Analytical untruncated pair function |
| [7. MSD](07_msd_interpretation.svg) | Explicitly schematic crossover; no measured diffusion |
| [8. RDF](08_rdf_interpretation.svg) | Explicitly schematic shell structure |
| [9. GCMC](09_gcmc_workflow.svg) | Equilibrium reservoir/proposal workflow |
| [10. BOMD and CPMD](10_bomd_vs_cpmd.svg) | Electronic minimization versus fictitious propagation |
| [11. Free energy](11_free_energy_landscape.svg) | Analytical toy landscape and biased weights |
| [12. Scales/costs](12_scales_and_costs.svg) | Qualitative cost drivers, no invented benchmark axis |

Regenerate from repository root with `python scripts/make_figures.py`. Actual short-run plots are kept separately in `validation/` and labeled as executed teaching simulations.
