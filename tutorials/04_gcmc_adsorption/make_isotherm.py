"""Create independent pressure directories without overwriting existing runs."""
from pathlib import Path
import json,shutil
base=Path(__file__).resolve().parent/"raspa3"
out=Path("outputs/mfi_isotherm")
for pressure in [1000,10000,100000]:
    for replica in range(3):
        target=out/f"P{pressure}_rep{replica}"
        target.mkdir(parents=True,exist_ok=False)
        for name in ["MFI_SI.cif","methane.json","force_field.json"]:
            shutil.copy2(base/name,target/name)
        config=json.loads((base/"simulation.json").read_text())
        config["Systems"][0]["ExternalPressure"]=pressure
        config["RandomSeed"]=2026+replica
        (target/"simulation.json").write_text(json.dumps(config,indent=2)+"\n")
        print(target)
