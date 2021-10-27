# Order of objects in lists: completions, attempts, yards, touchdown, interceptions, rating

game_log = [
    [27, 36, 337, 3, 3, 131.4],
    [24, 31, 343, 3, 3, 131.5],
    [27, 44, 260, 3, 3, 81.6],
    [27, 30, 278, 5, 5, 131.0],
    [33, 54, 272, 2, 2, 70.9],
    [32, 47, 397, 2, 2, 90.5],
    [20, 35, 206, 0, 1, 62.3],
]

print("\t\tCMP\tATT\tYDS\t\tTD\tINT\tRTG")  # Print the column label
for game_number, game in enumerate(game_log):
    print(f"Game {game_number}", end=' ')  # Print the row label
    for stat in game:
        print(f"\t{stat}", end=' ')

    print()  # Print a newline


