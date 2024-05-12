from typing import Union
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session 
from database import get_db
from utils import book_event
app = FastAPI()

@app.get("/{event_id}/{user_id}", response_model=dict)
def book(event_id: int, user_id: int, db: Session = Depends(get_db)):
    if book_event(db,user_id,event_id):
        return {"status": "success"}
    return {"status": "false"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}