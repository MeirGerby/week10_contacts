import mysql.connector
from dotenv import load_dotenv 
import os 

class DBConnecotor: 
    _connection = None
    load_dotenv()
    HOST = os.getenv('DB_HOST')
    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    PORT = os.getenv("DB_PORT")

    @classmethod
    def get_connction(cls):
        if cls._connection:
            if cls._connection.is_connected():
                print("cennecting to mysql")
                return cls._connection 
        cls._connection =  cls.connect_to_db() 

    @classmethod
    def connect_to_db(cls):
        """connecting to mysql db"""
        try:
            return mysql.connector.connect(host=cls.HOST, user=cls.USER, password=cls.PASSWORD)
        except:
            raise ConnectionError("mysql is not connecting")

        


    

