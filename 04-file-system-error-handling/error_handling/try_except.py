tup = (1, 2, 3)
print(f"Tuple: {tup}")
print(f"tup[0]: {tup[0]}")     # => 1

#tup[0] = 3

try:
    tup[0] = 3
except (TypeError, ValueError) as foo:
    print(f"Tuples are immutable: {foo}")

print("Got to the end of the program.")
