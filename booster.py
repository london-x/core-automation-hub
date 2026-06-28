import sys
import json
from pathlib import Path

"""
a = arguments
p = path
f = file
d = data
c = copy
x = copy_file
m = matrix
"""

a = sys.argv
if len(a) < 2:
    print("ERR: No file")
    sys.exit(1)

p = Path(a[1])
if not p.exists():
    print(f"ERR: {p} not found")
    sys.exit(1)

with open(p, "r", encoding="utf-8") as f:
    d = f.read()

c = p.with_suffix(p.suffix + ".copy")
with open(c, "w", encoding="utf-8") as x:
    x.write(d)

m = json.loads(d)

print(f"OK: {p.name}")
print(f"CP: {c.name}")
print(m)
