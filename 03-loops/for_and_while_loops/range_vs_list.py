linux_distros = ['Ubuntu', 'Debian', 'Red Hat', 'Fedora', 'Alpine', 'Kali', 'Parrot']

print("Example of iterating over an iterable.")
for linux_distro in linux_distros:
    print(f"Linux Distro: {linux_distro}")

print("\nExample of iterating over a range.")
for index in range(len(linux_distros)):
    print(f"Linux Distro at index {index}: {linux_distros[index]}")

print("\nExample of iterating using enumerate().")
for index, linux_distro in enumerate(linux_distros):
    print(f"Linux Distro at index {index}: {linux_distro}")

movie = {
    'Name': 'Goodfellas',
    'Year': 1990,
    'Director': 'Martin Scorsese',
    'Cast': ['Ray Liotta', 'Robert De Niro', 'Joe Pesci'],
}

print("\nExample of iterating over a dictionary (returns keys in the dictionary)")
for item in movie:
    print(item)

print("\nExample of iterating over a dictionary with values()")
for value in movie.values():
    print(f"Movie values: {value}")

print("\nExample of iterating over a dictionary with keys()")
for key in movie.keys():
    print(f"Movie key: {key} value: {movie[key]}")

print("\nExample of iterating over a dictionary with items()")
for key, value in movie.items():
    print(f"Movie key: {key} value: {value}")
