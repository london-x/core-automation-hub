import sys
import json
from pathlib import Path

"""
MAP:
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

[main 2026-06-28T15:39:37.854Z] StorageMainService: creating application shared storage
[main 2026-06-28T15:39:37.925Z] [shared storage] Creating shared storage database at 'c:\Users\Dom27\.vscode-shared\sharedStorage\state.vscdb' (wasCreated: false)
[main 2026-06-28T15:39:37.925Z] [shared storage] Initializing fallback application storage (path: c:\Users\Dom27\AppData\Roaming\Code\User\globalStorage\state.vscdb)
[main 2026-06-28T15:39:37.941Z] [shared storage] Fallback application storage initialized with 103 items
[main 2026-06-28T15:39:37.945Z] update#setState idle
[main 2026-06-28T15:39:38.754Z] vscode-file: Refused to load resource d:\Microsoft VS Code\93cfdd489c\resources\app\extensions\theme-seti\icons\seti.woff from vscode-file: protocol (original URL: vscode-file://vscode-app/d:/Microsoft%20VS%20Code/93cfdd489c/resources/app/extensions/theme-seti/icons/seti.woff)
(node:12460) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `Code --trace-deprecation ...` to show where the warning was created)
[main 2026-06-28T15:40:07.374Z] Extension host with pid 13768 exited with code: 0, signal: unknown.
