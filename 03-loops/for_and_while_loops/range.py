upper_bound = int(input("Please provide an upper bound for the range: "))

for i in range(upper_bound):
    print(f"{i}", end=" ")
print()

upper_bound = int(input("Please provide an upper bound for the range: "))
step = int(input("Please provide a step for the range: "))
for i in range(0, upper_bound, step):
    print(f"{i}", end=" ")
print()

upper_bound = int(input("Please provide an upper bound for the range: "))
lower_bound = int(input("Please provide a lower bound for the range: "))
step = int(input("Please provide a step for the range: "))
for i in range(lower_bound, upper_bound, step):
    print(f"{i}", end=" ")
print()
