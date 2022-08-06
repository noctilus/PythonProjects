import time
from w1thermsensor import W1ThermSensor
for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.1f" %
          (sensor.id, sensor.get_temperature()))

# Sensor 3c01a8161bf0 has temperature 0.44
# Sensor 3c01a816f695 has temperature 19.06
