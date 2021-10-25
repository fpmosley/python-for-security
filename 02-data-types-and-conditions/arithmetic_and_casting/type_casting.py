age = input("How old are you? ")
age = int(age)

# Alternative way is to nest the input() inside the int(); this would eliminate lines 1-2
# age = int(input("How old are you? "))

print(f"Age is type: {type(age)}")

if age >= 21:
    print("Old enough to purchase.")
elif age > 18:
    print("Almost old enough to purchase.")
else:
    print("Come back in a few years.")

print()

# Cast age to a float data type
age = float(age)
print(f"Age: {age}")
print(f"Age is type: {type(age)}")
