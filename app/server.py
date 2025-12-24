from fastapi import FastAPI, HTTPException 
import uvicorn
from typing import List, Optional
from model import Contact 
from manage_db import MannageDB

cursor = MannageDB.create_corsor()

app = FastAPI()
 
@app.get('/contacts')
def get_all_contacts():
    return MannageDB.get_contacts(cursor)

@app.post("/contacts")
def create_new_contact(contact: Contact):
    try:
        MannageDB.create(cursor, contact.id, contact.first_name, contact.last_name, contact.phone_number)
        return {"seccuss": f"contact id {contact.id}"}
    except:
        raise HTTPException(status_code=404, detail="The contact not found")
@app.put('/contacts/{id}')
def update_existing_contact(id: int, contact: Contact): 
    try:
        MannageDB.update(cursor, contact.id, contact.first_name, contact.last_name, contact.phone_number)
    except:
        raise HTTPException(status_code=404, detail="The contact not found")

@app.delete('/contacts/{id}')
def delete_contact(id: int, contact: Contact) -> Optional[dict]:
    try:
        MannageDB.delete
        return {"Message": "remove successfully"}
    except:
        raise HTTPException(status_code=404, detail="the ID is not found")


def run_server():
    uvicorn.run(app, host="localhost", port=8000)
     