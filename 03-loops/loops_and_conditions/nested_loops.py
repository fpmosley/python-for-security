print("\t2\t4\t6\t8\t10")  # Print the column label
for row in range(1, 11):
    print(f"{row}", end=' ')  # Print the row label
    for column in [2, 4, 6, 8, 10]:
        print(f"\t{row * column}", end=' ')  # Print the result on the same line
    print()  # Print a newline
