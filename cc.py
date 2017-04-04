import socket
import time
s = socket.socket()
host = socket.gethostname()
port = 1271
s.connect((host, port))
print "Time is : ", s.recv(1000)
s.close()
