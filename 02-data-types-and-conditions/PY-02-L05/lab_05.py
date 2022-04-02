ip_address = input("Please enter an IP address: ")

ip_octets = ip_address.split(".")

print(f"IP Octets: {ip_octets}")

first = int(ip_octets[0])
second = int(ip_octets[1])
third = int(ip_octets[2])
fourth = int(ip_octets[3])

print(f"{first:>3} : {bin(first)[2:]:0>8}")
print(f"{second:>3} : {bin(second)[2:]:0>8}")
print(f"{third:>3} : {bin(third)[2:]:0>8}")
print(f"{fourth:>3} : {bin(fourth)[2:]:0>8}")
