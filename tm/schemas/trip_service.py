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


def trip_service():
    return None