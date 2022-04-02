import json

service_ports = {}

while True:  # The logic 'service != "0" and port != "0"' is not necessary. "while True" is simpler and easier to read.
    service = input("Please enter a service name or type '0' to stop: ")
    if service == "0":
        break

    port = input("Please enter a port number or type '0' to stop: ")
    if port == "0":
        break

    service_ports[service] = port

print(json.dumps(service_ports, sort_keys=False, indent=4))  # Added json.dumps to pretty print the dictionary
