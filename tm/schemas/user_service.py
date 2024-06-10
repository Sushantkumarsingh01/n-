from utils.database import DatabaseConnect
from utils.database import DatabaseConnect

class UserService:
    @staticmethod
    def register_user(user):
        try:
            db_connection = DatabaseConnect()
            db_connection.connect()
            query = """
            INSERT INTO Users (FirstName, LastName, PhoneNumber, Email, Username, Password, Role)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            db_connection.execute_query(query, (
                user.first_name, user.last_name, user.phone_number, user.email, user.username, user.password, user.role
            ))
            db_connection.connection.commit()
            db_connection.disconnect()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def authenticate_user(username, password):
        try:
            db_connection = DatabaseConnect()
            db_connection.connect()
            query = "SELECT Role FROM Users WHERE Username = %s AND Password = %s"
            db_connection.execute_query(query, (username, password))
            result = db_connection.cursor.fetchone()
            db_connection.disconnect()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None
