try:
    with open("text.txt", "r") as text:
        text.write("Test")
except FileNotFoundError:  # FileNotFoundError
    print("Unsupported operation; can't write in read mode.")
