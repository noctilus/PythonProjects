import datetime
import json
import random
import socket

HOST = "141.95.127.166"
PORT = 9000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    temp = random.randrange(1, 30)
    press = random.randrange(890, 1024)
    MACHINE_ID = "083a72ac7060"
    timestamp = str(datetime.datetime.now())
    # Formulating dict{} from data provided by sensors and device
    data_to_send = {
        "press": press,
        "temp": temp,
        "machine_id": MACHINE_ID,
        "timestamp": timestamp,
    }
    # serializing data from dict{} to json object
    data_to_send_json = json.dumps(data_to_send)
    # json object (string) needs to be encoded to bytes
    # in order to send through the socket
    data_to_send_encoded = data_to_send_json.encode(encoding="utf-8")
    # connecting to data server
    s.connect((HOST, PORT))
    # sending data
    # sendall() closes socket after sending is finished afaik
    s.sendall(data_to_send_encoded)
    # reading the data sent back by data server
    data = s.recv(1024)

print(f"received,{data!r}")
