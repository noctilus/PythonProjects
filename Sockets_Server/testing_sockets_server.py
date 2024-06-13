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
    with conn:
        print(f"Connected from {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data_to_write)
            conn.sendall(data)
            conn.close()
