"""Extract a final complete XYZ frame; does not verify optimization convergence."""
import argparse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("input",type=Path);p.add_argument("output",type=Path);a=p.parse_args()
lines=a.input.read_text().splitlines();i=0;last=None
while i<len(lines):
    if not lines[i].strip():i+=1;continue
    n=int(lines[i]);frame=lines[i:i+n+2]
    if len(frame)!=n+2:raise ValueError("Incomplete final XYZ frame.")
    for row in frame[2:]:
        fields=row.split()
        if len(fields)<4:raise ValueError("Malformed XYZ row.")
        [float(v) for v in fields[1:4]]
    last=frame;i+=n+2
if last is None:raise ValueError("No XYZ frame.")
if a.output.exists():raise FileExistsError("Choose a new output path.")
a.output.write_text("\n".join(last)+"\n")
print("Extracted coordinates only; inspect optimizer log for convergence.")
