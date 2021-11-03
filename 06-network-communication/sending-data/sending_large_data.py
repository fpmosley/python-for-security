import socket

sock = socket.socket()
sock.bind(("0.0.0.0", 4444))
sock.listen()
conn, addr = sock.accept()
data = b''
buffer_size = 2048

while True:
    packet = conn.recv(2048)
    data += packet
    print(f"Recv: {packet.decode()}\nSize:{len(packet)}")
    if len(packet) < buffer_size:
        print("All data received")
        break
    else:
        conn.send("Waiting on more data.\n".encode())

sock.close()
