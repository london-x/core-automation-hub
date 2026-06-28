import sys
import json
from pathlib import Path

if __name__ == "__main__":
    a = sys.argv
    
    if len(a) < 2:
        print("Ошибка: Укажите путь к файлу в аргументах!")
        sys.exit(1)
        
    config_path = Path(a[1])
    
    if not config_path.exists():
        print(f"Ошибка: Файл по пути '{config_path}' не существует!")
        sys.exit(1)
        
    with open(config_path, "r", encoding="utf-8") as file:
        raw_data = file.read()
        
    copy_path = config_path.with_suffix(config_path.suffix + ".copy")
    with open(copy_path, "w", encoding="utf-8") as copy_file:
        copy_file.write(raw_data)
        
    json_data = json.loads(raw_data)
    
    print(f"Успех: Конфигурация '{config_path.name}' успешно загружена в RAM!")
    print(f"Защитный слепок сохранен по пути: '{copy_path.name}'")
    print("\n--- СОДЕРЖИМОЕ JSON МАТРИЦЫ ---")
    print(json_data)
