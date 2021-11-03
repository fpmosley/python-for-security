import socket

try:
    sock = socket.socket()
    sock.bind(("0.0.0.0", 4444))
    sock.listen()
    conn, addr = sock.accept()
    data = b''
    buffer_size = 2048

    while True:
        recv_data = conn.recv(2048).decode()
        print(f"Message from client: {recv_data}\n")

        conn.send("Message received.\n".encode())

        if recv_data == 'exit':
            conn.send("Connection closed by the client.\n".encode())
            sock.close()
            break
except Exception as e:
    print(e)
