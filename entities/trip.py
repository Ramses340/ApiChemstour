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

    @classmethod
    def update(cls, trip_id, name, city, country, latitude, longitude):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql = """
                UPDATE trip
                SET name = %s, city = %s, country = %s, latitude = %s, longitude = %s
                WHERE id = %s
            """
            cursor.execute(sql, (name, city, country, latitude, longitude, trip_id))
            connection.commit()
            return cursor.rowcount > 0
        except Error as ex:
            print("Error al actualizar:", ex)
            return False
        finally:
            if cursor: cursor.close()
            if connection: connection.close()

    @classmethod
    def delete(cls, trip_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql = "DELETE FROM trip WHERE id = %s"
            cursor.execute(sql, (trip_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Error as ex:
            print("Error al eliminar:", ex)
            return False
        finally:
            if cursor: cursor.close()
            if connection: connection.close()