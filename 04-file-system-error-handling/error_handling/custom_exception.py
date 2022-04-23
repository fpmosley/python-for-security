class CustomError(Exception):
    pass


while True:
    try:
        user_input = int(input("Please enter a number between 1 and 100: "))
        if user_input < 1 or user_input > 100:
            raise CustomError("Please enter a number between 1 and 100.")
    except CustomError as e:
        print(e)
    except ValueError as e:
        print(e)
