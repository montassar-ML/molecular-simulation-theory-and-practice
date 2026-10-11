# GitHub publication guide

This archive is prepared for review and subsequent publication. It has not been pushed to a GitHub account.

**Repository name:** `molecular-simulation-theory-and-practice`  
**Owner:** `montassar-ML`  
**Recommended description:** Graduate-level molecular simulation: statistical mechanics, MD, Monte Carlo, AIMD, sampling, analysis, uncertainty and reproducible Python exercises.

**Topics:** `molecular-dynamics`, `molecular-simulation`, `statistical-mechanics`, `monte-carlo`, `computational-chemistry`, `materials-science`, `lammps`, `cp2k`, `gcmc`, `enhanced-sampling`, `scientific-computing`, `education`.

**First commit message:** `Add molecular simulation course with theory, reproducible tutorials and validation`

## Review and publish

1. Review README, validation report and contact placeholders.
2. Create a public empty repository with the name above on your GitHub account.
3. Extract this folder and upload its contents, retaining subdirectories and dotfiles. Do not upload only the ZIP as the source tree.
4. Alternatively initialize Git locally, add the intended files, inspect the staged list, commit and push to your newly created remote.
5. Enable Actions if desired and inspect the validation job. Its standard-kernel notebook run is an additional environment check.
6. Add `repository-code` to CITATION.cff after the live repository URL exists. Optionally archive a tagged release with a DOI through an appropriate service; no DOI is invented here.

Original source figures are SVG plus their generator. The validation folder contains modest evidence of actual short runs; large trajectories, checkpoints and generated outputs are ignored for future work. Review any additional files before publishing.
