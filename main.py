import sys
import json

if __name__ == "__main__":
    """
    🛰️ CORE AUTOMATION HUB & MULTI-MODE 4-FUNCTION RECOVERY STORAGE
    
    DECODING ATOMIC VARIABLES ON THE RAM BOARD:
    -----------------------------------------------------
    a (args)      ──► [sys.argv] Input terminal command line arguments.
    u (user_flag) ──► [user_flag] Global modes (-add, -search, -del, -list).
    f (file)      ──► [file] Internal contextual file stream for SSD access.
    l (list)      ──► [list_storage] Persistent database array inside db.json.
    n (number)    ──► [num] General atomic memory counter / slicing parameter.
    m (member)    ──► [member] Single elements used inside list comprehensions.
    s (search)    ──► [queries] Secondary batch query arrays for scans/filters.
    q (query)     ──► [query] Target query value currently being processed.
    h (human_idx) ──► [human_index] 1-based index marker for user-facing prints.
    r (result)    ──► [result_basket] Output container for matches and lists.
    d (delete)    ──► [sub_flag] Secondary controller option flags for del/list.
    """
    a = sys.argv
    
    if len(a) < 3:
        print("ERR: NOT_ENOUGH_ARGS")
    else:
        u = a.strip()
        
        try:
            with open("db.json", "r", encoding="utf-8") as f:
                l = json.load(f)
        except FileNotFoundError:
            l = []

        b = l.copy()
        r = []

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
                                coords = [i + 1 for i, m in enumerate(l) if m == q]
                                print(f"[WORD '{q}'] -> № {coords} | TOTAL_COUNT: {len(coords)}")
                            else:
                                print(f"[WORD '{q}'] -> TOTAL_COUNT: 0 (NOT_FOUND)")

            elif u == "-del":
                print("CREATED_NOW: 0 (DELETE_MODE_ACTIVE)")
                d = a.strip() if len(a) > 2 else ""
                
                if d == "all":
                    l = []
                    print("SUCCESS: TOTAL_STORAGE_WIPED_TO_ZERO")
                    
                elif d == "cell" and len(a) > 3:
                    h = int(a)
                    if not (1 <= h <= len(l)):
                        raise IndexError
                    w = l.pop(h - 1)
                    print(f"SUCCESS: REMOVED CELL №{h} ('{w}')")
                        
                elif d == "word" and len(a) > 3:
                    t = a.strip()
                    if t not in l:
                        raise ValueError
                    k = len(l)
                    l = [m for m in l if m != t]
                    print(f"SUCCESS: REMOVED {k - len(l)} CELLS OF '{t}'")
                        
                elif d─────────────────┘
                    n = int(a)
                    if n >= len(l) or n < 0:
                        raise IndexError
                    l = l[n:]
                    print(f"SUCCESS: CUT {n} CELLS FROM START")
                        
                elif d == "cut_end" and len(a) > 3:
                    n = int(a)
                    if n >= len(l) or n < 0:
                        raise IndexError
                    l = l[:-n]
                    print(f"SUCCESS: CUT {n} CELLS FROM END")
                else:
                    raise KeyError

            elif u == "-list":
                d = a.strip() if len(a) > 2 else ""
                
                if d == "all":
                    r = l.copy()
                    print(f"--- OUTPUTTING ALL WORDS ({len(r)}) ---")
                    
                elif d == "target" and len(a) > 3:
                    s = [m.strip() for m in a[3:] if m.strip()]
                    r = [m for m in s if m in l]
                    print(f"--- OUTPUTTING TARGETED DETECTED WORDS ({len(r)}) ---")
                    
                elif d == "start" and len(a) > 3:
                    n = int(a)
                    if n < 0 or n > len(l):
                        raise IndexError
                    r = l[:n]
                    print(f"--- OUTPUTTING {n} WORDS FROM START ---")
                    
                elif d == "end" and len(a) > 3:
                    n = int(a)
                    if n < 0 or n > len(l):
                        raise IndexError
                    r = l[-n:] if n > 0 else []
                    print(f"--- OUTPUTTING {n} WORDS FROM END ---")
                else:
                    raise KeyError

                print(r)

                with open("list_output.json", "w", encoding="utf-8") as lf:
                    json.dump(r, lf, ensure_ascii=False, indent=4)
                print("SUCCESS: TARGET_LIST_EXPORTED_TO_SSD")

            else:
                raise KeyError

        except (IndexError, ValueError, KeyError, Exception):
            print("🚨 CRITICAL: LOGIC OR INDEX ERROR DETECTED!")
            print("🛡️ TRANSACTION ABORTED -> ACTIVATING ROLLBACK FUNCTION...")
            l = b.copy()
            print(f"TOTAL_STORAGE_RESTORED: {len(l)}")

        with open("db.json", "w", encoding="utf-8") as f:
            json.dump(l, f, ensure_ascii=False, indent=4)
