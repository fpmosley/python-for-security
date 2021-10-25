grade = int(input("Enter a grade: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 65:
    print("D")
elif grade >= 0:
    print("F")
else:
    print("ERROR: Grades cannot be negative numbers or words.")

'''
The code above will generate an error if the user enters a value that cannot
be cast to an integer. A 'ValueError' exception will be thrown.
This commented out code shows how you could make your code
resilient to that exception being thrown and exit gracefully by using a
"try/except" block. This gets discussed in the "File System & Error Handling"
module.

import sys

try:
    grade = int(input("Enter a grade: "))
    
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 65:
        print("D")
    elif grade >= 0:
        print("F")
    else:
        print("ERROR: Grades cannot be negative numbers or words.")
except ValueError as e:
    print("Cannot cast the grade entered to an integer.")
    sys.exit()
'''
