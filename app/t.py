from fastapi import FastAPI 
import uvicorn
from pydantic import BaseModel, Field
from typing import Annotated, List


app = FastAPI()

class Contact(BaseModel):
    id: int | None = None 
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    phone_number: Annotated[str, Field(max_length=20)] 


    
contacts: List[Contact] = []
