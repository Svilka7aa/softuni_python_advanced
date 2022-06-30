from os import remove
from os.path import exists

file_path = "./files/my_first_file.txt"
# open(file_path, "w").close
if exists(file_path):
    remove(file_path)
    print("File deleted")

else:
    print('File already deleted!')

# file = open(file_path, "W").close