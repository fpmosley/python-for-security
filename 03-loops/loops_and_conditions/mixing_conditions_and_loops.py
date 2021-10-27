numbers = [17, 98, 87, 40, 93, 69, 59, 87, 140, 82] 

for number in numbers:
    if number > 100:
        break
    elif number % 2 == 0 and number % 4 == 0:
        print(f"Number '{number}' is even and a multiple of 4")
        continue
    elif number % 2 == 0:
        print(f"Number '{number}' is even")
        continue
    elif number % 3 == 0:
        print(f"Number '{number}' is a multiple of 3")
