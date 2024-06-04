"""Testing sending sensor data from ESP32 to server
possibly as a json file"""

import json

TEMP = "29.5"
PRESS = "99491.21"
MACHINE = "083af2ac7060"
TIM = "(2024, 6, 4 ,1, 10, 59, 5, 93409)"
BAT = "85.4"
HUM = "55"
dictionary = {
    "pressure": PRESS,
    "temperature": TEMP,
    "machine_id": MACHINE,
    "timedate": TIM,
    "battery": BAT,
    "humidity": HUM,
}

json_object = json.dumps(dictionary)

with open("json.txt", "a") as json_file:
    json_file.write(json_object)
    print("Writen to file ok")

with open("json.txt", "r") as fil:
    json_z_pliku = json.load(fil)
    print(type(json_z_pliku))
    print(json_z_pliku)
