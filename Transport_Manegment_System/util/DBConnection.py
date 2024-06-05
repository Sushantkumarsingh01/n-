import mysql.connector
import configparser

class DBConnection:
    _connection = None

    @staticmethod
    def getConnection():
        if DBConnection._connection is None:
            config = configparser.ConfigParser()
            config.read('dbconfig.properties')
            DBConnection._connection = mysql.connector.connect(
                host=config['DATABASE']['host'],
                user=config['DATABASE']['user'],
                password=config['DATABASE']['password'],
                database=config['DATABASE']['database']
            )
        return DBConnection._connection





















































"""import mysql.connector
from mysql.connector import Error
from util.DBPropertyUtil import DBPropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            properties = DBPropertyUtil.get_properties('config/db.properties')
            try:
                DBConnection.connection = mysql.connector.connect(
                    host=properties['url'].split('/')[2].split(':')[0],
                    database=properties['url'].split('/')[-1],
                    user=properties['username'],
                    password=properties['password']
                )
                if DBConnection.connection.is_connected():
                    print("Connected to MySQL database")
            except Error as e:
                print(f"Error while connecting to MySQL: {e}")
        return DBConnection.connection """
