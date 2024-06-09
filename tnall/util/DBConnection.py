

import time
import mysql.connector
import configparser


class DatabaseConnect:
    def __init__(self, database='TransportManagement'):
        config = configparser.ConfigParser() #insital
        config.read('config.ini')
        database_config = config['Database']

        self.host = database_config['host']
        self.user = database_config['user']
        self.password = database_config['password']
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self, max_retries=3, retry_delay=2):
        for attempt in range(1, max_retries + 1):
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                self.cursor = self.connection.cursor()
                #print(f"Connected to the database: {self.database}")
                return self.connection
            except mysql.connector.Error as err:
                if attempt < max_retries:
                    print(f"Retrying connection (Attempt {attempt}/{max_retries})...")
                    time.sleep(retry_delay)
                else:
                    print("Unable to establish a connection.")
                    raise

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print("\n Disconnected")
        except mysql.connector.Error as e:
            print(f"Error occurred while disconnecting: {e}")
            raise

    def execute_query(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            return self.cursor, self.connection
        except mysql.connector.Error as e:
            raise

