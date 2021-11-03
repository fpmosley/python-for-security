import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 4321))
print(sock.recv(2048).decode())
sock.send(input("").encode())
print(sock.recv(2048).decode())
sock.send(input("").encode())
print(sock.recv(2048).decode())

sock.close()
