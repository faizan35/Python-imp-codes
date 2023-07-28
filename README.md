# Python Codes

## Contents

- [Python Codes](#python-codes)
  - [Contents](#contents)
  - [Clone Files Script - `clone-files-in-txt.py`](#clone-files-script---clone-files-in-txtpy)
    - [Usage](#usage)
  - [Print Directory Structure Script - `print-dir-structure.py`](#print-directory-structure-script---print-dir-structurepy)
    - [Usage](#usage-1)

## Clone Files Script - `clone-files-in-txt.py`

This script recursively clones files in a directory to a specified output directory. It reads the content of each file and writes it to a separate text file in the output directory.

#### Usage

1. Replace `'paste-your-path-here'` and `'paste-your-output-path-here'` with the actual paths.
2. Uncomment the line to skip `.css` files if needed.
3. Run the script:

   ```bash
   python clone-files-in-txt.py
   ```

## Print Directory Structure Script - `print-dir-structure.py`

This script prints the directory structure in a tree-like format. It uses box-drawing characters for better visualization and handles `PermissionError` while listing directory entries.

#### Usage

1. Replace `'paste-your-path-here'` with the actual root directory path.
2. Run the script:

   ```bash
   python print-dir-structure.py
   ```

Make sure to have the necessary permissions for the specified directories.
