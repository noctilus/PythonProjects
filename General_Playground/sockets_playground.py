import socket

# SERVER PART ###
# specifying AF_INET = IP4
# specyfying SOCK_STREAM = TCK protocol
# socket.SOCK_DGRAM = UDP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8000

# By binding the server to a port, we prepare it for receiving data

server.bind((SERVER_IP, SERVER_PORT))

# to actually listen for incoming connections

server.listen(0)
# 0is called backlog, number of connections
# can be put on hold before calling server.accept() on them
print(f"Server accepting connections on ,{SERVER_IP}:{SERVER_PORT}")

# accepting incoming connections is done by:
client_socket, client_address = server.accept()
# when accepted, the accept() method returns tuple on (conn,address)
# ACHTUNG: address is a tuple of client's IP and port,
# and conn is a new socket object to communicate with client!
# accept() creates a new socket to release the bind() port
# for other connections
print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
