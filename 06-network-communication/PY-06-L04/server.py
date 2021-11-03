import socket

sock = socket.socket()
sock.bind(("0.0.0.0", 4321))
sock.listen(1)

conn, addr = sock.accept()

conn.send("Welcome to the server!\nPlease insert your Username: ".encode())
username = conn.recv(2048).decode()

conn.send("Please insert the Password: ".encode())
password = conn.recv(2048).decode()

if username == "John" and password == "12345":
    conn.send(f"Welcome {username}".encode())
else:
    conn.send(f"Wrong username or password".encode())

sock.close()
