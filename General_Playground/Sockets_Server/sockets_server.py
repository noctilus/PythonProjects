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
            # data_to_write = data.decode(encoding="utf-8")
            data_to_write = f"({data.decode}\n)"
            if "machine_id" not in data_to_write:
                break
            log_file = open("temp.logs", "a", encoding="utf-8")
            try:
                print(data_to_write)
                log_file.write(data_to_write)
                conn.sendall(data)
                s.close()
            except UnicodeError as e:
                print(f"{e} \n")
            except KeyboardInterrupt as e:
                print(" Keyboard exit.")
                sys.exit()
            except ConnectionError as e:
                print(f"{e} \n, Connection error")
            except Exception as e:
                print(f"{e} \n, General catch all Exception")
