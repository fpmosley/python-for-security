import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 45000))
print(sock.recv(2048).decode())

sock.send("Thanks!".encode())

sock.close()
