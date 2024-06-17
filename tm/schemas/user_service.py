from utils.database import DatabaseConnect
from utils.database import DatabaseConnect

class UserService:
    @staticmethod
    def register_user(user):
        try:
            db_connection = DatabaseConnect()
            db_connection.connect()
            query = """
            INSERT INTO Customers (UserID, FirstName, LastName, PhoneNumber, Email)
            VALUES ((SELECT UserID FROM Users WHERE Username = %s), %s, %s, %s, %s)
            """
            print("Executing query:", query)  # Print the query
            db_connection.execute_query(query, (
                user.username, user.first_name, user.last_name, user.phone_number, user.email
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
            print(result)
            db_connection.disconnect()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None
