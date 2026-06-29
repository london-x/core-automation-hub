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

### `booster.py` User Manual

### 1\. Preparation

Ensure that both `booster.py` and your target JSON file (e.g., `db.json`) are located in the exact same directory.

The JSON file must contain valid syntax, for example:

json

    {
        "id": 1,
        "status": "active"
    }
    


### 2\. Execution via CLI (CMD / Terminal)

Open your command line interface directly in the directory containing your files and execute the following command:

bash

    python booster.py db.json
    

### 3\. Core Mechanics & Technical Workflow

*   **Input Validation:** The script evaluates the command-line arguments. If the file argument is omitted or the specified file does not exist, the script prints an `ERR` message and terminates execution via `sys.exit(1)` to prevent a system crash.
*   **Data Redundancy:** The script instantly generates an identical backup snapshot file on the disk named `db.json.copy`. This preserves the original data state if the primary file is corrupted.
*   **Memory Allocation:** The raw text payload is parsed and converted into a live dictionary object directly within the volatile memory (RAM), rendering it ready for immediate high-speed computations.

### SnapDBMS Log Purger — Official User Manual

High-performance, transaction-safe command-line infrastructure utility designed for automated server maintenance, log rotation, and structural JSON database resetting.

* * *

###  HOW IT WORKS (OPERATIONAL MECHANICS)

The utility operates as a dedicated external maintenance node. It evaluates the target database file directly on the SSD disk, calculates the total number of logs, completely wipes all accumulated records, and re-initializes the storage as a clean, sterile JSON skeleton (`[]`) in a single processor tact.

* * *

###  TERMINAL COMMAND SYNTAX & OUTPUT CODES

The tool is managed completely via command-line arguments in your Terminal or Command Prompt.

### Global Command Template

bash

    python log_purger.py [path_to_json_file]
    


### 1\. Standard Database Purge

To completely clear your main database or log file, pass its path as the first argument:

bash

    python log_purger.py db.json
    


*   **System Action:** Validates file structure, empties all records, and saves a fresh empty database.
*   **Terminal Output:**
    *   `db.json` *(Target file confirmed)*
    *   `37` *(Number of records detected before wipe)*
    *   `SUCCESS` *(Operation completed safely)*
*   **OS Exit Code:** `0` (Success)

### 2\. Guardrail: Missing File Argument

If you launch the utility without specifying any target file path:

bash

    python log_purger.py
    


*   **System Action:** Instantly cuts power to the process to prevent accidental drive damage.
*   **Terminal Output:** `ERR: NO_FILE`
*   **OS Exit Code:** `1` (Aborted)

### 3\. Guardrail: File Not Found

If you provide a path to a file that does not physically exist on your disk:

bash

    python log_purger.py missing_database.json
    


*   **System Action:** Blocks execution before touching the drive framework.
*   **Terminal Output:** `ERR: NOT_FOUND`
*   **OS Exit Code:** `1` (Aborted)

### 4\. Emergency Auto-Repair Sequence

If you accidentally target a corrupted database, a broken text file, or an invalid `.json` configuration:

bash

    python log_purger.py broken_file.json
    


*   **System Action:** Automatically detects structural damage, prevents software freeze, and forces a hard system wipe.
*   **Terminal Output:** `CRITICAL` *(Corruption intercepted and repaired)*
*   **OS Exit Code:** `0` (Success — Storage channel is fully restored and ready for new writes)

* * *

###  INTEGRATION PROTOCOL FOR AUTOMATION RUNNERS

If you are embedding this utility into automated background tasks (PowerShell loops, Windows Task Scheduler, or Bash runners), use the following operating system exit codes to monitor the system state:

*   **Exit Code `0`:** Task executed with 100% success. The storage file is safe, empty, and operational.
*   **Exit Code `1`:** Critical abort. The input path was empty, invalid, or database access was blocked by the OS kernel.

### `panic_response.py` User Manual

### 1\. Pre-flight Setup

1.  Ensure both **`panic_response.py`** and your database file **`db.json`** are located in the exact same directory.
2.  The target JSON file must contain a valid dictionary object, for example:
    
    json
    
        {
            "id": 1,
            "status": "stable"
        }
        
    
    

### 2\. Execution via CLI (CMD / Terminal)

Open your terminal interface directly in the directory containing the files and execute the following command:

bash

    python panic_response.py db.json
    


### 3\. Core Mechanics & Panic Triggers

This script implements a strict **Panic & Recover** architectural pattern to guarantee runtime memory safety:

*   **Scenario A: Missing File (Panic Event)**  
    If you omit the file argument or specify a non-existent path, the script triggers the `panic()` sequence, prints a `CRITICAL` log, and halts execution immediately (`sys.exit(1)`) to safeguard the operating system.
*   **Scenario B: Broken Syntax (ValueError Recovery)**  
    If the file is empty or contains corrupted JSON data, the script captures a `ValueError`. It automatically bypasses the crash and injects a secure fallback state `{"status": "fallback", "neurons": 0}` straight into RAM.
*   **Scenario C: Memory Type Collision (TypeError Barrier)**  
    If the file is successfully read but contains a JSON array `[]` instead of a dictionary `{}`, the script catches a `TypeError`. It isolates the memory type collision and returns an empty dictionary to prevent system lag.
