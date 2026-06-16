# core-automation-hub
All-in-One high-load CLI automation platform and server combiner. Includes persistent JSON database core with strict data pruning, system metrics analyzer, infrastructure error scanner, and autonomous e-commerce market price parser.

This repository is still under development and will be updated.

# 🛰️ main.py

All-in-One high-load CLI automation platform and server combiner. Includes persistent JSON database core with strict data pruning.

---

## 🚀 HOW TO USE

### 1. Append Memory Cells (Write Mode)
Insert any number of data chunks or words into the persistent database storage:
```bash
python main.py -add data1 data2 data3 word4
```
*System will automatically display `CREATED_NOW` count and `TOTAL_STORAGE` capacity.*

### 2. Batch Search (Read Mode)
Scan the storage parallelly for words or query human indexes (starting from 1) without touching the hard drive:
```bash
python main.py -search word4 2
```

### 3. Data Pruning & Surgical Deletion (Wipe Mode)

* **Wipe everything to absolute zero:**
  ```bash
  python main.py -del all
  ```
* **Remove specific cell by human index number:**
  ```bash
  python main.py -del cell 2
  ```
* **Purge all existing duplicates of a targeted word:**
  ```bash
  python main.py -del word data1
  ```
* **Slice fixed number of cells from the start:**
  ```bash
  python main.py -del cut_start 3
  ```
* **Slice fixed number of cells from the end:**
  ```bash
  python main.py -del cut_end 2
  ```
