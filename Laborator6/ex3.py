import os
import sys

def total_size_directory(directory_path):
    total_size=0
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError
        
        if not os.path.isdir(directory_path):
            raise NotADirectoryError
        for root, dirs, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    total_size += os.path.getsize(file_path)
                except Exception as e:
                    print(f"Error accessing file '{file_path}': {e}")
        print(f"Total size of all files in '{directory_path}': {total_size} bytes")

    except Exception as e:
        print(f"Error: {e}")
    
if __name__=="__main__":
    directory_path=sys.argv[1]
    total_size_directory(directory_path)
        