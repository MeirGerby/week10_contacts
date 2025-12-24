import mysql.connector 
import os 

class DBConnecotor: 
    _connection = None
    HOST = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')

    @classmethod
    def get_connction(cls):
        if cls._connection and cls._connection.is_connected():
            return cls._connection 
        cls._connection =  cls.connect_to_db() 

    @classmethod
    def connect_to_db(cls):
        """connecting to mysql db"""
        return mysql.connector.connect(cls.HOST, cls.USER, cls.PASSWORD)
        
        


    

