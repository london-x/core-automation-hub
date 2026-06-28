import sys
import json
from pathlib import Path
from typing import NoReturn

"""
a = arguments (sys.argv)
p = path object (Path)
d = raw text data from file
c = backup copy path
x = active file stream
m = loaded RAM matrix dict
v = ValueError sensor
T = TypeError sensor
E = base Exception catch
"""

def panic(msg: str) -> NoReturn:
    print(f"CRITICAL: {msg}")
    sys.exit(1)

def supervisor(p: Path) -> dict:
    if not p.exists():
        panic(f"File {p.name} missing")

    try:
        with open(p, "r", encoding="utf-8") as x:
            d = x.read()
    except (OSError, IOError) as error:
        panic(f"IO block fail: {error}")

    try:
        c = p.with_suffix(p.suffix + ".copy")
        with open(c, "w", encoding="utf-8") as x:
            x.write(d)
    except Exception as E:
        print(f"WARN: Snapshot write dropped: {E}")

    try:
        if not d.strip():
            raise ValueError("Empty data string")
            
        m = json.loads(d)
        
        if not isinstance(m, dict):
            raise TypeError("Matrix must parse strictly as dict object")
            
        return m

    except ValueError as v:
        print(f"RECOVERY [ValueError]: Payload data corruption. Log: {v}")
        return {"status": "fallback", "neurons": 0}

    except TypeError as T:
        print(f"RECOVERY [TypeError]: Runtime memory block type collision! Log: {T}")
        return {}

    except Exception as E:
        print(f"RECOVERY [Exception]: Unidentified runtime hazard caught: {E}")
        return {}

    finally:
        print(f"SYS: Memory bus cleared for target: {p.name}")

if __name__ == "__main__":
    a = sys.argv
    if len(a) < 2:
        panic("Launcher usage pattern: python script.py <target.json>")

    target_path = Path(a[1])
    active_matrix = supervisor(target_path)
    print(f"\nMatrix system deployment successful: {active_matrix}")
