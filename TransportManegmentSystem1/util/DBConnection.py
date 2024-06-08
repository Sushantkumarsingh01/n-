


import mysql.connector
import configparser
import time

class DatabaseConnect:
    def __init__(self, database='TransportManagement'):
        config = configparser.ConfigParser()
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
                print(f"Connected to the database: {self.database}")
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
                print("\nDisconnected from the database.")
        except mysql.connector.Error as e:
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

























"""

import mysql.connector
import time



class DatabaseConnect:
    def __init__(self, database='TransportManagement'):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'Sushant@9546'
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
                print(f"Connected to the database: {self.database}")
                return self.connection
            except mysql.connector.Error as err:
                if attempt < max_retries:
                    print(f"Retrying connection (Attempt {attempt}/{max_retries})...")
                    time.sleep(retry_delay)
                else:
                    print(f" Unable to establish a connection.")
                    raise Exception(f"Error in connecting: {err}")

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print("\nDisconnected from the database.")
        except mysql.connector.Error as e:
            raise Exception(f"Error disconnecting database: {e}")

    def execute_query(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            return self.cursor, self.connection
        except mysql.connector.Error as e:
            raise Exception(f"Error executing query: {e}")

    def get_current_cursor(self):
        pass

"""





























"""import mysql.connector
from mysql.connector import Error
import configparser
import os

class DBConnection:
    @staticmethod
    def get_connection():
        try:
            config = configparser.ConfigParser()
            config_file_path = os.path.join(os.path.dirname(__file__), 'database.properties')
            config.read(config_file_path)

            host = config['DATABASE']['host']
            user = config['DATABASE']['user']
            password = config['DATABASE']['password']
            database = config['DATABASE']['database']

            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            if connection.is_connected():
                print("Connected to database")

            return connection

        except Error as e:
            print(f"Error connecting to database: {e}")
            return None
"""










"""
import mysql.connector
from mysql.connector import Error
import configparser
import os


class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                config = configparser.ConfigParser()
                config_file_path = os.path.join(os.path.dirname(__file__), 'database.properties')

                if not os.path.exists(config_file_path):
                    raise FileNotFoundError(f"Config file not found at {config_file_path}")

                config.read(config_file_path)

                if 'DATABASE' not in config:
                    raise KeyError("DATABASE section not found in the config file")

                print("Config sections:", config.sections())  # Debug print
                print("Config DATABASE:", config['DATABASE'])  # Debug print

                DBConnection.connection = mysql.connector.connect(
                    host=config['DATABASE']['host'],
                    database=config['DATABASE']['database'],
                    user=config['DATABASE']['user'],
                    password=config['DATABASE']['password']
                )
                if DBConnection.connection.is_connected():
                    print("Connection established")
            except FileNotFoundError as e:
                print(f"File not found error: {e}")
                DBConnection.connection = None
            except KeyError as e:
                print(f"Key error: {e}")
                DBConnection.connection = None
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                DBConnection.connection = None
            except Exception as e:
                print(f"General error: {e}")
                DBConnection.connection = None
        return DBConnection.connection
        
        
"""


"""
import mysql.connector
from mysql.connector import Error
import configparser
import os

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                config = configparser.ConfigParser()
                config_file_path = os.path.join(os.path.dirname(__file__), 'database.properties')
                config.read(config_file_path)

                if 'DATABASE' not in config:
                    raise KeyError("DATABASE section not found in the config file")

                DBConnection.connection = mysql.connector.connect(
                    host=config['DATABASE']['host'],
                    database=config['DATABASE']['database'],
                    user=config['DATABASE']['user'],
                    password=config['DATABASE']['password']
                )
                if DBConnection.connection.is_connected():
                    print("Connection established")
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                DBConnection.connection = None
            except KeyError as e:
                print(f"Key error: {e}")
                DBConnection.connection = None
            except Exception as e:
                print(f"General error: {e}")
                DBConnection.connection = None
        return DBConnection.connection
"""




""""

import mysql.connector
from mysql.connector import Error
import configparser
import os

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                config = configparser.ConfigParser()
                config_file_path = os.path.join(os.path.dirname(__file__), 'database.properties')
                config.read(config_file_path)

                if 'DATABASE' not in config:
                    raise KeyError("DATABASE section not found in the config file")

                print("Config sections:", config.sections())  # Debug print
                print("Config DATABASE:", config['DATABASE'])  # Debug print

                DBConnection.connection = mysql.connector.connect(
                    host=config['DATABASE']['host'],
                    database=config['DATABASE']['database'],
                    user=config['DATABASE']['user'],
                    password=config['DATABASE']['password']
                )
                if DBConnection.connection.is_connected():
                    print("Connection established")
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                DBConnection.connection = None
            except KeyError as e:
                print(f"Key error: {e}")
                DBConnection.connection = None
            except Exception as e:
                print(f"General error: {e}")
                DBConnection.connection = None
        return DBConnection.connection
"""


