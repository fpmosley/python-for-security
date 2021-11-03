import socket

sock = socket.socket()
sock.bind(("0.0.0.0", 45000))
sock.listen(1)

conn, addr = sock.accept()

conn.send("Welcome to the server!".encode())

print(conn.recv(2048).decode())

sock.close()
