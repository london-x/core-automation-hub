import sys
import json
from pathlib import Path

args = sys.argv
if len(args) < 2:
    print("ERR: No file")
    sys.exit(1)

path = Path(args[1])
if not path.exists():
    print(f"ERR: {path} not found")
    sys.exit(1)

with open(path, "r", encoding="utf-8") as f_in:
    data = f_in.read()

copy_path = path.with_suffix(path.suffix + ".copy")
with open(copy_path, "w", encoding="utf-8") as f_out:
    f_out.write(data)

matrix = json.loads(data)

print(f"OK: {path.name}")
print(f"CP: {copy_path.name}")
print(matrix)
