file = open("write.txt", "w")
file.write("This is the first sentence.\n")
file.close()

file = open("write.txt", "a")
file.write("This is the second sentence.\n")
file.close()

file = open("write.txt", "r")
print(file.read())
file.close()
