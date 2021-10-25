import json  # imported for pretty printing purposes

# Nested data structure
# Contains a nested list of dictionaries inside of a dictionary
car = {
    'make': 'Audi',
    'model': 'S5',
    'color': 'white',
    'year': '2019',
    'mileage': 40000,
    'owners': [
        {
            'first_name': 'Franklin',
            'last_name': 'Mosley',
            'year': 2019
        },
        {
            'first_name': 'Samuel',
            'last_name': 'Jackson',
            'year': 2020
        },
    ]
}

print(f"Here is the nested data structure 'car': {json.dumps(car, sort_keys=False, indent=4)}\n")

# Adding a new owner
new_owner = {
    'first_name': 'Tom',
    'last_name': 'Cruise',
    'year': 2021
}

car['owners'].append(new_owner)

print(f"Added a new owner (Tom Cruise) 'car': {json.dumps(car, sort_keys=False, indent=4)}")
