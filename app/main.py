from fastapi import FastAPI, HTTPException 
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

@app.get('/contacts')
def get_all_contacts() -> list:
    return contacts 



@app.post("/contacts")
def create_new_contact(contact: Contact):
    contacts.append(contact)
    return {"message": "the contact added successfully",
            "contact id": contact.id}

@app.put('/contacts/{id}')
def update_existing_contact(id, contact: Contact):
    for co in contacts:    
        try:
            if co.id == id:
                contacts.append(contact)
                return {"Message": "update successfully"}
        except:
            raise HTTPException(status_code=404, detail="the ID is not found")
                
                
@app.delete('/contacts/{id}')
def delete_contact(id, contact: Contact):
    for co in contacts:    
        try:
            if co.id == id:
                contacts.remove(co)
                return {"Message": "remove successfully"}
        except:
            raise HTTPException(status_code=404, detail="the ID is not found")
           

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)