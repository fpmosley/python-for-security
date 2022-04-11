file_write = open("close.txt", "w")
file_write.write("This is the first sentence.\n")
file_write.close()  # What happens if we didn't close the file?

file_read = open("close.txt", "r")
print(file_read.read())
