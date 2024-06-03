import socket
import sys

HOST = "0.0.0.0"
PORT = 9000

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    first_transmission = b"SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.7"
    with conn:
        print(f"Connected from {addr}")
        print(conn)
        while True:
            conn.send(first_transmission)

            conn.send(b"Login:")
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.sendall(b"Password:")
            data_pass = conn.recv(1024)
            if not data:
                break
            print(data_pass)
            conn.sendall(b"Access denied")
            s.close()
