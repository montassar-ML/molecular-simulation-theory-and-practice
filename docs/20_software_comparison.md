# 20. Software roles and selection

**Evidence checked:** 11 October 2026. Links to “current” documentation can change. Match documentation to the installed version and record enabled packages/platforms.

## Engines

| Package | Main purpose and methods | Applications | License/access summary | Parallel/GPU qualification | Learning demand |
|---|---|---|---|---|---|
| LAMMPS | Classical particle MD; many potentials and selected MC-related fixes | Solids, fluids, polymers, interfaces, reactive/ML models when supported | GPL family; verify the installed distribution and component terms | MPI/OpenMP; GPU/KOKKOS and other packages accelerate supported styles | Moderate–high: explicit units, styles and parameters |
| GROMACS | Classical molecular MD and free-energy workflows | Water, electrolytes, biomolecules, membranes and compatible models | LGPL 2.1 or later | MPI/OpenMP and supported CUDA/SYCL/HIP paths; algorithm/build dependent | Moderate: topology and workflow conventions |
| OpenMM | Programmable molecular MD toolkit and custom forces/integrators | Molecular systems and algorithm prototyping | Mostly MIT and LGPL components; consult distribution license files | CPU and CUDA/HIP/OpenCL platforms; do not assume distributed MPI MD from Python alone | Moderate for Python users; high for new algorithms |
| CP2K | Electronic structure, BOMD and multiscale atomistic calculations | Liquids, solids, interfaces, reactions | GPL; dependencies have their own terms | MPI/OpenMP; selected grid, matrix and electronic kernels accelerated depending on build | High: electronic and dynamical convergence |
| RASPA3 | Classical MC/GCMC/Gibbs and supported MD | Adsorption, fluid equilibrium, nanoporous materials | MIT | Parallel workflows and implementation-specific threading; no blanket GPU guarantee | Moderate–high: fugacity, moves, host/model definitions |

RASPA3's current source distinguishes implemented from experimental features, including aspects of flexibility. Confirm that the specific move/model combination you need is supported. A code offering MD and MC still produces nonphysical-time equilibrium MC chains.

## Frameworks and sampling tools

| Package | Role | Supported workflow and access | Hardware meaning | Learning demand |
|---|---|---|---|---|
| ASE | Python atomistic framework with calculators, builders, optimizers and MD | LGPL; forces come from selected calculator | Parallel/GPU behavior mainly belongs to calculator; not a universal electronic engine | Low–moderate Python; model knowledge still essential |
| i-PI | Socket-based driver for advanced MD and quantum-nuclear sampling | GPL/MIT licensing options/components; inspect distributed license files | Distributes force tasks to clients; client engines determine CPU/GPU force capability | High for multi-client/restart setup |
| PLUMED | Collective variables, biasing, enhanced sampling and analysis | LGPL; compatible engine interface or standalone analysis | MPI/OpenMP and selected acceleration paths; bias can alter host-engine performance | Moderate–high: CVs, bias and reweighting |

PLUMED does not ordinarily replace a general molecular force engine. ASE and i-PI do not make every connected calculator equally appropriate. Keep the distinctions between driving coordinates, evaluating forces and estimating free energies.

## Analysis and visualization

| Package | Role and appropriate use | Access model | Parallel/GPU qualification | Learning demand |
|---|---|---|---|---|
| MDAnalysis | Python trajectory readers, selections and analysis | LGPL family; release 2.8 announcement specifies LGPL 2.1+; check exact installed LICENSE | Selected analyses support parallel backends; no blanket GPU coverage | Moderate Python; careful units/topology |
| OVITO | Atomistic visualization and structural analysis | Basic and Pro differ; current Basic binary license page states MIT; Pro commercial terms | Multithreaded analyses and rendering capabilities vary; rendering GPU is not MD acceleration | Low for viewing, moderate for pipelines |
| VMD | Molecular visualization, scripting and selected analyses | Custom University of Illinois license; specific commercial/redistribution conditions | Selected GPU/parallel features; not a general MD engine | Low for viewing, moderate–high for Tcl/Python scripting |

