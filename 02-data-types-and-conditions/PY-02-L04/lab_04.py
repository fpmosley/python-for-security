protocols_dict = {
    'FTP': '21',
    'DNS': '53',
    'LDAP': '389',
    'MySQL': '3306',
}

question = input("For which protocol would you like to know the port number? ")

if question in protocols_dict.keys():
    answer = protocols_dict[question]
    print(f"The port number for protocol '{question}' is: {answer}")
else:
    print("The protocol cannot be found")

# Alternative method of retrieving the value of the key using get() method.
# Use "get()" method to avoid the KeyError. Returns a 'None' type if the key doesn't exist.
answer = protocols_dict.get(question)
if answer:  # if answer is type None, then the condition will result in 'False'
    print(f"The port number for protocol '{question}' is: {answer}")
else:
    print("The protocol 'ssh' cannot be found")
