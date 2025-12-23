from typing import Annotated, List 
from pydantic import BaseModel, Field

class Contact(BaseModel):
    id: int 
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    phone_number: Annotated[str, Field(max_length=20)] 

class CreateContact(BaseModel):
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    phone_number: Annotated[str, Field(max_length=20)] 

class UpdateContact(BaseModel):
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    phone_number: Annotated[str, Field(max_length=20)] 