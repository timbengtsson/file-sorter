from datetime import datetime
from utils.config import desktop_folder
from utils.file_sorter import sort_files
from utils.logger import log_file, clear_old_logs

if __name__ == "__main__":
    # Get current data on local machine 
    now = datetime.now()

    try:
        log_file(str(now.strftime("%Y-%m-%d %H:%M:%S")) + " Starting file sorting...")
        sort_files(desktop_folder)
        clear_old_logs()
        log_file("Finished file sorting.\n")
    except Exception as ex:
        log_file(f"Error: {ex}")