*   **RAII Resource Cleanup (`finally` block)**  
    Regardless of success or failure, the hardware execution bus is guaranteed to trigger the `finally` statement, releasing file streams and printing `SYS: Memory bus cleared`.

### `file_supervisor.py` Technical Documentation

### Overview

**`file_supervisor.py`** is a native batch file validation and infrastructure monitoring tool designed for Python 3.11+. It processes multiple target configuration or database JSON files sequentially, catches individual system failures without immediate termination, and processes multi-source errors concurrently using modern exception handling features.

### Core Features

*   **Fault-Tolerant Scanning:** Individual file crashes do not halt the global execution queue.
*   **Modern Error Aggregation:** Leverages native `ExceptionGroup` mechanisms to bundle discrete system anomalies into a single manageable payload.
*   **Concurrence Routing:** Utilizes `except*` block splitting to trigger dedicated micro-recovery protocols based on exact exception criteria (File Missing vs. Data Corruption vs. Type Collision).

* * *

### Architectural Pipeline & Flow

### 1\. Ingestion Phase

The script scans a predefined target matrix of critical data nodes:

python

    target_files = ["db.json", "matrix.json", "logs.json"]
    

Используйте код с осторожностью.

### 2\. Validation Stage (3-Tier Security Inspection)

Each target is checked via sequential validation vectors:

*   **FS Boundary Check (`IndexError`):** Confirms if the file exists on the physical hard drive path.
*   **Payload Sanity Check (`ValueError`):** Confirms if the text buffer contains valid non-empty data strings.
*   **Contract Specification Check (`TypeError`):** Confirms if `json.loads` parses correctly as an actionable iterable (`dict` or `list`).

### 3\. Aggregation Stage

All failures bypass script crash parameters and are safely stored inside a dedicated runtime array: `collected_errors`.

### 4\. Routing Stage (The `except*` Bus)

If anomalies exist, an `ExceptionGroup` is forced into the system bus. The logic splits execution pathways on a type-basis:

*   `except* IndexError` → Logs missing paths and triggers infrastructure file generation templates.
*   `except* ValueError` → Intercepts blank data and triggers fresh state snapshot recovery from cloud storage.
*   `except* TypeError` → Intercepts wrong schema structural designs and flags matrix reformatting pipelines.

### 5\. Ultimate Cleanup Phase

The `finally` block resolves unconditionally across all outcomes, resetting infrastructure state and clearing temporary RAM caches.

* * *

### Technical Specifications

*   **Runtime Requirement:** Python 3.11 or higher (strictly required for syntax compiling).
*   **Dependencies:** Zero third-party dependencies. Powered by standard libraries (`json`, `sys`, `pathlib`).

### `transaction_processor.py` Technical Reference Manual

### Purpose

The script acts as a fault-tolerant financial ledger gatekeeper. It ingests banking data arrays, separates clean operations from malicious fraud requests, and logs execution traces into isolated tracking repositories without freezing the parent infrastructure.

* * *

### Technical Baseline

*   **Interpreter Target:** Python 3.10 or higher
*   **Dependencies:** Zero external libraries (Standard standard `json`, `sys`, `pathlib` engine packages only)

* * *

### Structural Data Pipeline

### 1\. Inbound Ingestion Guard

The execution stack mounts path elements and performs hardware checks:

*   Verifies file footprints on the drive grid. Triggers terminal lockdown if targets are missing.
*   Bounds file stream context buffers inside safe, non-leaking operational envelopes.
*   Automatically serializes raw string vectors into accessible dictionary objects.

### 2\. Multi-Branch Pattern Routing

Every isolated array dictionary entity faces deep pattern inspections:

*   **Approved Node:** Operations matching success criteria and carrying positive values clear the gateway.
*   **Banking Refusal Node:** Explicitly logged external drops route into anomaly buffers.
*   **Malicious Inversion Node:** Broken definitions or fuzzing inputs fall into the global fallback boundary trap.

### 3\. Assertion Boundary Fuse

An absolute logical constraint evaluates core transaction attributes. Negative tracking identifiers trigger internal system exceptions, breaking corrupt execution paths to secure downstream registry storage integrity.

### 4\. Split Logging Persistence

The execution cleanup track enforces permanent file persistence before system shutdown:

*   **`success_log.json`**: Pristine ledger ledger entries cleared for settlement transactions.
*   **`errors_log.json`**: Corrupt metadata payloads, failure track names, and debug traces for system review.

### User Manual: infrastructure\_provisioner.py

### 1\. CREATE MODE (3+ Args)

Creates a directory tree and generates a file with any extension and text content.

bash

    python infrastructure_provisioner.py core/logs info.txt "Log payload text"
    

Используйте код с осторожностью.

*   **Output:**
    
    text
    
        CREATED
        SIZE_BYTES: 16
        
    
    Используйте код с осторожностью.
    

### 2\. INSPECT MODE (1 Arg)

Calculates the exact size of a file or an entire directory in bytes.

bash

    python infrastructure_provisioner.py core
    

Используйте код с осторожностью.

*   **Output:**
    
    text
    
        TYPE: FOLDER
        TARGET_PATH: core
        SIZE_BYTES: 12480
        
    
    Используйте код с осторожностью.
    

### 3\. SYSTEM EXIT CODES

*   `0` — Success. Operation finished without errors.
*   `1` — Abort. Path not found, or missing arguments.
