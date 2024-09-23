import shutil
from pathlib import Path
from utils.config import file_types, file_to_folder_hash
from utils.logger import log_file

def sort_files(folder_path):
    folder = Path(folder_path)

    for file in folder.iterdir():
        if file.is_file():
            move_file(file)
        else:
            log_file(f"Skipping folder /{file.name}/")
 

def move_file(file):
    try:
        for move_to_directory, extensions in file_types.items():
            for extension in extensions:
                if file.suffix.lower() == extension:
                    move_to_directory = str(file_to_folder_hash[move_to_directory])
                    destination = Path(move_to_directory) / file.name
                    shutil.move(str(file), str(destination))
                    log_file(f"Moved file {file} to {destination}")
                    return  # Move the file once and break out 
    except Exception as ex:
        log_file(f"Error while trying to move file {file}. Error: {ex}")
