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

High-load CLI controller and persistent database snapshot manager for main.py with zero external dependencies. Features single-letter atomic RAM arrays, strict validation, batch token scanning, and transaction rollback engine.

---

## 🚀 HOW TO USE

### 1. Append Memory Cells (Write Mode)
Insert any series of data tokens, integers, or fractional values directly into the database:
```bash
python main.py -add data1 data2 4.22 -hz
```
*Security note: Empty strings or blank spaces trigger an internal `IndexError` via `raise`, instantly blocking bad data writes to the SSD.*

### 2. Batch Search (Read Mode)
Parallel scan for query matches or pull precise database cells using 1-based human indexing:
```bash
python main.py -search data1 3
```

### 3. Surgical Data Pruning (Wipe Mode)

* **Wipe entire storage database array to zero:**
  ```bash
  python main.py -del all
  ```
* **Remove specific target cell via human index position:**
  ```bash
  python main.py -del cell 2
  ```
* **Eradicate all duplicate entries matching a word pattern:**
  ```bash
  python main.py -del word data1
  ```
* **Slice fixed number of values from the start sequence:**
  ```bash
  python main.py -del cut_start 3
  ```
* **Slice fixed number of values from the end sequence:**
  ```bash
  python main.py -del cut_end 2
  ```

---

## 🛡️ CORE TRANSACTION ROLLBACK
Any unexpected indexing overflow, data type clash, or sub-flag error during execution triggers a safe exception route. The controller drops the corrupted transaction and restores the memory state array directly from the original RAM backup clone.