License summaries support access planning, not redistribution of binaries. This repository redistributes only the specifically attributed MIT RASPA3 teaching data; it does not redistribute the engines.

## Documentation, tutorials and scientific citations

| Package | Official documentation | Tutorial entry | Scientific citation |
|---|---|---|---|
| LAMMPS | [Manual](https://docs.lammps.org/) | [Official tutorial index](https://www.lammps.org/documentation/tutorials/) | [Thompson 2022](../references.md#thompson2022); [Gravelle 2025](../references.md#gravelle2025) |
| GROMACS | [Manual](https://manual.gromacs.org/current/) | [Interactive tutorials](https://tutorials.gromacs.org/) | [Abraham 2015](../references.md#abraham2015) |
| OpenMM | [Guide](https://docs.openmm.org/latest/userguide/) | [Cookbook](https://github.com/openmm/openmm-cookbook) | [Eastman 2017](../references.md#eastman2017) |
| CP2K | [Manual](https://manual.cp2k.org/) | [AIMD exercise](https://www.cp2k.org/exercises:common:aimd) | [Kühne 2020](../references.md#kuhne2020) |
| RASPA3 | [Documentation](https://iraspa.github.io/RASPA3/) | [Basic examples](https://iraspa.github.io/RASPA3/examples_basic.html) | [Ran 2024](../references.md#ran2024) |
| ASE | [Documentation](https://ase.gitlab.io/ase/) | [MD tutorial](https://ase.gitlab.io/ase/examples_generated/03-tutorials/md.html) | [Larsen 2017](../references.md#larsen2017) |
| i-PI | [Documentation](https://docs.ipi-code.org/) | [Source and examples](https://github.com/i-pi/i-pi) | [Kapil 2019](../references.md#kapil2019) |
| PLUMED | [Manual](https://www.plumed.org/doc-v2.9/user-doc/html/index.html) | [Tutorials](https://www.plumed.org/doc-v2.9/user-doc/html/tutorials.html) | [Tribello 2014](../references.md#tribello2014) |
| MDAnalysis | [Documentation](https://docs.mdanalysis.org/) | [Learning resources](https://www.mdanalysis.org/learning_MDAnalysis/) | [Michaud-Agrawal 2011](../references.md#michaud2011) |
| OVITO | [Manual](https://www.ovito.org/manual/) | [Tutorials](https://www.ovito.org/manual/tutorials/) | [Stukowski 2010](../references.md#stukowski2010) |
| VMD | [Official site](https://www.ks.uiuc.edu/Research/vmd/) | [Tutorial](https://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/) | [Humphrey 1996](../references.md#humphrey1996) |

Additional MC teaching: [NIST FEASST overview](https://pages.nist.gov/feasst/OVERVIEW.html). It is an alternative resource, not silently substituted for a supplied RASPA3 input.

## Selection exercise

Choose software for (a) methane uptake in a rigid zeolite, (b) water diffusion, (c) proton transfer at an oxide, and (d) quantum-nuclear structural effects. For each, identify the force model, engine/driver, analysis package and missing validation.

**Checkpoint:** GCMC for equilibrium uptake; physical MD for diffusion; electronically or chemically validated reactive forces for proton transfer; a PIMD driver plus suitable force provider for equilibrium nuclear quantum effects. Package popularity is not an evidence-based selection criterion.

Capability evidence: [LAMMPS accelerators](https://docs.lammps.org/Speed_packages.html), [GROMACS performance](https://manual.gromacs.org/current/user-guide/mdrun-performance.html), [OpenMM platforms](https://docs.openmm.org/latest/userguide/library/01_introduction.html), [CP2K GPU status](https://www.cp2k.org/gpu), [RASPA3 source](https://github.com/iRASPA/RASPA3), [OVITO licenses](https://www.ovito.org/manual/licenses/index.html), [VMD license](https://www.ks.uiuc.edu/Research/vmd/current/LICENSE.html), [MDAnalysis 2.8 licensing](https://www.mdanalysis.org/2024/11/22/release-2.8.0/).
