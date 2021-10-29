class CustomError(Exception):
    pass


for i in range(5):
    try:
        if i == 4:
            raise CustomError("Iterator is 4")
    except CustomError as e:
        print(e)
