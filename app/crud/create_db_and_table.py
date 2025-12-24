from model import Contact

class CreateDB:
    def init_db(self):
        self.create_datebase()
        self.create_table()
        self.insert_into_db()

    def create_datebase(self) -> str:
        create_db = "CREATE DATABASE IF NOT EXISTS contacts_db;" 
        return create_db 

    def create_table(self) -> str:
        table = "USE contacts_db; " \
        "CREATE TABLE IF NOT EXISTS contacts (" \
        "id INT AUTO_INCREMENT PRIMARY KEY, " \
        "first_name VARCHAR(50) NOT NULL, " \
        "last_name VARCHAR(50) NOT NULL, " \
        "phone_number VARCHAR(20) NOT NULL UNIQUE" \
        ");"    
        return table
    
    def insert_into_db(self) -> str:
        insert_into = "" \
            "INSERT INTO contacts " \
            "(first_name, last_name, phone_number) " \
            "VALUES" \
            "('John', 'Doe', '050-1234567')," \
            "('Jane', 'Smith', '052-9876543')," \
            "('Bob', 'Johnson', '054-5555555')," \
            "('Jack', 'Robinson', '050-6115555');"
        return insert_into 
    




    
    
    
    