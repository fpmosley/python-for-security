import socket

sock = socket.socket()

try:
    sock.connect(("127.0.0.1", 4444))
    sock.send("This is a message from the client\n".encode())  # Message encoded to a bytes object (UTF-8)
except Exception as e:
    print(f"Error: {e}")

sock.close()
