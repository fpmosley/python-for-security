def welcome(email, full_name=None):
    if full_name:
        print(f"Hi {full_name}, welcome to our site.")
    else:
        print("Name is required...Logging off.")


name = input("Please enter your full name: ")
welcome('test@gmail.com', name)
