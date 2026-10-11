# Contributing

Contributions should improve a specific explanation, calculation, test or learning activity. For scientific corrections include the disputed statement, a primary source, units/assumptions and a proposed replacement. For software issues include a minimal input, version, traceback and expected behavior without private data.

## Local checks

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/check_repository.py
python scripts/run_notebooks.py --output outputs/executed_notebooks
```

If kernels cannot start in a restricted environment, use `--mode inprocess` and state that limitation; it executes Python cells and captures figures without testing Jupyter transport. External engines require separate validation and must not be marked executed from static inspection alone.

Keep math displays in fenced `math` blocks, define symbols and units, and connect citations to claims. Update the reference audit when changing bibliography. Include source code for figures and label analytical/schematic curves. Do not add fabricated numerical outputs or unlicensed assets.

Original code contributions are offered under MIT; original prose/figures under CC BY 4.0. Third-party work needs compatible terms and attribution. By submitting, confirm that you are entitled to contribute the material under these terms.

A good pull request explains the scientific problem, the correction and the evidence used to check it. Avoid expanding validation merely to increase test count; add checks that resolve an actual failure mode.
