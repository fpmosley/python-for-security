message = "Welcome %s to class number %d!" % ("Python students", 2)
print("This is the % type of string formatting. Original string formatting type.")
print(message)

message = "Welcome {} to class number {}!".format("Python students", 2)
print("\nThis is style of formatting was introduced in Python students 2.6.")
print(message)

cohort = "Python students"
class_number = 2
message = f"Welcome {cohort} to class number {class_number}!"
print("\nf-strings are the preferred way of string formatting. First introduced in Python students 3.6.")
print(message)
