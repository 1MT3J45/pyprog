import socket,fact
s = socket.socket()
# Create a socket object
host = socket.gethostname() # Get local machine name
port = 1243 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port
s.listen(5) # Now wait for client connection.
while True:
	print "Waiting for connection..."
	c, addr = s.accept()
	# Establish connection with client.
	print 'Got connection from', addr
	t = c.recv(10)
	c.send(t.upper())
	c.close()
	# Close the connection
