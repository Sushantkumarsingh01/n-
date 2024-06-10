from utils.database import DatabaseConnect
from datetime import date

class BookingService:
    @staticmethod
    def book_trip(trip_id: int, passenger_id: int, booking_date: date):
        db_connection = DatabaseConnect()
        connection = db_connection.connect()
        try:
            query = "INSERT INTO Bookings (TripID, PassengerID, BookingDate, Status) VALUES (%s, %s, %s, %s)"
            db_connection.execute_query(query, (trip_id, passenger_id, booking_date, 'Booked'))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            db_connection.disconnect()
