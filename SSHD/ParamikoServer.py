# Create an SSH server
class MySSHServer(paramiko.ServerInterface):
    """Server instance creation"""

    def check_auth_password(self, username, password):
        # Implement your own authentication logic here
        # For demonstration purposes, allow any user with any password
        print(username, password)
        return paramiko.AUTH_SUCCESSFUL

    def get_allowed_auths(self, username):
        return username


# Set up the server
host_key = paramiko.RSAKey.generate(bits=2048)
server = paramiko.Transport(("0.0.0.0", 22))
server.add_server_key(host_key)

# Set the server to use our custom handler
server.start_server(server=MySSHServer())

print("SSH server listening on port 22...")

# Accept connections
while True:
    channel, addr = server.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    channel.close()

# Remember to handle exceptions and cleanup properly in a real-world scenario!
