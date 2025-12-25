from services.sql_connector import DBConnecotor 
from crud.create_db_and_table import CreateDB
from crud.crud import DatabaseService

class MannageDB: 
    
    @staticmethod
    def create_corsor():
        try:
            connector = DBConnecotor.connect_to_db()
            if connector.is_connected():
                try:
                    cursor = connector.cursor() 
                    return cursor
                except:
                    raise ConnectionError("the cursor is not connecter") 
        except:
            raise ConnectionError("can't connect to mysql")
            
            
        
    

    @staticmethod
    def create_db_and_tables(cursor):  
        try:
            create_db: str = CreateDB().create_datebase() 
            cursor.execute(create_db) 
            print("database created seccesfully")
        except:
            raise ConnectionError("can't create the database")
        try:
            create_table: str = CreateDB().create_table()
            cursor.execute(create_table) 
            print("table created seccesfully")
        except:
            raise ConnectionError("can't create the table")
            
        try:
            create_columns: str = CreateDB().insert_into_db()
            cursor.execute(create_columns) 
            print("columns created seccesfully")
        except:
            raise ConnectionError("can't create the table")
            
        
        
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


    

        

