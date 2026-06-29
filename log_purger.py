import json
import pathlib
import sys


def r():
    args = sys.argv
    if len(args) < 2:
        print("ERR: NO_FILE")
        sys.exit(1)
    path = pathlib.Path(args)
    print(path)
    if not path.exists():
        print("ERR: NOT_FOUND")
        sys.exit(1)
    try:
        with open(path, "r", encoding="utf-8") as file:
            list = json.load(file)
        if not isinstance(list, list):
            raise TypeError
        num = len(list)
        print(num)
        with open(path, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        print("SUCCESS")
        sys.exit(0)
    except (json.JSONDecodeError, TypeError, Exception):
        print("CRITICAL")
        with open(path, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        sys.exit(0)


if __name__ == "__main__":
    r()
