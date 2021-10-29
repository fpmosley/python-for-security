number_str = input("Enter a number: ")

try:
    number = int(number_str)
except:
    print(f"User didn't enter a valid number: {number_str}.")
else:
    print(f"User entered a valid number: {number_str}")
finally:
    print("This executes every time.")
