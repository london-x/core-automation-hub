import sys
import json

if __name__ == "__main__":
    """
    🛰️ CORE AUTOMATION HUB & PERSISTENT RECOVERY STORAGE
    
    DECODING ATOMIC VARIABLES ON THE RAM BOARD:
    -----------------------------------------------------
    a (args)      ──► [sys.argv] Input terminal command line arguments.
    u (user_flag) ──► [user_flag] Main global operating mode (-add, -search, -del).
    f (file)      ──► [file] Internal contextual file stream for SSD access.
    l (list)      ──► [list_storage] Persistent database array inside db.json.
    n (number)    ──► [new_count] Number of incoming cells loaded into RAM right now.
    m (member)    ──► [member] Current single element used inside list comprehensions.
    s (search)    ──► [search_queries] Batch query train for parallel scanning.
    q (query)     ──► [query] Current target query processed from the batch.
    h (human_idx) ──► [human_index] User-friendly cell index (starts tracking from 1).
    r (result)    ──► [result_basket] Address basket for matching duplicates coordinates.
    d (delete)    ──► [delete_sub_flag] Data pruning sub-mode (all, cell, word, etc).
    w (word)      ──► [word] Target data extracted from the persistent database index.
    t (target)    ──► [target_word] Specific value wiped from the storage by match.
    k (kill_len)  ──► [old_length] Database array size checked before data purging.
    x (cut_start) ──► [cut_start_count] Number of cells sliced away from file start.
    y (cut_end)   ──► [cut_end_count] Number of cells sliced away from file end.
    """
    a = sys.argv
    
    if len(a) < 3:
        print("ERR: NOT_ENOUGH_ARGS")
    else:
        u = a[1].strip()
        
        try:
            with open("db.json", "r", encoding="utf-8") as f:
                l = json.load(f)
        except FileNotFoundError:
            l = []

        b = l.copy()

        try:
            if u == "-add":
                n = len([m.strip() for m in a[2:] if m.strip()])
                if n == 0:
                    raise IndexError
                print(f"CREATED_NOW: {n}")
                l.extend([m.strip() for m in a[2:] if m.strip()])
                print(f"TOTAL_STORAGE: {len(l)}")
                print("SUCCESS: MEMORY_CELLS_APPENDED")

            elif u == "-search":
                print("CREATED_NOW: 0 (SEARCH_MODE_ACTIVE)")
                print(f"TOTAL_STORAGE: {len(l)}")
                s = a[2:]
                if not s:
                    print("ERR: NO_SEARCH_QUERIES_PROVIDED")
                else:
                    print("--- BATCH SEARCH RESULTS ---")
                    for q in s:
                        q = q.strip()
                        try:
                            h = int(q)
                            if 1 <= h <= len(l):
                                print(f"[INDEX {h}] -> {l[h - 1]}")
                            else:
                                raise IndexError
                        except ValueError:
                            if q in l:
                                r = [i + 1 for i, m in enumerate(l) if m == q]
                                print(f"[WORD '{q}'] -> № {r} | TOTAL_COUNT: {len(r)}")
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
                    t = a[3].strip()
                    if t not in l:
                        raise ValueError
                    k = len(l)
                    l = [m for m in l if m != t]
                    print(f"SUCCESS: REMOVED {k - len(l)} CELLS OF '{t}'")
                        
                elif d == "cut_start" and len(a) > 3:
                    x = int(a[3])
                    if x >= len(l) or x < 0:
                        raise IndexError
                    l = l[x:]
                    print(f"SUCCESS: CUT {x} CELLS FROM START")
                        
                elif d == "cut_end" and len(a) > 3:
                    y = int(a[3])
                    if y >= len(l) or y < 0:
                        raise IndexError
                    l = l[:-y]
                    print(f"SUCCESS: CUT {y} CELLS FROM END")
                else:
                    raise KeyError
                    
                print(f"TOTAL_STORAGE_NOW: {len(l)}")
                
            else:
                raise KeyError

        except (IndexError, ValueError, KeyError, Exception):
            print("🚨 CRITICAL: LOGIC OR INDEX ERROR DETECTED!")
            print("🛡️ TRANSACTION ABORTED -> ACTIVATING ROLLBACK FUNCTION...")
            l = b.copy()
            print(f"TOTAL_STORAGE_RESTORED: {len(l)}")

        with open("db.json", "w", encoding="utf-8") as f:
            json.dump(l, f, ensure_ascii=False, indent=4)
            
