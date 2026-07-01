import contextlib
import functools
import io
import json
import sys
import tempfile


@contextlib.contextmanager
def operational_io_latch(stream: io.BytesIO):
    try:
        yield stream
    finally:
        stream.seek(0)
        stream.truncate(0)
        print("LATCH_TRIGGERED: RAM_STREAM_TOTALLY_PURGED")


@functools.cache
def process_matrix_payload(raw_bytes: bytes) -> str:
    parsed_json = json.loads(raw_bytes.decode("utf-8"))
    return f"STATUS_VALIDATED_{parsed_json.get('id', 'RAW')}"


def run_transit_system() -> None:
    try:
        print("INITIALIZING SUPERSCALAR TRANSIT TRANSLATOR...")

        buf = io.BytesIO()

        with operational_io_latch(buf) as ram_pipe:
            with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", delete=False) as temp:
                json.dump({"id": 777, "node": "alpha_cortex"}, temp)
                temp_path = temp.name

            with open(temp_path, "r", encoding="utf-8") as f:
                raw_txt = f.read()

            ram_pipe.write(raw_txt.encode("utf-8"))
            
            view = memoryview(ram_pipe.getvalue())

            with contextlib.suppress(TypeError, ValueError):
                res1 = process_matrix_payload(bytes(view))
                print(f"TACT_1 (CLEAN CPU CALCULATION): {res1}")

                res2 = process_matrix_payload(bytes(view))
                print(f"TACT_2 (INFINITE RAM CACHE FASTBACK): {res2}")

            view.release()

        sys.exit(0)

    except Exception:
        print("FATAL_INFRASTRUCTURE_FAILURE")
        sys.exit(1)


if __name__ == "__main__":
    run_transit_system()
