import sys


def main_entry() -> None:
    try:
        args = sys.argv

        if len(args) < 2:
            print("CUSTOM_CMD_ACTIVE: STATUS_OK")
            print("USAGE: mycmd [run|check] [payload]")
            sys.exit(0)

        cmd = args

        match cmd:
            case "run":
                val = args if len(args) > 2 else "EMPTY"
                print(f"EXECUTION_TRIGGERED: PAYLOAD -> {val}")
            case "check":
                print("SYSTEM_INTEGRITY: SECURE")
            case _:
                print(f"ERR: UNKNOWN_ACTION -> {cmd}")

        sys.exit(0)

    except Exception:
        print("CRITICAL_CLI_TEMPL_FAIL")
        sys.exit(1)


if __name__ == "__main__":
    main_entry()
