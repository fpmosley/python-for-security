li = [] # an empty list

another_list = [4, 5, 6]  # a list initialized with values

li.append(1)  # insert a value into the first index
print(f"List: {li}")

li.append(2)  # insert a value into the next index
li.append(3)  # insert a value into the next index
print(f"List: {li}")

value = li[0]
print(f"Value of first index of list (li[0]): {value}")
value = li[2]
print(f"Value of third index of list (li[2]): {value}")

del li[2]
print(f"List after removing third index: {li}")

li.append(3)  # insert a value into the next index

print(f"List: {li}")
print(f"Another List: {another_list}")

concatenated_list = li + another_list  # Note: values for "li" and for "another_li" are not modified.
print(f"Concatenated List: {concatenated_list}")

# Can also use the extend function to concatenate two lists (or another iterable) 
li.extend(another_list) # Using the extend() method will modify "li"
print(f"Concatenated List (using extend()): {li}")

# Replacing values
li[0] = 0
li[1] = 0
li[2] = 0
li[3] = 0
li[4] = 0
li[5] = 0
print(f"List after replacing every index with '0': {li}")

# Mixing data types
li[0] = 0
li[1] = "a"
li[2] = 1
li[3] = "b" 
li[4] = 2
li[5] = "c" 
print(f"List with mixed data types: {li}")
