import os
import sys

def rename_files_with_prefix(directory_path):
    try:
       
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a directory.")
        files = os.listdir(directory_path)
        
        for i, filename in enumerate(files, start=1):
            old_path = os.path.join(directory_path, filename)
            new_filename = f"file{i}.{filename.split('.')[-1]}"  
            new_path = os.path.join(directory_path, new_filename)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = sys.argv[1]
    rename_files_with_prefix(directory_path)



#/Users/stefanbodescu/Desktop/pr_python/