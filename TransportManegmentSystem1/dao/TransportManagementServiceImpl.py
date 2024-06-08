from util.DBConnection import DatabaseConnect
from entity.Vehicle import Vehicle
from entity.Booking import Booking
from entity.Driver import Driver
from entity.Admin import Admin
from entity.Customer import Customer
import mysql.connector

class TransportManagementServiceImpl:
    def __init__(self):
        self.db_connection = DatabaseConnect()
        self.connection = self.db_connection.connect()

    def get_user_role(self, username, password):
        try:
            self.db_connection.connect()
            query = "SELECT Role FROM Users WHERE Username = %s AND Password = %s"
            self.db_connection.execute_query(query, (username, password))
            result = self.db_connection.cursor.fetchone()
            self.db_connection.disconnect()
            return result[0] if result else None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def get_customer_id(self, username):
        try:
            self.db_connection.connect()
            query = "SELECT CustomerID FROM Customers WHERE Username = %s"
            self.db_connection.execute_query(query, (username,))
            result = self.db_connection.cursor.fetchone()
            self.db_connection.disconnect()
            return result[0] if result else None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def register_user(self, first_name, last_name, phone_number, email, username, password, role):
        try:
            self.db_connection.connect()
            query = "INSERT INTO Users (Username, Password, Role) VALUES (%s, %s, %s)"
            self.db_connection.execute_query(query, (username, password, role))
            user_id = self.db_connection.cursor.lastrowid

            if role == "customer":
                query = "INSERT INTO Customers (UserID, FirstName, LastName, PhoneNumber, Email) VALUES (%s, %s, %s, %s, %s)"
                self.db_connection.execute_query(query, (user_id, first_name, last_name, phone_number, email))
            elif role == "admin":
                query = "INSERT INTO Admins (UserID) VALUES (%s)"
                self.db_connection.execute_query(query, (user_id,))

            self.db_connection.connection.commit()
            self.db_connection.disconnect()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def authenticate_admin(self, username, password):
        try:
            self.db_connection.connect()
            query = "SELECT * FROM Admins WHERE Username = %s AND Password = %s"
            self.db_connection.execute_query(query, (username, password))
            result = self.db_connection.cursor.fetchone()
            self.db_connection.disconnect()
            return result is not None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def authenticate_user(self, username, password):
        try:
            self.db_connection.connect()
            query = "SELECT Role FROM Users WHERE Username = %s AND Password = %s"
            self.db_connection.execute_query(query, (username, password))
            result = self.db_connection.cursor.fetchone()
            self.db_connection.disconnect()
            return result[0] if result else None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def addVehicle(self, vehicle):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Vehicles (Model, Capacity, Type, Status) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (vehicle.model, vehicle.capacity, vehicle.type, vehicle.status))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def updateVehicle(self, vehicle):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Vehicles SET Model = %s, Capacity = %s, Type = %s, Status = %s WHERE VehicleID = %s"
            cursor.execute(query, (vehicle.model, vehicle.capacity, vehicle.type, vehicle.status, vehicle.vehicle_id))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def deleteVehicle(self, vehicle_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Vehicles WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def scheduleTrip(self, vehicle_id, route_id, departure_date, arrival_date, trip_type, max_passengers):
        try:
            self.db_connection.connect()
            query = "INSERT INTO Trips (VehicleID, RouteID, DepartureDate, ArrivalDate, TripType, MaxPassengers, Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.db_connection.execute_query(query, (
            vehicle_id, route_id, departure_date, arrival_date, trip_type, max_passengers, 'Scheduled'))
            self.db_connection.connection.commit()
            self.db_connection.disconnect()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def cancelTrip(self, trip_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Trips WHERE TripID = %s"
            cursor.execute(query, (trip_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def bookTrip(self, trip_id, passenger_id, booking_date):
        try:
            self.db_connection.connect()
            query = "INSERT INTO Bookings (TripID, PassengerID, BookingDate, Status) VALUES (%s, %s, %s, %s)"
            self.db_connection.execute_query(query, (trip_id, passenger_id, booking_date, 'Booked'))
            self.db_connection.connection.commit()
            self.db_connection.disconnect()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def cancelBooking(self, booking_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Bookings WHERE BookingID = %s"
            cursor.execute(query, (booking_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def allocateDriver(self, trip_id, driver_id):
        try:
            self.db_connection.connect()
            query = "UPDATE Trips SET DriverID = %s WHERE TripID = %s"
            self.db_connection.execute_query(query, (driver_id, trip_id))
            self.db_connection.connection.commit()
            self.db_connection.disconnect()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def deallocateDriver(self, trip_id):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Trips SET DriverID = NULL WHERE TripID = %s"
            cursor.execute(query, (trip_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def getBookingsByPassenger(self, passenger_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Bookings WHERE PassengerID = %s"
            cursor.execute(query, (passenger_id,))
            bookings = cursor.fetchall()
            cursor.close()
            return [Booking(*booking) for booking in bookings]
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def getBookingsByTrip(self, trip_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Bookings WHERE TripID = %s"
            cursor.execute(query, (trip_id,))
            bookings = cursor.fetchall()
            cursor.close()
            return [Booking(*booking) for booking in bookings]
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def getAvailableDrivers(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Drivers WHERE DriverID NOT IN (SELECT DriverID FROM Trips WHERE DriverID IS NOT NULL)"
            cursor.execute(query)
            drivers = cursor.fetchall()
            cursor.close()
            return [Driver(*driver) for driver in drivers]
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []










































"""
from util.DBConnection import DatabaseConnect
from exception.VehicleNotFoundException import VehicleNotFoundException
from entity.Vehicle import Vehicle
import mysql.connector

class TransportManagementServiceImpl:
    def __init__(self):
        self.db_connection = DatabaseConnect()

    def addVehicle(self, vehicle):
        try:
            connection = self.db_connection.connect()
            cursor = connection.cursor()
            query = "INSERT INTO Vehicles (Model, Capacity, Type, Status) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (vehicle.model, vehicle.capacity, vehicle.type, vehicle.status))
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            self.db_connection.disconnect()

    def updateVehicle(self, vehicle):
        try:
            connection = self.db_connection.connect()
            cursor = connection.cursor()
            query = "UPDATE Vehicles SET Model = %s, Capacity = %s, Type = %s, Status = %s WHERE VehicleID = %s"
            cursor.execute(query, (vehicle.model, vehicle.capacity, vehicle.type, vehicle.status, vehicle.vehicle_id))
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            self.db_connection.disconnect()

    def deleteVehicle(self, vehicle_id):
        try:
            connection = self.db_connection.connect()
            cursor = connection.cursor()
            query = "DELETE FROM Vehicles WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            self.db_connection.disconnect()


"""

"""
from entity.Booking import Booking
from entity.Driver import Driver
from util.DBConnection import DatabaseConnect
from exception.VehicleNotFoundException import VehicleNotFoundException
from entity.Vehicle import Vehicle
import mysql.connector

class TransportManagementServiceImpl:
    def __init__(self):
        self.db_connection = DatabaseConnect()

    def addVehicle(self, vehicle):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Vehicles (Model, Capacity, Type, Status) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (vehicle.model, vehicle.capacity, vehicle.type, vehicle.status))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def updateVehicle(self, vehicle):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Vehicles SET Model = %s, Capacity = %s, Type = %s, Status = %s WHERE VehicleID = %s"
            cursor.execute(query, (vehicle.model, vehicle.capacity, vehicle.type, vehicle.status, vehicle.vehicle_id))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def deleteVehicle(self, vehicle_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Vehicles WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def scheduleTrip(self, vehicle_id, route_id, departure_date, arrival_date):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Trips (VehicleID, RouteID, DepartureDate, ArrivalDate) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (vehicle_id, route_id, departure_date, arrival_date))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def cancelTrip(self, trip_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Trips WHERE TripID = %s"
            cursor.execute(query, (trip_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def bookTrip(self, trip_id, passenger_id, booking_date):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Bookings (TripID, PassengerID, BookingDate) VALUES (%s, %s, %s)"
            cursor.execute(query, (trip_id, passenger_id, booking_date))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def cancelBooking(self, booking_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Bookings WHERE BookingID = %s"
            cursor.execute(query, (booking_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def allocateDriver(self, trip_id, driver_id):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Trips SET DriverID = %s WHERE TripID = %s"
            cursor.execute(query, (driver_id, trip_id))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def deallocateDriver(self, trip_id):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Trips SET DriverID = NULL WHERE TripID = %s"
            cursor.execute(query, (trip_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def getBookingsByPassenger(self, passenger_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Bookings WHERE PassengerID = %s"
            cursor.execute(query, (passenger_id,))
            bookings = cursor.fetchall()
            cursor.close()
            return [Booking(*booking) for booking in bookings]
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def getBookingsByTrip(self, trip_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Bookings WHERE TripID = %s"
            cursor.execute(query, (trip_id,))
            bookings = cursor.fetchall()
            cursor.close()
            return [Booking(*booking) for booking in bookings]
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def getAvailableDrivers(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Drivers WHERE DriverID NOT IN (SELECT DriverID FROM Trips WHERE DriverID IS NOT NULL)"
            cursor.execute(query)
            drivers = cursor.fetchall()
            cursor.close()
            return [Driver(*driver) for driver in drivers]
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return [] """
            
            

