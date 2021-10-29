path = input("Enter a directory path for the text file: ")
filename = input("Enter filename: ")
with open(f"{path}/{filename}", "r") as file:
    for line in file:
        print(line)
