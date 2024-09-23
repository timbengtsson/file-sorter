import time
from pathlib import Path
import datetime
from utils.config import projects_path

now = datetime.datetime.now()

def clear_old_logs(days=5):
    now_time = time.time()
    age_in_seconds = days * 86400
    log_dir = Path(projects_path) / 'logs'

    if not log_dir.exists():
        log_dir.mkdir(parents=True)

    for log_file in log_dir.iterdir():
        if log_file.is_file():
            file_age = now_time - log_file.stat().st_mtime
            if file_age > age_in_seconds:
                print(f"Removing {log_file}")
                log_file.unlink()

def log_file(message):
    event_log = Path(projects_path) / 'logs' / (now.strftime('%Y_%m_%d') + ".log")

    if not event_log.parent.exists():
        event_log.parent.mkdir(parents=True)

    with open(event_log, "a") as file_handle:
        file_handle.write(str(message) + "\n")
