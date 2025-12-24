

class DatabaseService:
    def create_contact(self, Dict: <Contact Params>) -> int:
        create_query = f"INSERT INTO contacts_db velues({contact})" 
        return create_query


    def get_all_contacts(self) -> list[dict]:
        select_query = "SELECT * FROM contacts_db"
        return select_query

    def update_contact(self, id, Dict: <Contact Params>) -> str:
        update_query = "SELECT * FROM contacts_db WHERE ID == id"
        return  

    def delete_contact(self, id) -> bool:
        delete_query = "DELETE * FROM contacts_db WHERE ID == id"
        pass 
        return 

 

