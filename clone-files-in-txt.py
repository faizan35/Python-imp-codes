import os

def write_files_to_output(directory, output_dir):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Skip .css files
            # if filename.endswith('.css'):
            #     continue

            filepath = os.path.join(foldername, filename)
            try:
                with open(filepath, 'r') as file:
                    content = file.read()

                # Calculate the relative path without the base directory
                relative_path = os.path.relpath(foldername, directory)
                output_subdir = os.path.join(output_dir, relative_path)
                os.makedirs(output_subdir, exist_ok=True)

                # Write content to a separate file in the output directory
                output_filepath = os.path.join(output_subdir, f"{filename}_output.txt")
                with open(output_filepath, 'w') as out:
                    out.write(f"Filename: {filename}\n")
                    out.write(f"Filepath: {os.path.join(relative_path, filename)}\n")
                    out.write(f"Content:\n{content}\n")
                    out.write("=" * 50 + "\n")
            except Exception as e:
                print(f"Could not read file {filepath} due to {e}")

if __name__ == "__main__":
    dir_to_search = r'paste-your-path-here'
    output_directory = r'paste-your-output-path-here'
    write_files_to_output(dir_to_search, output_directory)
    print(f"Output written to {output_directory}")
