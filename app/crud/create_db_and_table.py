from model import Contact

class CreateDB:
    
    @staticmethod
    def create_datebase() -> str:
        create_db = "CREATE DATABASE IF NOT EXISTS contacts_db;" 
        return create_db 

    @staticmethod
    def create_table() -> str:
        table = "USE contacts_db; " \
        "CREATE TABLE IF NOT EXISTS contacts (" \
        "id INT AUTO_INCREMENT PRIMARY KEY, " \
        "first_name VARCHAR(50) NOT NULL, " \
        "last_name VARCHAR(50) NOT NULL, " \
        "phone_number VARCHAR(20) NOT NULL UNIQUE" \
        ");"    
        return table
    
    @staticmethod
    def insert_into_db() -> str:
        insert_into = "" \
            "INSERT INTO contacts " \
            "(first_name, last_name, phone_number) " \
            "VALUES" \
            "('John', 'Doe', '050-1234567')," \
            "('Jane', 'Smith', '052-9876543')," \
            "('Bob', 'Johnson', '054-5555555')," \
            "('Jack', 'Robinson', '050-6115555');"
        return insert_into 
    




    
    
    
    