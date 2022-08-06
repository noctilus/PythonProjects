import psycopg2
from psycopg2 import Error
from w1thermsensor import W1ThermSensor, Sensor


s1 = "3c01a8161bf0"
s2 = "3c01a816f695"
sensor1 = (W1ThermSensor(Sensor.DS18B20, s1).get_temperature())
sensor2 = (W1ThermSensor(Sensor.DS18B20, s2).get_temperature())

print(sensor1)
print(sensor2)
sens2 = float(sensor2)
try:
    # Connect to an existing database
    connection = psycopg2.connect(user="fnx",
                                  password="move300",
                                  host="192.168.8.109",
                                  port="5432",
                                  database="home_automation")

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    # Executing a SQL query
    insert_query = """ INSERT INTO env_data (SENSOR_NO, SENSOR_VAL1, SENSOR_VAL1_UNIT) VALUES (%s, %s, %s)"""
    data_values = (s1, sensor1, "C")
    cursor.execute(insert_query, data_values)
    connection.commit()

    insert_query = """ INSERT INTO env_data (SENSOR_NO, SENSOR_VAL1, SENSOR_VAL1_UNIT) VALUES (%s, %s, %s)"""
    data_values = (s2, sensor2, "C")
    cursor.execute(insert_query, data_values)
    connection.commit()


#       cursor.execute("SELECT version();")
    # Fetch result

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
