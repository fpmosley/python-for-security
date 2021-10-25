structure = [
    {
        'Arizona': 'Phoenix',
        'California': 'Sacramento',
        'Hawaii': 'Honolulu'
    },
    5000,
    6000,
    7000,
    ['hat', 't-shirt', 'jeans']
]

# Print '5000'; 1st index of the 'structure' list
print(structure[1])

# Print the dictionary of states; 0 index of the 'structure' list
print(structure[0])

# Print the list of clothes; 4th index of the 'structure' list
print(structure[4])

# Print the word 'Phoenix'; 'Arizona' key of the dictionary at the 0 index of the 'structure' list
print(structure[0]['Arizona'])

# Print the word 'jeans'; 4th index of the 'structure' list and 2nd index of the sublist
print(structure[4][2])

# Delete the value 7000
del(structure[3])
print(f"Deleted the value '7000': {structure}")
