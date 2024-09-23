from pathlib import Path
import os

# Platform-specific configuration
projects_path = os.path.dirname(os.path.realpath(__file__))
home_dir = Path.home()

# Path to folders
downloads_folder = home_dir / "Downloads"
documents_folder = home_dir / "Documents"
pictures_folder = home_dir / "Pictures"
desktop_folder = home_dir / "Desktop"
video_folder = home_dir / "Videos"
music_folder = home_dir / "Music"
# misc_folder = home_dir / "misc"

# Ensure misc folder exists ( if we want to have a folder for every other file type )
# misc_folder.mkdir(parents=True, exist_ok=True)

# File type to folder mapping
file_to_folder_hash = {
    "images": pictures_folder,
    "Documents": documents_folder,
    "Video": video_folder,
    "Audio": music_folder,
    # "Others": misc_folder,
}

# What file types do you want to move?
file_types = {
    "images": ['.jpeg', '.png', '.jpg', '.svg', '.tif', '.webp'],
    "Documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    "Video": ['.avi', '.mp4', '.mov', '.mkv'],
    "Audio": ['.mp3', '.ogg', '.wav', '.amr'],
}
