
# File Sorter

A Python script that automatically organizes files from your desktop into categorized folders based on file type. The script makes it easier to keep your desktop clean by sorting files into designated folders.

## Features

- Automatically moves files from your desktop to pre-defined folders based on their file type.
- Customizable configuration to define which file types should be moved and where.
- Batch files for easy execution and automation of the sorting process.
- Supports a variety of file formats, such as images, documents, and media files.

## Table of Contents

- [File Sorter](#file-sorter)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Logs](#logs)
  - [Configuration](#configuration)
    - [Example `config.py`:](#example-configpy)
    - [How to Customize:](#how-to-customize)
  - [Batch Files](#batch-files)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/timbengtsson/file-sorter.git
   ``` 

2. **Navigate to the project directory:**

   ```bash
   cd file-sorter
   ``` 

3. **Install required dependencies (if any):**

   Currently, there are no external dependencies. Just ensure you have Python 3.x installed.

## Usage

1. **Run the Python Script:**

   You can manually run the Python script to sort files on your desktop:

   ```bash
   python main.py
   ```

   By default, the script will sort common file types (e.g., images, documents) into their respective folders like `Images`, `Documents`, etc.


## Logs 

The script will log all files it moves to the console. You can view the logs in the `logs` folder in the project directory.

There will be a log file for each day 5 days back in time.

## Configuration

You can customize the sorting behavior by modifying the `config.py` file located in the project `utils` directory. This file allows you to add or edit which file types should be sorted and where they should be moved.

### Example `config.py`:

```python
file_types = {
    "images": ['.jpeg', '.png', '.jpg', '.svg', '.tif', '.webp'],
    "Documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    "Video": ['.avi', '.mp4', '.mov', '.mkv'],
    "Audio": ['.mp3', '.ogg', '.wav', '.amr'],
}
```

### How to Customize:

1. **Add a new folder category:**

   If you want to add a new folder (for example Database .sql files), simply add an entry in the `config.json` file:

   ```json
   "Database": [".sql"]
   ```

2. **Edit existing categories:**

   To modify existing categories, just update the list of file extensions under each folder name.

3. **Remove file extensions from sorting:**

   Remove a file extension from the list to prevent that file type from being sorted into a specific folder.

## Batch Files

To automate running the script, batch files are provided for ease of use:

- **Windows:** You can run the `double_click_to_set_up_task.bat` file to set up a windows scheduled task to run the Python script without needing to open a terminal. 
- And the `delete_task.bat` to remove the scheduled task. 

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue. Any suggestions or improvements are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.