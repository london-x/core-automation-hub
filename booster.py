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

with open(path, "r", encoding="utf-8") as file:
    data = file.read()

copy = path.with_suffix(path.suffix + ".copy")
with open(copy, "w", encoding="utf-8") as copy_file:
    copy_file.write(data)

matrix = json.loads(data)

print(f"OK: {path.name}")
print(f"CP: {copy.name}")
print(matrix)
