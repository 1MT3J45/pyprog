import socket
import time
s = socket.socket()
host = socket.gethostname()
port = 1271
s.bind((host,port))
s.listen(5)
while True:
	c, addr = s.accept()
	print 'Got connection from ', addr
	contents = time.asctime()
	c.send(str(contents))
	c.close()
	
