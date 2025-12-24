from services.sql_connector import DBConnecotor 
from model import Contact 

class MannageDB: 
    def __init__(self):
        self._connector = DBConnecotor.get_connction()
        self.contacts: list[Contact] = [] 
        self.db_name = "contact_db" 