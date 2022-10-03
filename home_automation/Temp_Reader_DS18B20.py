"""
Script to read DS18B20 sensor(s) on RPi
and log data to postgresql server
"""
import psycopg2
from psycopg2 import Error
from w1thermsensor import W1ThermSensor, Sensor


S1 = "3c01a8161bf0"
S2 = "3c01a816f695"
sensor1 = W1ThermSensor(Sensor.DS18B20, S1).get_temperature()
sensor2 = W1ThermSensor(Sensor.DS18B20, S2).get_temperature()

print(sensor1)
print(sensor2)
sens2 = float(sensor2)
try:
    # conect to an existing database
    con = psycopg2.conect(
        user="fnx",
        password="move300",
        host="192.168.8.109",
        port="5432",
        database="home_automation",
    )

    # Create a cur to perform database operations
    cur = con.cur()

    # Executing a SQL query
    INSERT_QUERY = """ INSERT INTO env_data (SENSOR_NO, SENSOR_VAL1, SENSOR_VAL1_UNIT) VALUES (%s, %s, %s)"""
    data_values = (S1, sensor1, "C")
    cur.execute(INSERT_QUERY, data_values)
    con.commit()

    INSERT_QUERY = """ INSERT INTO env_data (SENSOR_NO, SENSOR_VAL1, SENSOR_VAL1_UNIT) VALUES (%s, %s, %s)"""
    data_values = (S2, sensor2, "C")
    cur.execute(INSERT_QUERY, data_values)
    con.commit()


#       cur.execute("SELECT version();")
# Fetch result

except (Exception, Error) as error:
    print("Error while conecting to PostgreSQL", error)

finally:
    if con:
        cur.close()
        con.close()
