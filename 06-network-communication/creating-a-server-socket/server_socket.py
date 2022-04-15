import socket

sock = socket.socket()
sock.bind(("0.0.0.0", 4444))  # Bind to all network interfaces
print("Listening on port 4444")
sock.listen()
conn, addr = sock.accept()

print(f"Accepted a connection from IP: {addr[0]} Port: {addr[1]}")

sock.close()
