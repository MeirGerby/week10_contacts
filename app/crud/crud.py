class DatabaseService:

        
    @staticmethod
    def create_contact(id: int, first_name: str, last_name: str, phone_number: str) -> str:
        create_query = "INSERT INTO contacts_db " \
        "(first_name, last_name, phone_number) " \
        "VALUES (self.first_name, self.last_name, self.phone_number)" 
        return create_query

    @staticmethod
    def get_all_contacts() -> str:
        select_query = "SELECT * FROM contacts_db"
        return select_query
    
    @staticmethod
    def update_contact(id: int, first_name: str, last_name: str, phone_number: str) -> str:
        update_query = f"""
        UPDATE contacts_db 
        SET first_name = {first_name},
        last_name = {last_name},
        phone_number = {phone_number} 
        WHERE id = {id}
        """
        return update_query
    
    @staticmethod
    def delete_contact(id: int) -> str:   
        delete_query = f"DELETE FROM contacts_db WHERE id = {id}"
        return delete_query 

 

