# core-automation-hub
All-in-One high-load CLI automation platform and server combiner. Includes a persistent JSON database core with strict data pruning, system metrics analyzer, infrastructure error scanner, autonomous e-commerce market price parser, and a universal Excel pipeline translator.

This repository is still under development and will be updated.

# USER MANUAL: PERSISTENT SnapDBMS CONTROLLER (main.py)

High-performance console controller and database snapshot manager written in pure Python 3 with zero external dependencies. Optimized for minimal RAM footprint using an atomic 21-letter variable layout in active memory. Data is permanently written inside a local JSON snapshot storage db.json on the SSD.

The platform includes an integrated high-precision hardware profiler (time.perf_counter) that automatically benchmarks execution speed and outputs the exact processing delta in milliseconds (v ms) upon termination of ANY command.

---

## MODE 1: PAYLOAD APPEND & INJECTION (-add)

Ingests and records string tokens, integer values, or fractional metrics directly into the database array.

* Global array append to the end of storage:
  ```bash
  python main.py -add token1 token2 99.4 4.22
  ```
* Surgical array insertion inside a custom slice window (range):
  Splits the storage array in RAM and injects a new token sequence strictly at the requested 1-based human index position, automatically shifting existing downstream entries to the right:
  ```bash
  python main.py -add range 3 new_cell_1 new_cell_2
  ```
* Input perimeter validation: Blank parameters or empty strings wrapped in quotes (python main.py -add "   ") are caught by the list comprehension generator. The payload calculation fires a strict raise IndexError fuse, aborting empty array writes to the SSD and routing execution to the rollback routine.

---

## MODE 2: BATCH INTELLECTUAL LOOKUP RADAR (-search)

Performs high-speed parallel sequence scanning within RAM under a non-mutating isolated route without modifying the source JSON file on disk.

* Global parallel lookup (Simultaneous index query and string scan):
  ```bash
  python main.py -search query_word 3 target_token
  ```
  * Pure integer parameters (e.g., 3) are automatically evaluated as absolute index lookups. The system shifts the coordinate back by one element (l[h - 1]) and extracts the string stored at that precise slot.
  * Character-based words fail integer parsing, get intercepted by a ValueError trap, and are rerouted into an optimized enumerate scanner. It maps the exact 1-based line coordinates of all matching duplicates along with the absolute occurrence calculation (TOTAL_COUNT).
* Numeric string escaping (The 'w' word prefix marker):
  To scan for a sequence comprised entirely of numbers (such as an object ID, hash, or zip code like 495) as a literal text word instead of an index location, prepend the character marker w. The algorithm strips the prefix and passes the digits directly to the duplicate sequence scanner, bypassing index boundaries:
  ```bash
  python main.py -search w495
  ```
* Bounded scanning inside a specific index slice window (range):
  Narrows the scanner beam. Evaluates query tokens strictly within the requested boundary limits (e.g., from row 1 to 10), completely ignoring any database entries outside this active memory frame:
  ```bash
  python main.py -search range 1 10 query_word w495
  ```

---

## MODE 3: STRUCTURAL PRUNING & DEDUPLICATION (-del)

Provides complete structural control over storage size limitations on the SSD, allowing for pinpoint or mass cell erasures.

* Wipe entire database storage array to absolute zero:
  ```bash
  python main.py -del all
  ```
* Remove a specific cell via its 1-based human index number (e.g., row №2):
  ```bash
  python main.py -del cell 2
  ```
* Mass purge of all duplicate entries matching a word pattern:
  Deploys a list comprehension filter utilizing the != inequality operator, completely cutting out the target word from the database array:
  ```bash
  python main.py -del word query_word
  ```
* Eradicate a slice window out of the middle of the storage array (range):
  Stitches together the immutable parts of the storage array before and after the targeted boundaries (l[:x] + l[y:]), dropping the middle slice out of memory:
  ```bash
  python main.py -del range 5 8
  ```
* Automated Database Deduplication Engine (dups):
  Deploys a high-speed dict.fromkeys(l) memory pipeline that instantly purges all existing duplicates from the database while strictly preserving the initial historical timeline order of the unique records:
  ```bash
  python main.py -del dups
  ```

---

## MODE 4: WINDOW FILTERING & DATASET METRICS (-list)

Generates highly-formatted sequence arrays wrapped in brackets [] and quotes "". It prints the structures directly to the terminal while dumping a dataset to list_output.json for external script automation pipelines or Excel ingestion.

* Extract specific target tokens matching an array payload input:
  Compares the incoming token chain against the active database and returns an array of elements that actually exist within memory:
  ```bash
  python main.py -list target token1 token2 fake_token
  ```
* Generate an array list out of a specific index boundary window (range):
  Captures an isolated memory frame out of the middle of the database array storage:
  ```bash
  python main.py -list range 3 7
  ```
* Global database infrastructure analytical summary (stats):
  Scans the database via a unique element collector set(l), maps out unique entries, and processes an immutable data audit report displaying: total log volume (TOTAL_LOGS_ACCUMULATED), unique record entries (UNIQUE_MEMORY_ENTRIES), structural duplicate counts (DUPLICATE_CELLS_FOUND), and the precise database redundancy ratio (DATABASE_TRASH_RATIO):
  ```bash
  python main.py -list stats
  ```

---

## CRITICAL TRANSACTION ROLLBACK ENGINE

The controller is engineered around the fault-tolerance standards of mission-critical software systems. Prior to executing any database mutation, an isolated memory snapshot clone b = l.copy() is established inside RAM.

If an unexpected index overflow error (requesting rows out of bounds), data type mismatch (passing literal strings to index properties), or sub-flag exception occurs during processing, the system prevents binary file corruption or empty array writes.

The global exception cascade except (IndexError, ValueError, KeyError, Exception) intercepts the software panic, immediately discards the current transaction route, terminates the corrupted thread, and restores the system array directly from the original backup clone b. The persistent db.json on the disk remains completely safe, clean, and unaffected.
