car = dict()  # Creates an empty dictionary; Could also create with "car = {}"

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
car["make"] = "Tesla"
car["model"] = "Model S"
car["color"] = "red"
car["year"] = "2020"

print(f"Here is your 'car': {car}")
print(f"Data type for variable 'car': {type(car)}")

# Create a prefilled dictionary
# Note: Can also be in a single line: {'make': 'Audi', 'model': 'A7', 'color': 'black', 'year': '2021', 'mileage': 3000}
another_car = {
    'make': 'Audi',
    'model': 'e-tron GT',
    'color': 'black',
    'year': '2021',
    'mileage': 3000
}  # Prefilled dictionary

print(f"Here is 'another_car': {another_car}")

# Change the model
if 'model' in another_car.keys():
    another_car['model'] = "A7"
    print(f"Here is a different model 'another_car': {another_car}")
    print(f"The car model for 'another_car': {another_car['model']}")

# Delete the mileage
del another_car['mileage']
if 'mileage' not in another_car.keys():
    print(f"'another_car' without the mileage: {another_car}")
