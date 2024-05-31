import socket

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
            log_file = open("temp.logs", "a", encoding="utf-8")
            try:
                data_to_write = f"{data.decode()}\n"
                log_file.write(data_to_write)
                conn.sendall(data)
                s.close()
            except UnicodeError as e:
                print(f"{e} \n")
                pass