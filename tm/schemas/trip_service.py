from utils.database import DatabaseConnect
from datetime import date

class TripService:
    @staticmethod
    def schedule_trip(vehicle_id: int, route_id: int, departure_date: date, arrival_date: date, trip_type: str, max_passengers: int):
        db_connection = DatabaseConnect()
        connection = db_connection.connect()
        try:
            query = "INSERT INTO Trips (VehicleID, RouteID, DepartureDate, ArrivalDate, TripType, MaxPassengers, Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            db_connection.execute_query(query, (vehicle_id, route_id, departure_date, arrival_date, trip_type, max_passengers, 'Scheduled'))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            db_connection.disconnect()


@staticmethod
def cancel_trip(trip_id: int) -> bool:
    try:
        db_connection = DatabaseConnect()
        connection = db_connection.connect()

        # Check if there are associated bookings
        booking_query = "SELECT * FROM Bookings WHERE TripID = %s"
        db_connection.execute_query(booking_query, (trip_id,))
        booking_result = db_connection.cursor.fetchall()  # Fetch all booking results
        if booking_result:
            # For simplicity, let's just return False if there are bookings associated with the trip
            return False

        # If there are no associated bookings, proceed to cancel the trip
        delete_query = "DELETE FROM Trips WHERE TripID = %s"
        db_connection.execute_query(delete_query, (trip_id,))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        db_connection.disconnect()



"""
    @staticmethod
    def cancel_trip(trip_id: int) -> bool:
        db_connection = DatabaseConnect()
        connection = db_connection.connect()
        try:
            query = "DELETE FROM Trips WHERE TripID = %s"
            db_connection.execute_query(query, (trip_id,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            db_connection.disconnect()
"""

def trip_service():
    return None