import json
import pathlib
import sys


def r():
    args = sys.argv
    if len(args) < 2:
        print("ERR: NO_FILE")
        sys.exit(1)
    path = pathlib.Path(args[1])
    print(f"Target path: {path}")
    if not path.exists():
        print("ERR: NOT_FOUND")
        sys.exit(1)
    try:
        with open(path, "r", encoding="utf-8") as file:
            content_list = json.load(file)
        if not isinstance(content_list, list):
            raise TypeError
        num = len(content_list)
        print(f"Elements found: {num}")
        with open(path, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        print("SUCCESS")
        sys.exit(0)
    except (json.JSONDecodeError, TypeError, Exception) as err:
        print(f"CRITICAL: Wipe triggered due to error ({type(err).__name__})")
        with open(path, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        sys.exit(0)


if __name__ == "__main__":
    r()
