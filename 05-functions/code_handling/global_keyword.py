def change_name(name):
    global input_name
    print(f"Name to change: {name}")
    input_name = name[:1]


input_name = input("Enter a first name: ")
change_name(input_name)
print(f"Input name: {input_name}")
