import io
import pathlib
import sys
import tempfile
import time


def run_accelerator() -> None:
    try:
        saved = pathlib.Path("core/production_data")
        saved.mkdir(parents=True, exist_ok=True)

        buf = io.BytesIO()
        start = time.time()
        tick_count = 0

        print("HIGH-SPEED RING TIMER WITH MEMORYVIEW ACTIVATED...")

        while True:
            tick_count += 1
            data = f"PRICE_UPDATE_TICK_{tick_count}_DATA_777_0.85\n".encode("utf-8")
            buf.write(data)

            now = time.time()

            if now - start >= 60.0:
                print("\n[TRIGGER] 60 SECONDS PASSED. PACKET ANALYSIS VIA RAM...")

                buf.seek(0)
                payload = buf.read()

                view = memoryview(payload)

                with tempfile.NamedTemporaryFile(
                    delete=False, dir="core", suffix=".tmp"
                ) as temp:
                    temp.write(view)
                    temp_path = pathlib.Path(temp.name)

                print(f"TEMP CONVEYER DEPLOYED: {temp_path.name}")

                if b"DATA_777" in view:
                    prod_file = saved / f"excel_ready_{int(now)}.log"
                    with open(prod_file, "wb") as f:
                        f.write(view)
                    print(f"PRODUCTION OUTFLOW SECURED: {prod_file.name}")

                view.release()

                if temp_path.exists():
                    temp_path.unlink()
                    print("TEMP GARBAGE PURGED SUCCESSFULLY")

                buf.seek(0)
                buf.truncate(0)

                start = now
                print("RESETTING TIMER. NEW 60 SECONDS INTERVAL STARTED!\n")

            time.sleep(1)

    except Exception:
        print("CRITICAL_CORE_ERR")
        sys.exit(1)


if __name__ == "__main__":
    run_accelerator()
