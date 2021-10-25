print(f"True or True:      {True or True}")
print(f"True or False:     {True or False}")
print(f"False or False:    {False or False}")
print(f"False or True:     {False or True}")

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

if first_name == "Franklin" or last_name == "Mosley":
    print("You have a first name of 'Franklin' or a last name of 'Mosley'")
else:
    print("Imposter!")
