with open("apache.log") as log_file:
    for line in log_file:
        fields = line.split()
        print(f"IP Address: {fields[0]} Time: {fields[3]} {fields[4]}")
