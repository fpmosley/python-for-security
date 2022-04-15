import socket

sock = socket.socket()
sock.bind(("0.0.0.0", 4444))

sock.listen()

conn, addr = sock.accept()
data = conn.recv(2048).decode()  # Buffer size set to power of 2 (2^11); 2048 bytes

print(f"Accepted a connection from IP: {addr[0]} Port: {addr[1]}")
print(f"Message length: {len(data)}")
print(f"Received message: {data}")

sock.close()
