import json
import sys
from pathlib import Path

if __name__ == "__main__":
    src_path = Path("bank_report.json")
    ok_path = Path("success_log.json")
    err_path = Path("errors_log.json")

    ok_pool = []
    err_pool = []

    print("SYS: Starting Core...")

    try:
        if not src_path.exists():
            raise IndexError("Source file missing")

        with open(src_path, "r", encoding="utf-8") as f:
            raw_data = f.read()

        if not raw_data.strip():
            raise ValueError("Source data empty")

        txs = json.loads(raw_data)

        if not isinstance(txs, list):
            raise TypeError("Invalid data matrix type")

        for tx in txs:
            try:
                match tx:
                    case {"status": "SUCCESS", "tx_id": int(tid), "amount": float(amt)} if amt > 0:
                        assert tid > 0, f"Malformed tx_id: {tid}"
                        print(f"OK: TX {tid} approved with amount: {amt}")
                        ok_pool.append(tx)

                    case {"status": "FAILED", "tx_id": _, "amount": _}:
                        raise ValueError(f"Bank dropped transaction state: {tx}")

                    case _:
                        raise TypeError(f"Security hazard caught: {tx}")

            except (ValueError, TypeError, AssertionError) as tx_err:
                print(f"WARN: Micro-tx aborted: {tx_err}")
                err_pool.append({
                    "raw": tx,
                    "type": type(tx_err).__name__,
                    "msg": str(tx_err)
                })

    except Exception as glob_err:
        print(f"\nCRITICAL: Core panic: {glob_err}")
        print(">>> USER_MSG: System temporarily locked. Retry later. <<<")
        sys.exit(1)

    finally:
        try:
            with open(ok_path, "w", encoding="utf-8") as f:
                json.dump(ok_pool, f, ensure_ascii=False, indent=4)
                
            with open(err_path, "w", encoding="utf-8") as f:
                json.dump(err_pool, f, ensure_ascii=False, indent=4)
                
            print("\nSYS: All registry logs flushed successfully.")
        except Exception as log_err:
            print(f"CRITICAL: Disk write failure: {log_err}")

        print("SYS: Core session closed.")
