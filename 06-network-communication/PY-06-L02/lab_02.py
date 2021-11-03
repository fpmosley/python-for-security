import socket
import time

my_sock = socket.socket()
my_sock.connect(("127.0.0.1", 4444))

time.sleep(5)

my_sock.close()
