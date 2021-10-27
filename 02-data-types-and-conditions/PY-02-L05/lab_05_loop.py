ip_address = input("Please enter an IP address: ")

ip_octets = ip_address.split(".")

print(f"IP Octets: {ip_octets}")
for ip_octet in ip_octets:  # Implemented the lab with a for loop; Taught in the next class on Loops
    print(f"{ip_octet:>3} : {bin(int(ip_octet))[2:]:0>8}")
