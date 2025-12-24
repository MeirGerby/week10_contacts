from typing import Annotated
from pydantic import BaseModel, Field

class Contact(BaseModel):
    id: int | None = None
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    phone_number: Annotated[str, Field(max_length=20)] 


    def convert_contact_to_dict(self):
        return {
            "first name": self.first_name,
            "last name": self.last_name,
            "phone number": self.phone_number
            } 
    
