# file_path = "./text2.txt"
file_path = "./text.txt"
try:
    open(file_path, "r")
    print("File found")
except FileNotFoundError:
    print("File not found")
