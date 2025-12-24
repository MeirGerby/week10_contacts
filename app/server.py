from fastapi import FastAPI, HTTPException 
import uvicorn
from typing import List, Optional
from model import Contact


app = FastAPI()
 
@app.get('/contacts')
def get_all_contacts() -> List[Contact]:
    
    return contacts

@app.post("/contacts")
def create_new_contact(contact: Contact) -> dict:
    contacts.append(contact)
    return {"message": "the contact added successfully",
            "contact id": contact.id}

@app.put('/contacts/{id}')
def update_existing_contact(id: int, contact: Contact) -> Optional[dict]: 
    for i in range(len(contacts)):
        try:
            if contacts[i].id == id:
                contacts[i] = contact 
                return {'contacts': contacts} 
        except:
            raise HTTPException(status_code=404, detail="The ID not found")

@app.delete('/contacts/{id}')
def delete_contact(id: int, contact: Contact) -> Optional[dict]:
    for i in range(len(contacts)):    
        try:
            if contacts[i].id == id:
                contacts.remove(contacts[i])
                return {"Message": "remove successfully"}
        except:
            raise HTTPException(status_code=404, detail="the ID is not found")


def run_server():
    uvicorn.run(app, host="localhost", port=8000)
     