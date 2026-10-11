# 21. Research applications and literature map

**Level:** intermediate → research. The summaries below distinguish a verified paper's scope from a proposed educational exercise. They do not reproduce published numerical datasets. Computational-demand statements identify cost drivers, not fabricated hardware timings.

## Foundation, review and application mapping

| Method / application | Foundational primary paper | Review or synthesis | Representative application and DOI | What it supports |
|---|---|---|---|---|
| Classical MD / LJ liquid | Verlet 1967 | Allen–Tildesley textbook | [Rahman 1964](../references.md#rahman1964), 10.1103/PhysRev.136.A405 | Atomic velocity correlations in a simple liquid |
| Classical liquid-water models | Jorgensen 1983 | [Vega–Abascal 2011](../references.md#vega2011) | [Jorgensen 1983](../references.md#jorgensen1983), 10.1063/1.445869 | Model-dependent water structure/thermodynamics |
| MC / fluids and phase equilibria | Metropolis 1953; Hastings 1970 | Frenkel–Smit textbook | [Martin–Siepmann 1998](../references.md#martin1998), 10.1021/jp972543+ | Transferable united-atom alkane model and phase-equilibrium targets |
| Classical MD / metals | [Daw–Baskes 1984](../references.md#daw1984) | [Deringer 2019](../references.md#deringer2019), broader model comparison | Daw–Baskes, 10.1103/PhysRevB.29.6443 | Metallic many-body energetics; does not validate this course's EMT calculation |
| Coarse-grained / polymers | [Kremer–Grest 1990](../references.md#kremer1990) | Allen–Tildesley textbook | Kremer–Grest, 10.1063/1.458541 | Entangled versus shorter-chain dynamics in a bead-spring melt |
| Coarse-grained / biomolecular organization | [Marrink 2007](../references.md#marrink2007) | [Martini 3](../references.md#souza2021), model synthesis/validation | Souza 2021, 10.1038/s41592-021-01098-3 | A defined coarse-grained force-field scope |
| GCMC / MOF adsorption screening | Metropolis; grand-canonical theory | [Han 2009](../references.md#han2009) | [Wilmer 2012](../references.md#wilmer2012), 10.1038/nchem.1192 | Computational screening of hypothetical MOFs |
| GCMC / COF gas storage | Grand-canonical theory | Han 2009 | [Han 2008](../references.md#han2008), 10.1021/ja803247y | Predicted hydrogen adsorption in specified COFs |
| MD / porous gas-mixture diffusion | Newtonian MD, Einstein relation | Frenkel–Smit textbook; [RASPA synthesis](../references.md#dubbeldam2015) | [Snurr–Kärger 1997](../references.md#snurr1997), 10.1021/jp970242u | Binary self-diffusion in silicalite and comparison with NMR |
| Electrolyte transport | Green–Kubo | Allen–Tildesley textbook | [France-Lanord–Grossman 2019](../references.md#france2019), 10.1103/PhysRevLett.122.136001 | Ion-pair correlations and limits of simple Nernst–Einstein estimates |
| AIMD / liquid water | Car–Parrinello 1985 | [Gillan et al. 2016](../references.md#michaelides2016) | [Laasonen et al. 1993](../references.md#laasonen1993), 10.1063/1.465574 | Electronic-structure treatment of liquid water |
| AIMD / oxide–water interfaces | BO forces / electronic structure | CP2K review; DFT-water perspective | [Oxide-water study 2019](../references.md#oxide2019), 10.1021/acsomega.8b03350 | Surface/coverage-dependent adsorption and dissociation |
| Metal surfaces / complementary DFT | Electronic-structure energetics | CP2K review (method context) | [Michaelides et al. 2003](../references.md#michaelides2003), 10.1103/PhysRevLett.90.216102 | Static water-monomer adsorption; explicitly not a transport/AIMD trajectory study |
| Reactive MD / hydrocarbon chemistry | [van Duin 2001](../references.md#van_duin2001) | [Senftle 2016](../references.md#senftle2016) | van Duin, 10.1021/jp004368u | A fitted reactive hydrocarbon force-field domain |
| KMC / oxide catalysis | Bortz 1975; Gillespie 1977 | [Reuter–Scheffler 2006](../references.md#reuter2006), detailed methodological study | [Reuter et al. 2004](../references.md#reuter2004), 10.1103/PhysRevLett.93.116105 | Rate-based steady-state heterogeneous catalysis |
| Enhanced sampling / rare configurations | Torrie–Valleau 1977 | [Roux 1995](../references.md#roux1995) | [Laio–Parrinello 2002](../references.md#laio2002), 10.1073/pnas.202427399 | History-dependent exploration of solvated/conformational free energies |
| PIMD / nuclear quantum effects | [Ceperley 1995](../references.md#ceperley1995), foundational review | [Markland–Ceriotti 2018](../references.md#markland2018) | [Cheng 2019](../references.md#cheng2019), 10.1073/pnas.1815117116 | Quantum-nuclear contributions to water/ice thermodynamics |
| MLIP-MD / water and solids | Behler–Parrinello 2007 | Deringer 2019; [Yuan et al. 2026](../references.md#foundation2026) | [CHGNet 2023](../references.md#chen2023), 10.1038/s42256-023-00716-3; [MACE-MP 2025](../references.md#batatia2025), 10.1063/5.0297006 | Learned atomistic models and domain-specific demonstrations |

Where a textbook or methodological study fills the synthesis column, it is labeled as such rather than falsely called a review article. Full metadata are in [references](../references.md).

## Liquids, mixtures and gases

**Question:** how do interactions set local structure and mobility? Classical MD provides a time-resolved trajectory under the chosen potential; equilibrium MC offers configurational sampling without physical time. Rahman's work studied liquid argon correlations, not every gas or liquid. Martin–Siepmann's united-atom alkane work targeted phase equilibria. Their findings demonstrate the role of force-field design and molecular representation.

**Educational application:** compare LJ MD and MC at the same Hamiltonian/state, then consider a binary-mixture parameter audit. Analyze RDFs, density/energy distributions and, only for valid dynamics, MSD/VACF. Gas diffusion needs collision statistics and suitable cell/time scales; a dilute gas may demand longer trajectories despite cheap force evaluations.

**Demands and limits:** many classical force evaluations are affordable relative to DFT but finite size, cross interactions, phase equilibration and long-time correlations remain. Complement equilibrium MC with MD transport; neither replaces parameter validation.

## Solids and polymers

**Question:** which degrees of freedom control structural stability and relaxation? Daw–Baskes established a many-body metallic energy framework applied to defects/surfaces; the course's copper EMT exercise is a separate model with separate evidence needs. Kremer–Grest examined chain-length-dependent dynamics in a bead-spring melt.

**Educational application:** compare lattice displacement/RDF in a solid with chain size, segment MSD and end-to-end relaxation in a polymer design exercise. Classical MD is appropriate when the potential represents the bonding and relevant dynamics.

**Demands and limits:** defect migration and polymer disentanglement can require far longer sampling than thermal vibrations. Coarse graining reduces coordinates but loses atomistic detail and friction. An observed plateau can reflect confinement, entanglement or insufficient time. Complement with free-energy barriers, larger cells and independent reference material properties.

## Water and electrolyte solutions

**Question:** how does the molecular model change hydrogen bonding and transport? Jorgensen et al. compared several water potentials; Vega–Abascal review broader model performance. France-Lanord–Grossman address ion correlations in conductivity approximations. These sources support model sensitivity and correlation-aware analysis, not universal rankings under all conditions.

**Educational application:** [Case C](../tutorials/03_water_electrolyte/README.md) analyzes geometry-defined hydrogen bonds, ion coordination and water COM displacement. Fixed-charge rigid water is a deliberate approximation; it cannot describe proton transfer. Use collective charge-current correlations for conductivity when distinct-ion contributions matter.

**Demands and limits:** electrostatics and constraints affect compute cost; slow ion association affects independent sampling. Check finite-size transport and force-field compatibility. Complement classical MD with electronic-structure checks or polarizable/reactive models when the physical question requires them.

## Porous materials: uptake versus transport

**Question:** how much adsorbs, and how fast does it move? Wilmer's study screened hypothetical MOFs; Han's study predicted hydrogen storage in specified COFs. These are adsorption applications. Snurr–Kärger compared MD binary self-diffusion in silicalite with NMR, a distinct transport problem.

**Educational application:** use GCMC methane/MFI to obtain equilibrium occupancy and adsorption-site distributions. Then prepare physical MD at selected loadings to study guest displacements. Framework rigidity, LJ/charge parameters, gas fugacity and defects are model choices. Hydrogen may require nuclear-quantum/effective-potential corrections depending on conditions.

**Demands and limits:** pressure points and seeds parallelize, but dense insertion and narrow-pore transport are difficult. A rigid accessible cavity can fill through GCMC insertion even when physical entry is kinetically blocked. Neither uptake nor an MC movie alone proves membrane flux or separation rate. Complement adsorption with transport and experimentally relevant host activation states.

## Interfaces, surfaces and chemistry

**Question:** how do surface structure and neighboring water affect adsorption and dissociation? The 2019 oxide study combines static calculations and AIMD for Ti/Ru/Ir oxide surfaces at specified coverages. It reports an interplay of intrinsic interactions and cooperative effects. The Michaelides metal-surface paper concerns static monomer adsorption and is included as a complementary energetic reference, not an MD transport study.

**Educational application:** [Case E](../tutorials/05_aimd_water/README.md) teaches electronic-force controls before attempting an interface. A research extension would vary slab thickness, coverage, surface termination and functional, then analyze coordination, persistent dissociation and density/orientation profiles.

**Demands and limits:** electronic solves, slab cells and rare proton events make sampling expensive. A few observed bond changes do not establish a rate. Reactive MD may extend sampling only after chemistry-specific validation; ReaxFF hydrocarbon parameters do not justify oxide chemistry. Complement with reaction-path/free-energy calculations and independent electronic references.

## Rate-based catalysis

**Question:** how do competing elementary events determine steady-state activity? Reuter et al. combine first-principles information and statistical mechanics for heterogeneous catalysis. KMC is selected because rates between metastable states, rather than every bond vibration, determine the long-time process.

**Educational application:** solve and simulate the two-state model in [Notebook 4](../notebooks/04_mc_gcmc_kmc.ipynb), then design a surface event catalogue. Record time-weighted coverages, event counts and turnover with uncertainty.

**Demands and limits:** DFT rate generation can dominate cost. Missing channels, environment-dependent barriers and failed Markov separation change predictions. An exact KMC algorithm only solves its supplied stochastic model. Complement it with barrier validation and sensitivity analysis.

## Free energies, quantum nuclei and learned potentials

**Question:** can methods overcome insufficient sampling while preserving an interpretable statistical target? Laio–Parrinello demonstrate biased exploration; Cheng et al. combine learned potentials, free-energy methods and quantum nuclear treatment for water/ice thermodynamics. These findings are specific to their models and validation.

**Educational application:** [Case F](../tutorials/06_free_energy/README.md) validates WHAM on a known toy distribution; [Notebook 6](../notebooks/06_resources_and_quantum.ipynb) contrasts quantum/classical oscillator variance. The [MLIP audit](../tutorials/07_mlip_md/README.md) asks whether a learned model covers a chosen deployment domain.

**Demands and limits:** windows, beads and reference calculations multiply work. Biasing does not guarantee hidden-coordinate sampling. PIMD bead motion is not real-time quantum motion. A general-purpose pretrained potential still needs chemical/environment validation. Complement sampling acceleration with reference corrections, independent tests and explicit uncertainty.

## Research-design exercise

Choose one application and submit a one-page protocol with: question; target ensemble; model; algorithm; observable/equation; numerical convergence; sampling evidence; independent model validation; resource pilot; interpretation boundary; foundation/review/application citations. Do not substitute an attractive trajectory image for any of these evidence categories.
