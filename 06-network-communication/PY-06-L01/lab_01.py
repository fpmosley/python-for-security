import socket

my_sock = socket.socket()
my_sock.bind(("0.0.0.0", 4444))
my_sock.listen(1)
connection, address = my_sock.accept()
print(f"Connection: {connection} Address: {address}")
my_sock.close()
