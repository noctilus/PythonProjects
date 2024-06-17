import json
import socket
import sys
import time

HOST = "0.0.0.0"
PORT = 9000
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Don't block the socket after creating it
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
            received_timestamp = time.time_ns()
            try:
                # Can't use with open(): because there's a problem with
                # Error handling later on.
                log_file = open("temp.logs", "a", encoding="utf-8")
                # decode received data from bytes to string
                decoded_data = data.decode(encoding="utf-8")
                # decode string to json object
                decoded_data = json.loads(decoded_data)
                decoded_data.update({"received_timestamp": received_timestamp})
                decoded_data.update({"sensor_ip": addr[0]})
                print(decoded_data)
                # format the json object to write to file and write
                data_to_write = f"({decoded_data}\n)"
                log_file.write(data_to_write)
                log_file.close()
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
