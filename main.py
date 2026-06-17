import sys
import json
import time

if __name__ == "__main__":
    t = time.perf_counter()

    """
    a (args)        ──► [sys.argv] Input terminal command line arguments.
    u (user_flag)   ──► [user_flag] Global modes (-add, -search, -del, -list).
    f (file)        ──► [file] Internal contextual file stream for SSD access.
    l (list)        ──► [list_storage] Persistent database array inside db.json.
    n (number)      ──► [num] General atomic memory counter / slicing parameter.
    m (member)      ──► [member] Single elements used inside list comprehensions.
    s (search)      ──► [queries] Secondary batch query arrays for scans/filters.
    q (query)       ──► [query] Target query value currently being processed.
    h (human_idx)   ──► [human_index] 1-based index marker for user-facing prints.
    r (result)      ──► [result_basket] Output container for matches and lists.
    d (delete)      ──► [sub_flag] Secondary controller option flags for del/list.
    b (backup)      ──► [backup_list] Isolated RAM snapshot clone for rollback.
    k (raw_s)       ──► [raw_search] Unprocessed incoming slice of command tokens.
    p (sub_list)    ──► [sub_list_range] Target chunk sliced from database in bounds.
    c (coords)      ──► [coordinate_basket] Calculated 1-based line markers for dups.
    w (target)      ──► [target_value] String target after dropping character markers.
    o (list_file)   ──► [list_file_stream] Standalone text stream for search exports.
    z (time_end)    ──► [time_end] High-precision benchmark marker captured at stop.
    v (ms_delta)    ──► [ms_delta] Final elapsed calculation interval in milliseconds.
    x (range_start) ──► [range_start] Lower limit human index integer for window.
    y (range_end)   ──► [range_end] Upper limit human index integer for window.
    """
    a = sys.argv
    
    if len(a) < 3:
        print("ERR: NOT_ENOUGH_ARGS")
    else:
        u = a[1].strip() if len(a) > 1 else ""
        
        try:
            with open("db.json", "r", encoding="utf-8") as f:
                l = json.load(f)
        except FileNotFoundError:
            l = []

        b = l.copy()
        r = []

        try:
            if u == "-add":
                d = a[2].strip() if len(a) > 2 else ""
                
                if d == "range" and len(a) > 4:
                    h = int(a[3]) - 1
                    if h < 0 or h > len(l):
                        raise IndexError
                    s = [m.strip() for m in a[4:] if m.strip()]
                    if not s:
                        raise IndexError
                    l = l[:h] + s + l[h:]
                    print(f"SUCCESS: INSERTED {len(s)} CELLS AT POSITION {h + 1}")
                else:
                    k = a[2:] if d != "range" else a[4:]
                    s = [m.strip() for m in k if m.strip()]
                    n = len(s)
                    if n == 0:
                        raise IndexError
                    print(f"CREATED_NOW: {n}")
                    l.extend(s)
                    print("SUCCESS: MEMORY_CELLS_APPENDED")
                print(f"TOTAL_STORAGE: {len(l)}")

            elif u == "-search":
                print("CREATED_NOW: 0 (SEARCH_MODE_ACTIVE)")
                print(f"TOTAL_STORAGE: {len(l)}")
                
                d = a[2].strip() if len(a) > 2 else ""
                
                if d == "range" and len(a) > 5:
                    x = int(a[3]) - 1
                    y = int(a[4])
                    if x < 0 or y > len(l) or x >= y:
                        raise IndexError
                    s = a[5:]
                    p = l[x:y]
                    print(f"--- BATCH SEARCH RESULTS WITHIN RANGE {x+1} TO {y} ---")
                    for q in s:
                        q = q.strip()
                        if q.startswith("w") and len(q) > 1:
                            w = q[1:]
                            if w in p:
                                c = [i + 1 + x for i, m in enumerate(p) if w == m]
                                print(f"[WORD '{w}'] -> № {c} | TOTAL_COUNT: {len(c)}")
                            else:
                                print(f"[WORD '{w}'] -> TOTAL_COUNT: 0 (NOT_FOUND)")
                        else:
                            try:
                                h = int(q)
                                if x + 1 <= h <= y:
                                    print(f"[INDEX {h}] -> {l[h - 1]}")
                                else:
                                    print(f"[INDEX {h}] -> ERR: OUT_OF_SEARCH_RANGE")
                            except ValueError:
                                if q in p:
                                    c = [i + 1 + x for i, m in enumerate(p) if q == m]
                                    print(f"[WORD '{q}'] -> № {c} | TOTAL_COUNT: {len(c)}")
                                else:
                                    print(f"[WORD '{q}'] -> TOTAL_COUNT: 0 (NOT_FOUND)")
                else:
                    s = a[2:] if d != "range" else a[5:]
                    if not s:
                        print("ERR: NO_SEARCH_QUERIES_PROVIDED")
                    else:
                        print("--- BATCH GLOBAL SEARCH RESULTS ---")
                        for q in s:
                            q = q.strip()
                            if q.startswith("w") and len(q) > 1:
                                w = q[1:]
                                if w in l:
                                    c = [i + 1 for i, m in enumerate(l) if w == m]
                                    print(f"[WORD '{w}'] -> № {c} | TOTAL_COUNT: {len(c)}")
                                else:
                                    print(f"[WORD '{w}'] -> TOTAL_COUNT: 0 (NOT_FOUND)")
                            else:
                                try:
                                    h = int(q)
                                    if 1 <= h <= len(l):
                                        print(f"[INDEX {h}] -> {l[h - 1]}")
                                    else:
                                        raise IndexError
                                except ValueError:
                                    if q in l:
                                        c = [i + 1 for i, m in enumerate(l) if q == m]
                                        print(f"[WORD '{q}'] -> № {c} | TOTAL_COUNT: {len(c)}")
                                    else:
                                        print(f"[WORD '{q}'] -> TOTAL_COUNT: 0 (NOT_FOUND)")

            elif u == "-del":
                print("CREATED_NOW: 0 (DELETE_MODE_ACTIVE)")
                d = a[2].strip() if len(a) > 2 else ""
                
                if d == "all":
                    l = []
                    print("SUCCESS: TOTAL_STORAGE_WIPED_TO_ZERO")
                    
                elif d == "cell" and len(a) > 3:
                    h = int(a[3])
                    if not (1 <= h <= len(l)):
                        raise IndexError
                    w = l.pop(h - 1)
                    print(f"SUCCESS: REMOVED CELL №{h} ('{w}')")
                        
                elif d == "word" and len(a) > 3:
                    w = a[3].strip()
                    n = len(l)
                    l = [m for m in l if w != m]
                    print(f"SUCCESS: REMOVED {n - len(l)} CELLS MATCHING '{w}'")

                elif d == "range" and len(a) > 4:
                    x = int(a[3]) - 1
                    y = int(a[4])
                    if x < 0 or y > len(l) or x >= y:
                        raise IndexError
                    l = l[:x] + l[y:]
                    print(f"SUCCESS: WIPED RANGE FROM CELL {x+1} TO {y}")

                elif d == "dups":
                    n = len(l)
                    l = list(dict.fromkeys(l))
                    print(f"SUCCESS: PURGED {n - len(l)} DUPLICATES. BASE IS CLEAN.")
                else:
                    raise KeyError
                print(f"TOTAL_STORAGE_NOW: {len(l)}")

            elif u == "-list":
                d = a[2].strip() if len(a) > 2 else ""
                
                if d == "target" and len(a) > 3:
                    s = [m.strip() for m in a[3:] if m.strip()]
                    r = [m for m in l if m in s]
                    print(f"--- OUTPUTTING TARGETED DETECTED WORDS ({len(r)}) ---")
                    
                elif d == "range" and len(a) > 4:
                    x = int(a[3]) - 1
                    y = int(a[4])
                    if x < 0 or y > len(l) or x >= y:
                        raise IndexError
                    r = l[x:y]
                    print(f"--- OUTPUTTING RANGE FROM CELL {x+1} TO {y} ---")

                elif d == "stats":
                    n = len(l)
                    print("--- DATABASE INFRASTRUCTURE METRICS ---")
                    print(f"TOTAL_LOGS_ACCUMULATED : {n}")
                    print(f"UNIQUE_MEMORY_ENTRIES  : {len(set(l))}")
                    print(f"DUPLICATE_CELLS_FOUND  : {n - len(set(l))}")
                    print(f"DATABASE_TRASH_RATIO   : {round(((n - len(set(l))) / n) * 100, 2) if n > 0 else 0}%")
                    r = {"total": n, "unique": len(set(l)), "duplicates": n - len(set(l)), "trash_percent": round(((n - len(set(l))) / n) * 100, 2) if n > 0 else 0}
                else:
                    raise KeyError

                print(r)

                with open("list_output.json", "w", encoding="utf-8") as o:
                    json.dump(r, o, ensure_ascii=False, indent=4)
                print("SUCCESS: TARGET_LIST_EXPORTED_TO_SSD")

            else:
                raise KeyError

                except (IndexError, ValueError, KeyError, Exception):
                    print("CRITICAL: LOGIC OR INDEX ERROR DETECTED!")
                    print("TRANSACTION ABORTED -> ACTIVATING ROLLBACK FUNCTION...")
                    l = b.copy()
                    print(f"TOTAL_STORAGE_RESTORED: {len(l)}")

                with open("db.json", "w", encoding="utf-8") as f:
                    json.dump(l, f, ensure_ascii=False, indent=4)
