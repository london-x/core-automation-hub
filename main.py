import sys
import json
import time

if __name__ == "__main__":
    start_time = time.perf_counter()
    args = sys.argv
    
    if len(args) < 3:
        print("ERR: NOT_ENOUGH_ARGS")
    else:
        mode = args[1].strip() if len(args) > 1 else ""
        
        try:
            with open("db.json", "r", encoding="utf-8") as f_in:
                db = json.load(f_in)
        except FileNotFoundError:
            db = []

        backup = db.copy()
        res = []

        try:
            if mode == "-add":
                dele = args[2].strip() if len(args) > 2 else ""
                
                def parse(val):
                    try: 
                        return int(val)
                    except ValueError:
                        try: 
                            return float(val)
                        except ValueError: 
                            return val

                if dele == "range" and len(args) > 4:
                    human_idx = int(args[3]) - 1
                    if human_idx < 0 or human_idx > len(db):
                        raise IndexError
                    queries = [parse(member.strip()) for member in args[4:] if member.strip()]
                    if not queries:
                        raise IndexError
                    db = db[:human_idx] + queries + db[human_idx:]
                    print(f"SUCCESS: INSERTED {len(queries)} CELLS AT POSITION {human_idx + 1}")
                else:
                    raw_args = args[2:] if dele != "range" else args[4:]
                    queries = [parse(member.strip()) for member in raw_args if member.strip()]
                    num = len(queries)
                    if num == 0:
                        raise IndexError
                    print(f"CREATED_NOW: {num}")
                    db.extend(queries)
                    print("SUCCESS: MEMORY_CELLS_APPENDED")
                print(f"TOTAL_STORAGE: {len(db)}")

            elif mode == "-search":
                print("CREATED_NOW: 0 (SEARCH_MODE_ACTIVE)")
                print(f"TOTAL_STORAGE: {len(db)}")
                
                dele = args[2].strip() if len(args) > 2 else ""
                
                if dele == "range" and len(args) > 5:
                    start_idx = int(args[3]) - 1
                    end_idx = int(args[4])
                    if start_idx < 0 or end_idx > len(db) or start_idx >= end_idx:
                        raise IndexError
                    queries = args[5:]
                    db_slice = db[start_idx:end_idx]
                    print(f"--- BATCH SEARCH RESULTS WITHIN RANGE {start_idx+1} TO {end_idx} ---")
                    for query in queries:
                        query = query.strip()
                        if query.startswith("w") and len(query) > 1:
                            word = query[1:]
                            if word in db_slice:
                                matches = [i + 1 + start_idx for i, member in enumerate(db_slice) if word == member]
                                print(f"[WORD '{word}'] -> № {matches} | TOTAL_COUNT: {len(matches)}")
                            else:
                                print(f"[WORD '{word}'] -> TOTAL_COUNT: 0 (NOT_FOUND)")
                        else:
                            try:
                                human_idx = int(query)
                                if start_idx + 1 <= human_idx <= end_idx:
                                    print(f"[INDEX {human_idx}] -> {db[human_idx - 1]}")
                                else:
                                    print(f"[INDEX {human_idx}] -> ERR: OUT_OF_SEARCH_RANGE")
                            except ValueError:
                                if query in db_slice:
                                    matches = [i + 1 + start_idx for i, member in enumerate(db_slice) if query == member]
                                    print(f"[WORD '{query}'] -> № {matches} | TOTAL_COUNT: {len(matches)}")
                                else:
                                    print(f"[WORD '{query}'] -> TOTAL_COUNT: 0 (NOT_FOUND)")
                else:
                    queries = args[2:] if dele != "range" else args[5:]
                    if not queries:
                        print("ERR: NO_SEARCH_QUERIES_PROVIDED")
                    else:
                        print("--- BATCH GLOBAL SEARCH RESULTS ---")
                        for query in queries:
                            query = query.strip()
                            if query.startswith("w") and len(query) > 1:
                                word = query[1:]
                                if word in db:
                                    matches = [i + 1 for i, member in enumerate(db) if word == member]
                                    print(f"[WORD '{word}'] -> № {matches} | TOTAL_COUNT: {len(matches)}")
                                else:
                                    print(f"[WORD '{word}'] -> TOTAL_COUNT: 0 (NOT_FOUND)")
                            else:
                                try:
                                    human_idx = int(query)
                                    if 1 <= human_idx <= len(db):
                                        print(f"[INDEX {human_idx}] -> {db[human_idx - 1]}")
                                    else:
                                        raise IndexError
                                except ValueError:
                                    if query in db:
                                        matches = [i + 1 for i, member in enumerate(db) if query == member]
                                        print(f"[WORD '{query}'] -> № {matches} | TOTAL_COUNT: {len(matches)}")
                                    else:
                                        print(f"[WORD '{query}'] -> TOTAL_COUNT: 0 (NOT_FOUND)")

            elif mode == "-del":
                print("CREATED_NOW: 0 (DELETE_MODE_ACTIVE)")
                dele = args[2].strip() if len(args) > 2 else ""
                
                if dele == "all":
                    db = []
                    print("SUCCESS: TOTAL_STORAGE_WIPED_TO_ZERO")
                    
                elif dele == "cell" and len(args) > 3:
                    human_idx = int(args[3])
                    if not (1 <= human_idx <= len(db)):
                        raise IndexError
                    word = db.pop(human_idx - 1)
                    print(f"SUCCESS: REMOVED CELL №{human_idx} ('{word}')")
                        
                elif dele == "word" and len(args) > 3:
                    word = args[3].strip()
                    num = len(db)
                    db = [member for member in db if word != member]
                    print(f"SUCCESS: REMOVED {num - len(db)} CELLS MATCHING '{word}'")

                elif dele == "range" and len(args) > 4:
                    start_idx = int(args[3]) - 1
                    end_idx = int(args[4])
                    if start_idx < 0 or end_idx > len(db) or start_idx >= end_idx:
                        raise IndexError
                    db = db[:start_idx] + db[end_idx:]
                    print(f"SUCCESS: WIPED RANGE FROM CELL {start_idx+1} TO {end_idx}")

                elif dele == "dups":
                    num = len(db)
                    db = list(dict.fromkeys(db))
                    print(f"SUCCESS: PURGED {num - len(db)} DUPLICATES. BASE IS CLEAN.")
                else:
                    raise KeyError
                print(f"TOTAL_STORAGE_NOW: {len(db)}")

            elif mode == "-list":
                dele = args[2].strip() if len(args) > 2 else ""
                
                if dele == "target" and len(args) > 3:
                    queries = [member.strip() for member in args[3:] if member.strip()]
                    res = [member for member in db if member in queries]
                    print(f"--- OUTPUTTING TARGETED DETECTED WORDS ({len(res)}) ---")
                    
                elif dele == "range" and len(args) > 4:
                    start_idx = int(args[3]) - 1
                    end_idx = int(args[4])
                    if start_idx < 0 or end_idx > len(db) or start_idx >= end_idx:
                        raise IndexError
                    res = db[start_idx:end_idx]
                    print(f"--- OUTPUTTING RANGE FROM CELL {start_idx+1} TO {end_idx} ---")

                elif dele == "stats":
                    num = len(db)
                    print("--- DATABASE INFRASTRUCTURE METRICS ---")
                    print(f"TOTAL_LOGS_ACCUMULATED : {num}")
                    print(f"UNIQUE_MEMORY_ENTRIES  : {len(set(db))}")
                    print(f"DUPLICATE_CELLS_FOUND  : {num - len(set(db))}")
                    print(f"DATABASE_TRASH_RATIO   : {round(((num - len(set(db))) / num) * 100, 2) if num > 0 else 0}%")
                    res = {"total": num, "unique": len(set(db)), "duplicates": num - len(set(db)), "trash_percent": round(((num - len(set(db))) / num) * 100, 2) if num > 0 else 0}
                else:
                    raise KeyError

                print(res)

                with open("list_output.json", "w", encoding="utf-8") as f_out:
                    json.dump(res, f_out, ensure_ascii=False, indent=4)
                print("SUCCESS: TARGET_LIST_EXPORTED_TO_SSD")

            else:
                raise KeyError

        except (IndexError, ValueError, KeyError, Exception):
            print("CRITICAL: LOGIC OR INDEX ERROR DETECTED!")
            print("TRANSACTION ABORTED -> ACTIVATING ROLLBACK FUNCTION...")
            db = backup.copy()
            print(f"TOTAL_STORAGE_RESTORED: {len(db)}")

        with open("db.json", "w", encoding="utf-8") as f_out:
            json.dump(db, f_out, ensure_ascii=False, indent=4)

    end_time = time.perf_counter()
    elapsed_ms = round((end_time - start_time) * 1000, 4)
    print(f"PERFORMANCE_BENCHMARK: {elapsed_ms} ms")
