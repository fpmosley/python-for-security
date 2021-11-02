def welcome(full_name, email):
    return f"Welcome {full_name}, your email address is {email}."


name = input("Please enter your full name: ")
email = input("Please enter your email address: ")
message = welcome(name, email)
print(message)
