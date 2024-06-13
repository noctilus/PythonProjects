import socket

HOST = "141.95.127.166"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Helo World!")
    data = s.recv(1024)

print(f"received,{data!r}")
