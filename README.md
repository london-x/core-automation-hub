# core-automation-hub
All-in-One high-load CLI automation platform and server combiner. Includes a persistent JSON database core with strict data pruning, system metrics analyzer, infrastructure error scanner, autonomous e-commerce market price parser, and a universal Excel pipeline translator.

This repository is still under development and will be updated.

# USER MANUAL: CLI CONTROLLER & DBMS (main.py)

High-performance console controller and persistent database snapshot manager for main.py with zero external dependencies. Features single-letter atomic RAM arrays, strict validation, 4-mode window filtering, batch token scanning, and an integrated transaction rollback engine. The tool is written in pure Python 3, optimized for minimal RAM footprint, and preserves all persistent arrays inside a local JSON storage (`db.json`) on the SSD.

The controller includes a high-precision hardware profiler (`time.perf_counter`) that automatically benchmarks every transaction and outputs the exact execution delta in milliseconds (`v ms`) upon termination.

---

## MODE 1: MEMORY APPEND & CELL INSERTION (`-add`)

Ingests and appends any series of string tokens, integer identifiers, or fractional metrics directly into the persistent database.

*   **Global append to the end of the array storage:**
    ```bash
    python main.py -add token1 token2 99.4 4.22
    ```
*   **Surgical range insertion at an arbitrary index:**
    Slices the active database array in RAM and inserts new elements strictly at the specified 1-based human index position, shifting existing downstream entries to the right. Command to insert tokens at position №3:
    ```bash
    python main.py -add range 3 new_cell_1 new_cell_2
    ```
*   **Input perimeter verification:** Blank parameters or empty strings wrapped in quotes (`python main.py -add "   "`) are automatically stripped. The internal logic detects that the valid payload count `n` equals `0`, fires a strict `raise IndexError` fuse, aborts the corrupted payload append, and safely routing execution to the rollback sequence.

---

## MODE 2: BATCH INTELLECTUAL SEARCH RADAR (`-search`)

Performs high-speed parallel sequence scanning and reads data within RAM under a strict, non-mutating isolated route without modifying the source JSON file on disk.

*   **Global parallel lookup (Simultaneous index query and string scan):**
    ```bash
    python main.py -search query_word 3 target_token
    ```
    *   Pure integer strings (e.g., `3`) are automatically evaluated as absolute index lookups. The system shifts the human-readable coordinate back by one такт (`l[h - 1]`) and instantly extracts the string stored at that precise slot.
    *   Character-based words fail the initial integer parsing, get intercepted by a `ValueError` trap, and are rerouted into an optimized `enumerate` scanner. It maps the exact 1-based line coordinates of all matching duplicates along with the absolute occurrence calculation (`TOTAL_COUNT`).
*   **Numeric string escaping (The 'w' word prefix marker):**
    To scan for a string token comprised entirely of numbers (such as an object ID, area code, or numeric hash like `495`) as a literal text word instead of an index position, prepend the character marker `w`. The algorithm strips the prefix and passes the digits safely into the string matching engine, bypassing index overflow crashes:
    ```bash
    python main.py -search w495
    ```
*   **Bounded scanning inside a specific index slice window (`range`):**
    Narrows the scanner beam. Evaluates query tokens and calculates occurrence coordinates strictly within the requested boundary limits (e.g., from row 1 to 10), completely ignoring any database entries outside this active memory frame:
    ```bash
    python main.py -search range 1 10 query_word w495
    ```

---

## MODE 3: SURGICAL PRUNING & SYSTEM STORAGE PURGE (`-del`)

Provides complete structural control over storage size limitations on the SSD, allowing for pinpoint or mass cell erasures.

*   **Wipe entire persistent database storage array to absolute zero:**
    ```bash
    python main.py -del all
    ```
*   **Remove a specific cell via its 1-based human index number (e.g., row №2):**
    ```bash
    python main.py -del cell 2
    ```
*   **Mass purge of all duplicate entries matching a word pattern:**
    Deploys a list comprehension filter utilizing the `!=` inequality operator, completely cutting out the target word from the database array:
    ```bash
    python main.py -del word query_word
    ```
*   **Eradicate a slice window out of the middle of the storage array (e.g., rows 5 through 8):**
    Stitches together the immutable parts of the storage array before and after the targeted boundaries (`l[:x] + l[y:]`), dropping the middle slice out of memory:
    ```bash
    python main.py -del range 5 8
    ```

---

## MODE 4: WINDOW FILTERING, DATA EXPORT & ANALYTICS (`-list`)

Generates highly-formatted sequence arrays wrapped in brackets `[]` and quotes `""`. It prints the filtered structures directly to the terminal while dumping a sterile, raw dataset to `list_output.json` for external script automation pipelines or Excel ingestion.

*   **Extract specific target tokens matching an array payload input:**
    Compares the incoming token chain against the active database and returns an array of elements that actually exist within memory:
    ```bash
    python main.py -list target token1 token2 fake_token
    ```
*   **Generate an array list out of a specific index boundary window (e.g., rows 3 through 7):**
    Captures an isolated memory frame out of the middle of the database array storage:
    ```bash
    python main.py -list range 3 7
    ```
*   **Global database infrastructure analytical summary (`stats`):**
    Scans the database via a unique element collector `set(l)`, maps out unique entries, and processes an immutable data audit report displaying: total log volume, unique record entries, structural duplicate counts, and the precise database redundancy ratio:
    ```bash
    python main.py -list stats
    ```

---

## CORE TRANSACTION ROLLBACK ARCHITECTURE

The controller is engineered around the fault-tolerance standards of mission-critical software systems. Prior to executing any database mutation, an isolated memory snapshot clone `b = l.copy()` is established inside RAM.

If an unexpected index overflow error (requesting rows out of bounds), data type mismatch (passing literal strings to index properties), or sub-flag exception occurs during processing, **the system prevents binary file corruption or empty array writes**. 

The global exception cascade `except (IndexError, ValueError, KeyError, Exception)` intercepts the software panic, immediately discards the current transaction route, terminates the corrupted thread, and restores the system array directly from the original backup clone `b`. The persistent `db.json` on the disk remains completely safe, clean, and unaffected.
