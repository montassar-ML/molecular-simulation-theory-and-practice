"""Offline checks for this repository; optional external HTTP reachability audit.

This checks the Markdown constructs used here, not arbitrary CommonMark or a
live GitHub renderer. Scientific validity is assessed separately by the tests
and EQUATION_REVIEW.md. Run from any directory.
"""
import argparse
import ast
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def prose(text):
    return re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)


def links(text):
    """Read inline destinations, retaining parentheses inside DOI URLs."""
    for match in re.finditer(r"\]\(", text):
        start = match.end()
        depth = 1
        end = start
        while end < len(text) and depth:
            if text[end] == "(": depth += 1
            if text[end] == ")": depth -= 1
            end += 1
        if depth == 0:
            yield text[start:end-1].strip().strip("<>")


def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    used = Counter()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.M):
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        suffix = "" if used[slug] == 0 else f"-{used[slug]}"
        used[slug] += 1
        result.add(slug + suffix)
    return result


def math_items(text, source):
    for i, item in enumerate(re.finditer(r"^```math\s*\n(.*?)^```\s*$", text, re.M | re.S)):
        yield {"source": source, "kind": "display", "index": i, "tex": item.group(1).strip()}
    clean = re.sub(r"`[^`\n]+`", "", prose(text))
    for i, item in enumerate(re.finditer(r"(?<![\\$])\$(?!\$)(.+?)(?<!\\)\$(?!\$)", clean, re.S)):
        yield {"source": source, "kind": "inline", "index": i, "tex": item.group(1)}


def reachable(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MolecularSimulationCourse-LinkAudit/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return {"url": url, "status": response.status, "final_url": response.url}
    except urllib.error.HTTPError as exc:
        return {"url": url, "status": exc.code, "note": "HTTP response; access restrictions can prevent verification"}
    except Exception as exc:
        return {"url": url, "status": "unverified", "note": type(exc).__name__}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--external", action="store_true", help="Check non-DOI external links; DOI metadata already has a separate audit")
    parser.add_argument("--export-math", type=Path, help="Export TeX snippets for an optional KaTeX parser")
    args = parser.parse_args()
    errors, equations, external = [], [], set()
    counts = Counter()
    markdown = sorted(ROOT.rglob("*.md"))
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        counts["markdown_files"] += 1
        if "\\[" in text or "\\]" in text:
            errors.append(f"{rel}: legacy display delimiter")
        if len(re.findall(r"^```", text, re.M)) % 2:
            errors.append(f"{rel}: unbalanced code fences")
        for item in math_items(text, rel):
            equations.append(item)
            counts[item["kind"] + "_equations"] += 1
            stripped = re.sub(r"\\[{}]", "", item["tex"])
            depth = 0
            for char in stripped:
                depth += (char == "{") - (char == "}")
                if depth < 0: break
            if depth:
                errors.append(f"{rel}: unbalanced math braces: {item['index']}")
        for target in links(prose(text)):
            parsed = urllib.parse.urlsplit(target)
            if parsed.scheme in {"https", "http"}:
                external.add(target)
                continue
            if parsed.scheme:
                continue
            dest = (path.parent / urllib.parse.unquote(parsed.path)).resolve() if parsed.path else path
            counts["internal_links"] += 1
            if not dest.exists():
                errors.append(f"{rel}: missing target {target}")
            elif parsed.fragment and dest.suffix == ".md":
                if urllib.parse.unquote(parsed.fragment) not in anchors(dest.read_text()):
                    errors.append(f"{rel}: missing anchor {target}")
    for path in sorted(ROOT.rglob("*.py")):
        try:
            ast.parse(path.read_text(), filename=str(path))
            counts["python_files"] += 1
        except SyntaxError as exc:
            errors.append(str(exc))
    import nbformat
    for path in sorted((ROOT / "notebooks").glob("*.ipynb")):
        nb = nbformat.read(path, as_version=4)
        nbformat.validate(nb)
        counts["notebooks"] += 1
        for cell in nb.cells:
            if cell.cell_type == "code": ast.parse(cell.source)
            elif cell.cell_type == "markdown":
                equations.extend(math_items(cell.source, str(path.relative_to(ROOT))))
        if any(o.output_type == "error" for c in nb.cells if c.cell_type == "code" for o in c.outputs):
            errors.append(f"{path.name}: error output retained")
    bib = (ROOT / "references.bib").read_text()
    keys = re.findall(r"@\w+\s*\{\s*([^,]+),", bib)
    audit = json.loads((ROOT / "data/reference_audit.json").read_text())
    if len(keys) != len(set(keys)): errors.append("Duplicate BibTeX keys")
    if set(keys) != {x["key"] for x in audit}: errors.append("BibTeX and metadata audit keys differ")
    ref_anchors = anchors((ROOT / "references.md").read_text())
    if not set(keys) <= ref_anchors: errors.append("Missing reference anchors")
    dois = [x["doi"].lower() for x in audit if x.get("doi")]
    if len(dois) != len(set(dois)): errors.append("Duplicate reference DOI")
    counts["references"] = len(keys)
    counts["doi_records"] = len(dois)
    for item in json.loads((ROOT / "data/THIRD_PARTY_PROVENANCE.json").read_text()):
        actual = hashlib.sha256((ROOT/item["path"]).read_bytes()).hexdigest()
        if actual != item.get("teaching_sha256", item["sha256"]):
            errors.append(f"Provenance hash mismatch: {item['path']}")
    for path in (ROOT / "tutorials/05_aimd_water").glob("*.inp"):
        stack = []
        for line in path.read_text().splitlines():
            line = line.split("#", 1)[0].strip().upper()
            if line.startswith("&END"):
                end = line.split()[1:]
                if not stack or (end and end[0] != stack[-1]):
                    errors.append(f"CP2K section mismatch in {path.name}")
                else: stack.pop()
            elif line.startswith("&"): stack.append(line.split()[0][1:])
        if stack: errors.append(f"CP2K unclosed sections: {path.name}")
    for path in (ROOT / "tutorials/04_gcmc_adsorption/raspa3").glob("*.json"):
        json.loads(path.read_text())
    if args.export_math:
        args.export_math.write_text(json.dumps(equations, indent=2))
    report = {"scope": "offline syntax, local links, metadata consistency and static inputs; not scientific convergence or engine execution", "counts": dict(counts), "errors": errors}
    (ROOT / "validation").mkdir(exist_ok=True)
    (ROOT / "validation/repository_checks.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
    if args.external:
        urls = sorted(u for u in external if urllib.parse.urlsplit(u).netloc not in {"doi.org", "dx.doi.org"})
        with ThreadPoolExecutor(max_workers=6) as pool: results = list(pool.map(reachable, urls))
        (ROOT / "validation/external_links.json").write_text(json.dumps({"date": "2026-10-11", "scope": "non-DOI Markdown links; DOI identities checked through reference_audit.json", "results": results}, indent=2)+"\n")
        print("External HTTP results:", dict(Counter(str(x["status"]) for x in results)))
    raise SystemExit(bool(errors))


if __name__ == "__main__": main()
