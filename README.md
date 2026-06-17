# core-automation-hub
All-in-One high-load CLI automation platform and server combiner. Includes persistent JSON database core with strict data pruning, system metrics analyzer, infrastructure error scanner, and autonomous e-commerce market price parser.

This repository is still under development and will be updated.

 🛰️ [CORE-AUTOMATION-HUB]: ГЛОБАЛЬНАЯ КАРТА АВТОМАТИЗАЦИИ СФЕРЫ №1
========================================================================
                                
       [ ВХОДНОЙ СИЛОВОЙ КАБЕЛЬ: АРГУМЕНТЫ sys.argv / ТЕРМИНАЛ ]
                                   │
                                   ▼
        ┌─────────────────────────────────────────────────────┐
        │   ЦЕНТРАЛЬНЫЙ МОНОЛИТ СУБД И КОНТРОЛЛЕР (main.py)   │
        │ ─────────────────────────────────────────────────── │
        │  • Пакетный зрячий нано-сканер логов (enumerate)    │
        │  • Ручной предохранитель холостого такта (raise)    │
        │  • Бронированный замок сохранения SSD (json.dump)   │
        │  • СЕО-Движок транзакционного отката (RAM Rollback) │
        └──────────────────┬──────────────┬───────────────────┘
                           │              │
         ┌─────────────────┘              └─────────────────┐
         │                                                  │
         ▼                                                  ▼
┌─────────────────────────────────┐        ┌──────────────────────────────────┐
│  АНАЛИЗАТОР ЖЕЛЕЗА (sys_info)   │        │   СЕТЕВОЙ СТОРОЖ (net_monitor)   │
│ ─────────────────────────────── │        │ ──────────────────────────────── │
│ • Вызов поршней ядра ОС (wmic)  │        │ • Пинг интернет-пакетов (loss/ms)│
│ • Просчет свободных Гб на SSD  │        │ • Сканер системных крашей ОС     │
│ • Зрячие Excel-таблицы (CSV)    │        │ • Моментальный пуш логов ошибок  │
└────────────────┬────────────────┘        └────────────────┬─────────────────┘
                 │                                          │
                 └─────────────────┬────────────────────────┘
                                   │
                                   ▼
        ┌─────────────────────────────────────────────────────┐
        │     АВТОНОМНЫЙ СУВЕРЕННЫЙ ПОИСКОВИК (price_parser)  │
        │ ─────────────────────────────────────────────────── │
        │  • Скрытый обход сайтов без цензуры (HTTP Requests) │
        │  • Выжигание бинарного мусора и HTML-текста в RAM   │
        │  • Авто-скачивание любых файлов (.pdf/.zip/.exe)    │
        │  • Фиксация аналитики и выгрузка напрямую в EXCEL   │
        └─────────────────────────────────────────────────────┘

# 🛰️ main.py

High-load CLI controller and persistent database snapshot manager for main.py with zero external dependencies. Features single-letter atomic RAM arrays, strict validation, 4-mode array filtering, batch token scanning, and transaction rollback engine.

This repository is under development and will be updated.

---

## 🚀 HOW TO USE

### 1. Append Memory Cells (Write Mode)
Insert any series of data tokens, integers, or fractional values directly into the database:
```bash
python main.py -add data1 data2 4.22 -hz
```
*Security note: Empty inputs inside quotes trigger an internal `IndexError` via `raise`, instantly blocking bad data writes to the SSD.*

### 2. Batch Search (Read Mode)
Parallel scan for query matches or pull precise database cells using 1-based human indexing:
```bash
python main.py -search data1 3
```

### 3. Surgical Data Pruning (Wipe Mode)
* **Wipe entire storage database array to zero:** `python main.py -del all`
* **Remove cell via index position:** `python main.py -del cell 2`
* **Eradicate word duplicate entries:** `python main.py -del word data1`
* **Slice values from the start sequence:** `python main.py -del cut_start 3`
* **Slice values from the end sequence:** `python main.py -del cut_end 2`

### 4. Token List Generator (Export Mode)
Generate highly-formatted string array outputs wrapped in brackets `[]` and quotes `""`:
* **Output all words from database:** `python main.py -list all`
* **Filter and output targeted list of specific words:** `python main.py -list target data1 data2`
* **Generate array list of N items from the start:** `python main.py -list start 5`
* **Generate array list of N items from the end:** `python main.py -list end 3`
*Outputs are printed to console and automatically exported to `list_output.json` for external Excel parsing tools.*

---

## 🛡️ CORE TRANSACTION ROLLBACK
Any unexpected indexing overflow, data type clash, or sub-flag error during execution triggers a safe exception route. The controller drops the corrupted transaction and restores the memory state array directly from the original RAM backup clone.
