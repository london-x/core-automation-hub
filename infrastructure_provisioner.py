import pathlib
import sys


def run_provisioner() -> None:
    args = sys.argv

    if len(args) < 2:
        print("ERR: NO_ARGUMENTS")
        print("USAGE 1 (Create): python script.py [folder] [file_name] [text]")
        print("USAGE 2 (Inspect): python script.py [path_to_check]")
        sys.exit(1)

    try:
        if len(args) >= 3:
            folder = pathlib.Path(args[1])
            folder.mkdir(parents=True, exist_ok=True)

            file = folder / args[2]
            text = args[3] if len(args) > 3 else ""

            if not file.exists():
                with open(file, "w", encoding="utf-8") as f:
                    f.write(text)
                print("CREATED")
            else:
                print("EXISTS")

            print(f"SIZE_BYTES: {file.stat().st_size}")
            sys.exit(0)

        else:
            target = pathlib.Path(args[1])

            if not target.exists():
                print("ERR: NOT_FOUND")
                sys.exit(1)

            total_size = 0

            if target.is_file():
                total_size = target.stat().st_size
                print("TYPE: FILE")
            elif target.is_dir():
                for f in target.rglob("*"):
                    if f.is_file():
                        total_size += f.stat().st_size
                print("TYPE: FOLDER")

            print(f"TARGET_PATH: {target}")
            print(f"SIZE_BYTES: {total_size}")
            sys.exit(0)

    except Exception:
        print("CRITICAL")
        sys.exit(1)


if __name__ == "__main__":
    run_provisioner()
