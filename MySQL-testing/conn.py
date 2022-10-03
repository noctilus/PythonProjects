""" Simple MySQL query script """
import mysql.connector

cnx = mysql.connector.connect(
    user="horst_baza",
    database="horst_baza",
    host="193.177.164.5",
    password="bKU6WC9y0R",
)
cursor = cnx.cursor()

QUERY = "SELECT * FROM clients"


cursor.execute(QUERY)

for data in cursor:  # type: ignore
    print(data)

cursor.close()
cnx.close()
