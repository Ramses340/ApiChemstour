# entities/trip.py

from persistence.db import get_connection
from mysql.connector import Error

class Trip:

    def __init__(self, name, city, country, latitude, longitude):
        self.name = name
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude


    @classmethod
    def get(cls):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT id, name, city, country, latitude, longitude FROM trip')
            return cursor.fetchall()
        except Error as ex:
            print("Error al obtener viajes:", ex)
            return []
        finally:
            if cursor: cursor.close()
            if connection: connection.close()

    @classmethod
    def add(cls, name, city, country, latitude, longitude):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql = "INSERT INTO trip (name, city, country, latitude, longitude) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, city, country, latitude, longitude ))
            connection.commit()
            return True
        except Error as ex:
            print("Error al insertar:", ex)
            return False
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
