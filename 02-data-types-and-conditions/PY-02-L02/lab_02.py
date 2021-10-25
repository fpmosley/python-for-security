name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello {}, your age is {}".format(name, age))
print(f"Hello {name}, your age is {age}")  # Can also print the message as an f-string

if age >= 21:
    print("You can buy an alcoholic beverage")
else:
    print("You cannot buy an alcoholic beverage")
