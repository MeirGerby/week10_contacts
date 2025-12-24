from services.sql_connector import DBConnecotor 
from model import Contact 
from crud.create_db_and_table import CreateDB
from crud.crud import DatabaseService

class MannageDB: 
    
    @staticmethod
    def create_corsor():
        connector = DBConnecotor.get_connction()
        cursor = connector.cursor() 
        return cursor
    

    @staticmethod
    def create_db_and_tables(cursor):    
        cursor.execute(CreateDB().create_datebase()) 
        cursor.execute(CreateDB().create_table()) 
        cursor.execute(CreateDB().insert_into_db()) 
        
    @staticmethod
    def get_contacts(cursor):
        cursor.execute(DatabaseService.get_all_contacts()) 
    @staticmethod
    def update(cursor, id, first_name, last_name, phone_number):
        cursor.execute(DatabaseService.update_contact(id, first_name, last_name, phone_number)) 
    @staticmethod
    def delete(id ,cursor):
        cursor.execute(DatabaseService.delete_contact(id)) 
    @staticmethod
    def create(cursor,id, first_name: str, last_name: str, phone_number: str):
        cursor.execute(DatabaseService.create_contact(id, first_name, last_name, phone_number))  

    

        

