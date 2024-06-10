from utils.database import DatabaseConnect

class DriverService:
    @staticmethod
    def get_available_drivers():
        db_connection = DatabaseConnect()
        connection = db_connection.connect()
        try:
            query = "SELECT * FROM Drivers WHERE Status = 'Available'"
            db_connection.execute_query(query)
            result = db_connection.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            db_connection.disconnect()
