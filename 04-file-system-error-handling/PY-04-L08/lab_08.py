import os

try:
    os.mkdir(r"/tmp")
except:
    print("This directory already exists.")

with open(f"/tmp/test.txt", "a+") as file:
    pass

path = input("Enter a directory path: ")
file_name = input("Enter file name: ")
new_file_name = input("Enter a new name: ")

os.system(fr"cp {path}/{file_name} {path}/{new_file_name}")  # using a raw f-string
