print("Demo of the 'continue' command within a 'for' loop.")
print("Printing even numbers from 1-100.")
for i in range(1, 101):
    if not i % 2 == 0:
        continue
    else:
        print(i, end=' ')
