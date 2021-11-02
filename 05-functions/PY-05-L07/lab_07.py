import os
import sys

line = "<----------------------------------------------------------->"
system = sys.platform
print(f"You are using {system}")

root_folder = input("Enter folder: ")


def mapper(path):
    try:
        for item in os.listdir(path):
            full_path = fr"{path}/{item}"
            if os.path.isfile(full_path):
                size = os.stat(full_path).st_size
                print(f"Found {full_path} - size {size} bytes")
            elif os.path.isdir(full_path):
                print(f"{line}\nEntering folder {item}\n{line}")
                mapper(full_path)
            else:
                print("Unknown.")
    except Exception as error:
        print(error)


mapper(root_folder)
