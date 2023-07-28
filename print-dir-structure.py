
import os

def print_dir_structure(root_dir, indent="", last=True):
    """
    Print the directory structure in a tree-like format starting from the given root directory.

    Parameters:
        root_dir (str): The root directory to start printing from.
        indent (str): The current level of indentation for better visualization.
        last (bool): True if the current directory is the last one in the list, False otherwise.
    """
    print(indent, end="")
    
    if last:
        print("└─ ", end="")
        new_indent = indent + "   "
    else:
        print("├─ ", end="")
        new_indent = indent + "│  "
    
    print(os.path.basename(root_dir))

    try:
        entries = os.listdir(root_dir)
        entries.sort()  # Sort entries to maintain consistent order
        for i, entry in enumerate(entries):
            entry_path = os.path.join(root_dir, entry)
            is_last = (i == len(entries) - 1)
            if os.path.isdir(entry_path):
                print_dir_structure(entry_path, new_indent, is_last)
            else:
                print(new_indent, end="")
                print("└─ " if is_last else "├─ ", end="")
                print(entry)
    except PermissionError as e:
        print(new_indent + f"PermissionError: {e}")

if __name__ == "__main__":
    root_directory = r'paste-your-path-here'
    
    if os.path.isdir(root_directory):
        print_dir_structure(root_directory)
    else:
        print("Invalid directory path. Please enter a valid directory.")
