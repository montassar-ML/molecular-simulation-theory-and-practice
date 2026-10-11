# Educational-resource review and research provenance

Research date: **11 October 2026**. This file records what was inspected, the pedagogical inference and how it influenced this original course. Linked resources were not treated as permission to copy. Publisher/Crossref bibliographic checks are recorded in [reference audit](data/reference_audit.json).

| Resource inspected | Effective teaching feature | Course design inference and limitation |
|---|---|---|
| [LAMMPS official tutorial index](https://www.lammps.org/documentation/tutorials/) | Routes readers to beginner and application material | Provide navigation by question and level; an engine index is not a unified theoretical curriculum |
| [LAMMPS tutorial site source](https://github.com/lammpstutorials/lammpstutorials.github.io) | Stepwise lessons linked to runnable inputs | Pair each exercise with checkpoints; do not reproduce lesson text |
| [LAMMPS tutorial inputs](https://github.com/lammpstutorials/lammpstutorials-inputs) | Visible inputs make workflows inspectable | Keep input, model definition and expected artifacts together; imported inputs still need model validation |
| [GROMACS tutorials](https://tutorials.gromacs.org/) | Interactive notebooks from basics through free energy | Use notebooks for numerical exploration; provide explicit prerequisites and convergence limits |
| [OpenMM cookbook](https://github.com/openmm/openmm-cookbook) | Small Python recipes plus tested notebook infrastructure | Separate small executable checks from long external-engine examples |
| [ASE MD tutorial](https://ase.gitlab.io/ase/examples_generated/03-tutorials/md.html) | Builders, calculators and propagators exposed as distinct objects | Teach model–integrator separation; warn that calculator availability is not validation |
| [CP2K AIMD exercise](https://www.cp2k.org/exercises:common:aimd) | Links electronic forces to liquid-water dynamics | Add explicit SCF/basis/grid and physical-sampling error categories |
| [RASPA3 source](https://github.com/iRASPA/RASPA3) and [examples](https://iraspa.github.io/RASPA3/examples_basic.html) | Concrete MC ensembles and adsorption examples | Add derivations of reservoir/proposal factors and distinguish adsorption from diffusion |
| [FEASST overview](https://pages.nist.gov/feasst/OVERVIEW.html) | Modular Monte Carlo methods and tutorial pathways | Show sampling efficiency and analytical-limit checks |
| [PLUMED tutorials](https://www.plumed.org/doc-v2.9/user-doc/html/tutorials.html) | CV/bias-focused exercises across engines | Teach estimator and overlap requirements alongside the bias |
| [MDAnalysis learning](https://www.mdanalysis.org/learning_MDAnalysis/) | Analysis concepts connected to Python workflows | Make normalization, topology, periodicity and units explicit |
| [i-PI](https://github.com/i-pi/i-pi) | Force-driver separation and advanced sampling | Explain bead/client resource costs and imaginary-time interpretation |

The added value is the connection between physical measure, numerical algorithm, resources, estimator and scope of a scientific claim. That is an editorial design inference, not a claim that the source resources omit all these topics.

## Literature verification policy

DOIs were resolved against Crossref, with titles, authors, journal, volume, issue and pages/article numbers retained where available. Publisher pages/official records were used for highlighted applications and discrepancies. A metadata record verifies identity; it does not by itself validate every statement in a paper. Application summaries are deliberately limited to claims supported by inspected abstracts/pages and do not invent performance or property values.

Foundations include Metropolis/Hastings, Verlet, thermostats/barostats, Car–Parrinello, umbrella sampling, WHAM/MBAR, metadynamics, path integrals, MLIPs and uncertainty. Textbook editions were checked at [Elsevier](https://shop.elsevier.com/books/understanding-molecular-simulation/frenkel/978-0-323-90292-2) and [Oxford](https://academic.oup.com/book/27866).

## Resolved bibliographic discrepancies

- **Gravelle et al.**: publisher and article identity give 6(1), **3037**, 2025, DOI 10.33011/livecoms.6.1.3037. Crossref's page field returned 3027; the publisher's article number is used and the discrepancy is retained in the audit.
- **Grossfield et al.**: the requested 2018 date is supported by PubMed/PMC and NIST records; Crossref/publisher issue metadata uses 2019. The entry uses 2018 with a note documenting both records, volume 1(1), article 5067. DOI identity is unchanged.
- **Stukowski**: online publication in 2009, journal issue in 2010. The conventional issue-year citation is 2010.
- **Wilmer et al.**: online in 2011, issue in 2012; use the 2012 issue citation.
- The catalysis example is Reuter, Frenkel and Scheffler, DOI **10.1103/PhysRevLett.93.116105**.
- MACE-MP is cited using the verified 2025 JCP article DOI **10.1063/5.0297006**, not an unverified guessed journal identifier.

Some official URLs return blocking/error responses to automated access despite searchable official records. [External link results](validation/external_links.json) distinguish resolved links, HTTP errors and timeouts. Such failures are not reported as successful page retrieval.

## Reuse boundary

All chapter prose, core Python algorithms, notebook activities and figures are original educational material. RASPA3 example structure/model files are the only bundled upstream scientific input assets, reused under MIT with the original notice and [file provenance](data/THIRD_PARTY_PROVENANCE.json). The teaching copy corrects the silicon display/element label; numerical interaction parameters are preserved. No private research data, licensed binaries, pretrained ML weights or external textbook diagrams are included.
