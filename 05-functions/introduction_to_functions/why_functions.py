try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    operator = input("Please enter one of the following operators: +, -, *, /, **, %, area: ")

    if operator == '+':
        description = f"{num1} + {num2}"
        print(f"The result of {description} = {num1 + num2}")
    elif operator == '-':
        description = f"{num1} - {num2}"
        print(f"The result of {description} = {num1 - num2}")
    elif operator == '*':
        description = f"{num1} * {num2}"
        print(f"The result of {description} = {num1 * num2}")
    elif operator == '/':
        description = f"{num1} / {num2}"
        print(f"The result of {description} = {num1 / num2}")
    elif operator == '**':
        description = f"{num1} ** {num2}"
        print(f"The result of {description} = {num1 ** num2}")
    elif operator == '%':
        description = f"{num1} % {num2}"
        print(f"The result of {description} = {num1 % num2}")
    elif operator == 'area':
        description = f"{num1} * {num2 ** 2}"
        print(f"The result of {description} = {num1 * (num2 ** 2)}")
    else:
        print(f"The operator '{operator}' doesn't exist.")
except ValueError:
    print("Please enter a number.")
except KeyError:
    print(f"The operator '{operator}' doesn't exist.")
except ZeroDivisionError:
    print("Can't divide by 0.")
