from dao.TransportManagementService import TransportManagementService
from entity import Vehicle, Booking, Trip, Passenger
from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.BookingNotFoundException import BookingNotFoundException
from util.DBConnection import DBConnection
from typing import List
import mysql.connector

class TransportManagementServiceImpl(TransportManagementService):

    def __init__(self):
        self.connection = DBConnection.getConnection()

    def addVehicle(self, vehicle: Vehicle) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO Vehicles (Model, Capacity, Type, Status) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (vehicle._model, vehicle._capacity, vehicle._type, vehicle._status))
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def updateVehicle(self, vehicle: Vehicle) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "UPDATE Vehicles SET Model = %s, Capacity = %s, Type = %s, Status = %s WHERE VehicleID = %s"
            cursor.execute(query, (vehicle._model, vehicle._capacity, vehicle._type, vehicle._status, vehicle._vehicle_id))
            self.connection.commit()
            if cursor.rowcount == 0:
                raise VehicleNotFoundException()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def deleteVehicle(self, vehicleId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "DELETE FROM Vehicles WHERE VehicleID = %s"
            cursor.execute(query, (vehicleId,))
            self.connection.commit()
            if cursor.rowcount == 0:
                raise VehicleNotFoundException()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def scheduleTrip(self, vehicleId: int, routeId: int, departureDate: str, arrivalDate: str) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO Trips (VehicleID, RouteID, DepartureDate, ArrivalDate, Status) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (vehicleId, routeId, departureDate, arrivalDate, 'Scheduled'))
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def cancelTrip(self, tripId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "UPDATE Trips SET Status = %s WHERE TripID = %s"
            cursor.execute(query, ('Cancelled', tripId))
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def bookTrip(self, tripId: int, passengerId: int, bookingDate: str) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO Bookings (TripID, PassengerID, BookingDate, Status) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (tripId, passengerId, bookingDate, 'Confirmed'))
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def cancelBooking(self, bookingId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "UPDATE Bookings SET Status = %s WHERE BookingID = %s"
            cursor.execute(query, ('Cancelled', bookingId))
            self.connection.commit()
            if cursor.rowcount == 0:
                raise BookingNotFoundException()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def allocateDriver(self, tripId: int, driverId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "UPDATE Trips SET DriverID = %s WHERE TripID = %s"
            cursor.execute(query, (driverId, tripId))
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def deallocateDriver(self, tripId: int) -> bool:
        cursor = self.connection.cursor()
        try:
            query = "UPDATE Trips SET DriverID = NULL WHERE TripID = %s"
            cursor.execute(query, (tripId,))
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def getBookingsByPassenger(self, passengerId: int) -> List[Booking]:
        cursor = self.connection.cursor()
        try:
            query = "SELECT * FROM Bookings WHERE PassengerID = %s"
            cursor.execute(query, (passengerId,))
            bookings = cursor.fetchall()
            return [Booking(*booking) for booking in bookings]
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()

    def getBookingsByTrip(self, tripId: int) -> List[Booking]:
        cursor = self.connection.cursor()
        try:
            query = "SELECT * FROM Bookings WHERE TripID = %s"
            cursor.execute(query, (tripId,))
            bookings = cursor.fetchall()
            return [Booking(*booking) for booking in bookings]
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()

    def getAvailableDrivers(self) -> List[int]:
        cursor = self.connection.cursor()
        try:
            query = "SELECT DriverID FROM Drivers WHERE DriverID NOT IN (SELECT DriverID FROM Trips WHERE Status = 'Scheduled' OR Status = 'In Progress')"
            cursor.execute(query)
            drivers = cursor.fetchall()
            return [driver[0] for driver in drivers]
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
