file_write = open("close.txt", "w")
file_write.write("This is the first sentence.\n")
file_write.flush()

file_read = open("close.txt", "r")
print(file_read.read())
