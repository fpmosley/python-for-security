print("Demo of the 'break' command within a 'for' loop.")
for i in range(1, 101):
    print(i, end=' ')
    if i == 50:
        break
print("The loop was exited.")

print("\nDemo of the 'break' command within a 'while' loop.")
counter = 1
while counter <= 100:
    print(counter, end=' ')
    if counter == 10:
        break

    counter = counter + 1  # Can also write as "counter += 1"

print("The loop was exited.")
