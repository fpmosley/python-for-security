import socket

sock = socket.socket()

try:
    sock.connect(("127.0.0.1", 4444))
except Exception as e:
    print(f"Error: {e}")

sock.close()
