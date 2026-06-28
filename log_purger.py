import json
import pathlib
import sys


def r():
    """
    a = [sys.argv] Input terminal command line arguments.
    p = [path] Target file path object on SSD.
    f = [file] Internal file stream for disk access.
    l = [list] Stored database array inside RAM.
    n = [num] General atomic memory counter for cells.
    """
    a = sys.argv
    if len(a) < 2:
        print("ERR: NO_FILE")
        sys.exit(1)
    p = pathlib.Path(a)
    print(p)
    if not p.exists():
        print("ERR: NOT_FOUND")
        sys.exit(1)
    try:
        with open(p, "r", encoding="utf-8") as f:
            l = json.load(f)
        if not isinstance(l, list):
            raise TypeError
        n = len(l)
        print(n)
        with open(p, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        print("SUCCESS")
        sys.exit(0)
    except (json.JSONDecodeError, TypeError, Exception):
        print("CRITICAL")
        with open(p, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        sys.exit(0)


if __name__ == "__main__":
    r()
