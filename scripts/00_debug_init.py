import os
import datetime

try:
    log_path = os.path.join(os.path.dirname(__file__), "debug_init_log.txt")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()}: 00_debug_init.py loaded\n")
    print("00_debug_init.py loaded and logged to " + log_path)
except Exception as e:
    print(f"00_debug_init.py failed: {e}")
