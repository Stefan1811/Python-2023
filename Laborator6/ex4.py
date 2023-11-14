import os
import sys

def count_files_by_extension(directory_path):
    extension_counts = {}

    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a directory.")

        files = os.listdir(directory_path)

        if not files:
            print(f"The directory '{directory_path}' is empty.")
            return

        for filename in files:
           
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension[1:]
            extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        print(f"File counts in '{directory_path}':")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = sys.argv[1]
    count_files_by_extension(directory_path)
