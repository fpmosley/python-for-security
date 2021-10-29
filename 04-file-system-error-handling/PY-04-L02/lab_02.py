product = 1
for i in range(4):
    try:
        num = int(input("Enter a number: "))
        product *= num
    except:
        print("The input is not a valid number")
print(f"The product of the 4 numbers is: {product}")
