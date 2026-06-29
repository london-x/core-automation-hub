import json
import sys
from pathlib import Path

if __name__ == "__main__":
    target_files = ["db.json", "matrix.json", "logs.json"]
    collected_errors = []

    print("SYS: Starting batch file supervisor...")

    for file_str in target_files:
        path = Path(file_str)

        try:
            if not path.exists():
                raise IndexError(f"File {path.name} is missing from disk")

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.strip():
                raise ValueError(f"File {path.name} contains empty string")

            data = json.loads(content)

            if not isinstance(data, (dict, list)):
                raise TypeError(f"File {path.name} contains invalid data type")

            print(f"OK: File {path.name} successfully validated.")

        except (IndexError, ValueError, TypeError) as err:
            collected_errors.append(err)
        except Exception as err:
            collected_errors.append(err)

    try:
        if collected_errors:
            raise ExceptionGroup(
                "CRITICAL: Batch file validation finished with errors",
                collected_errors,
            )

    except* IndexError as eg:
        print("\n[ADMINISTRATION LOG]: Missing files detected:")
        for e in eg.exceptions:
            print(f"-> Action: Create empty file on server. Log: {e}")

    except* ValueError as eg:
        print("\n[SECURITY LOG]: Empty or corrupted files detected:")
        for e in eg.exceptions:
            print(f"-> Action: Trigger backup deployment. Log: {e}")

    except* TypeError as eg:
        print("\n[ARCHITECTURE LOG]: Structural data mismatch detected:")
        for e in eg.exceptions:
            print(f"-> Action: Reformat JSON matrix. Log: {e}")

    finally:
        print("\nSYS: Batch validation finished. All system resources cleared.")
