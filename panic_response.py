import sys
import json
from pathlib import Path
from typing import NoReturn, Union

def panic(msg: str) -> NoReturn:
    print(f"CRITICAL: {msg}")
    sys.exit(1) 

def supervisor(path: Path) -> Union[dict, list]:
    if not path.exists():
        panic(f"File {path.name} missing") 

    data = ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
    except (OSError, IOError) as err:
        panic(f"IO block fail: {err}") 

    try:
        bak = path.with_suffix(path.suffix + ".copy")
        with open(bak, "w", encoding="utf-8") as f:
            f.write(data)
    except Exception as err:
        print(f"WARN: Snapshot write dropped: {err}") 

    try:
        if not data.strip():
            raise ValueError("Empty data string") 

        res = json.loads(data) 

        if not isinstance(res, (dict, list)):
            raise TypeError("Matrix must parse strictly as dict or list object") 

        return res 

    except ValueError as err:
        print(f"RECOVERY [ValueError]: Payload data corruption. Log: {err}")
        return {"status": "fallback", "neurons": 0} 

    except TypeError as err:
        print(f"RECOVERY [TypeError]: Runtime memory block type collision! Log: {err}")
        return {} 

    except Exception as err:
        print(f"RECOVERY [Exception]: Unidentified runtime hazard caught: {err}")
        return {} 

    finally:
        print(f"SYS: Memory bus cleared for target: {path.name}") 

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        panic("Launcher usage pattern: python script.py <target.json>") 

    target_path = Path(args[1])
    active_matrix = supervisor(target_path)
    print(f"\nMatrix system deployment successful: {active_matrix}")
