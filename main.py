from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

users_db = {
    "Hamza": {"password": "Farah"},
    "user2": {"password": "password2"}
}

class User(BaseModel):
    username: str
    password: str

class Ticket(BaseModel):
    date: str
    amount: int

@app.post("/signin/")
async def login(user: User):
    if user.username in users_db and users_db[user.username]["password"] == user.password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@app.post("/ticket/")
async def book_ticket(ticket: Ticket):
    return {"message": "Ticket booked successfully!"}

