```
markdown
# Advanced File Organizer & Sorter

A robust Python utility designed to automatically sort all files within a specific directory into subfolders based on their file extension. The tool ensures data integrity by generating unique random names for every file before moving it.

## ⚡ Features

- **Smart Sorting**: Automatically detects file extensions and creates corresponding subdirectories (e.g., `.txt`, `.jpg`, `.pdf`).
- **Secure Renaming**: Generates cryptographically safe-looking random alphanumeric strings (length 1–7) to prevent naming conflicts.
- **Self-Protection**: Intelligent safety checks detect if the script resides within the target folder. It automatically skips its own execution and protects other critical scripts from being deleted or renamed incorrectly.
- **Extension Preservation**: Ensures the final filename always follows the strict format `RandomString.extension`.
- **Error Handling**: Gracefully handles permission errors, missing paths, and symbolic links without crashing.

## 🛠️ Prerequisites

No external libraries are required. This script relies solely on Python's standard library modules:
- `os`
- `shutil`
- `random`
- `string`
- `sys`

**Python Version:** Compatible with Python 3.x

## 📥 Installation

1. Clone or download the script (e.g., `file_organizer.py`) to your machine.
2. Open a terminal or command prompt.
3. Run the script using Python:
```

bash python file_organizer.py

```

> **Note**: Ensure you have write permissions for the directory you intend to organize.

## 🚀 Usage

### Step-by-Step Execution

1. **Launch the Script**:
```

bash   python file_organizer.py   

```

2. **Enter Directory Path**:
   When prompted, type the full absolute path of the folder you want to organize.
   *Example*: `C:\Users\YourName\Documents\MixedFiles` or `/home/user/Downloads`

3. **Confirm Action**:
   The script will display a warning stating that files will be moved permanently. Type `y` and press Enter to proceed.

4. **Execution**:
   - The script scans the directory for unique extensions.
   - It creates subfolders named with dots preceding the extension (e.g., `.txt`).
   - Files are moved into their respective folders and renamed.
   - The original location is cleared once processing is complete.

### Example Output

If your input directory contains:
- `report.pdf`
- `image.jpg`
- `data.csv`

The script will create:
```

text 📁 .pdf/   📄 aB9x2.pdf 📁 .jpg/   📄 kL4m1.jpg 📁 .csv/   📄 pQ7r8.csv

```

## 🔒 Safety & Security Measures

This script includes multiple layers of protection to prevent accidental data loss or system corruption:

- **Script Self-Protection**: If `file_organizer.py` is located inside the target folder, it triggers a critical warning and pauses execution until user confirmation, preventing self-deletion.
- **General Script Protection**: All files ending in `.py` containing keywords like "sorter" or "script" are automatically skipped to avoid breaking other automated tools stored in the same location.
- **Path Validation**: Verifies that the provided path exists and is actually a directory before attempting any operations.
- **Atomic Operations**: Uses standard OS file moving functions (`shutil.move`) which handle cross-folder transfers safely within the same drive.

## ⚠️ Warnings

- **Irreversible Changes**: Once executed, the script moves files permanently. There is no undo function within the script itself. **Always backup important data** before running bulk file operations.
- **No Preview**: The current version processes files immediately upon confirmation. No preview mode is available yet.
- **Drive Constraints**: Files can only be moved between subdirectories on the same drive/partition as the source. Cross-drive moves require manual intervention.

## 🐛 Troubleshooting

| Issue | Possible Cause | Solution |
|-------|----------------|----------|
| `PermissionError` | Lack of read/write access | Run terminal with administrator/root privileges. |
| Script refuses to start | Invalid Python environment | Ensure you have an active Python 3 installation. |
| Files not sorted correctly | Mixed extension formats | The script handles both `file.ext` and `file`.ext inputs uniformly. |
| Recursion Loop Detected | Script included its own logic incorrectly | Check the "Self-Protection" section; ensure filenames don't contain common triggers like 'sorter'. |

## 📄 License

This project is open-source and free to use for personal and commercial purposes.

---

*Developed for efficient digital organization.*
```