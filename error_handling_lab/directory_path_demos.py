import time
from os import mkdir, rmdir, listdir


directory_path = "./"
mkdir("./dir_to_delete")
time.sleep(5)
rmdir("./dir_to_delete")


print(listdir(directory_path))
