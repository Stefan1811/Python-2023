import os
import sys

def read_print_files(directory_path,extension):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError
        
        if not os.path.isdir(directory_path):
            raise NotADirectoryError
        
        for file in os.listdir(directory_path):
                if file.endswith(extension):
                    f_path=os.path.join(directory_path, file)
                    try:
                      with open(f_path, 'r') as file:
                        contents = file.read()
                        print(f"Contents of {file}:\n{contents}\n")
                    except Exception as e:
                        print(f"Error reading file '{file}': {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__=="__main__":
    directory_path=sys.argv[1]
    extension=sys.argv[2]
    read_print_files(directory_path,extension)