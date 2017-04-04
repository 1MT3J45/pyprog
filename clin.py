import socket # Import socket module
s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1243

# Reserve a port for your service.
s.connect((host, port))
st = raw_input("Enter the string: ")
s.send(st)
print "Upper is: ", s.recv(10)
s.close
# Close the socket when done
