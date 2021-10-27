tup = (1, 2, 3)
tup[0]  # => 1
tup[0] = 3  # Raises a TypeError

# Use pass in exception handling
try:
  tup[0] = 3  # Raises a TypeError
except TypeError:
  pass

# Use pass in if...elif chains
for x in range(100):
    if x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")
    else:
        print(x)


# Use pass in future code
def future_function(result):
    pass


def present_function():
    print('''Example of code I'm currently developing. This code calls 'future_function' which I haven't written yet.
    So I'll put in a pass statement as a placeholder in the function. This is so I can continue developing and
    testing my 'present_function'.''')
    result = 1 + 2
    future_function(result)
    return


present_function()
