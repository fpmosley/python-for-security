tup = (1, 2, 3)
print(f"Tuple: {tup}")
print(f"tup[0]: {tup[0]}")     # => 1

#tup[0] = 3

try:
    tup[0] = 3
except (ValueError, TypeError) as e:
    print(f"Tuples are immutable: {e}")

print("Got to the end of the program.")
