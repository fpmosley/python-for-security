import socket

sock = socket.socket()

try:
    sock.connect(("127.0.0.1", 4444))

    while True:
        send_data = input("Message to server: ")
        sock.send(send_data.encode())

        recv_data = sock.recv(2048).decode()
        print(f"Message from server: {recv_data}\n")

        if recv_data == 'exit':
            print("Connection closed by the server.\n".encode())
            sock.close()
            break

except Exception as e:
    print(f"Error: {e}")

sock.close()
