class DatabaseService:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name: str = first_name
        self.last_name: str = last_name 
        self.phone_number: str = phone_number
        
    def create_contact(self) -> str:
        create_query = "INSERT INTO contacts_db " \
        "(first_name, last_name, phone_number) " \
        "VALUES (self.first_name, self.last_name, self.phone_number)" 
        return create_query

    def get_all_contacts(self) -> str:
        select_query = "SELECT * FROM contacts_db"
        return select_query

    def update_contact(self, id: int) -> str:
        update_query = f"""
        UPDATE contacts_db 
        SET first_name = {self.first_name},
        last_name = {self.last_name},
        phone_number = {self.phone_number} 
        WHERE id = {id}
        """
        return update_query
        
    def delete_contact(self, id: int) -> str:
        delete_query = f"DELETE FROM contacts_db WHERE id = {id}"
        return delete_query 

 

