from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, constr
from typing import List
# To store a list of items(here users) in memory, we can use a python list or dict at module level
# although the data will be lost if we restart the application. 

app = FastAPI()

class UserRegistration(BaseModel):
    username: str
    email: EmailStr # Pydantic type that validates the field as a proper email address format.
    password: constr(min_length=8)  # constr (constrained string) is used to set length

# In-memory store (will be lost on restart)
registered_users: List[UserRegistration] = []

# exposing a post endpoint in FastAPI
@app.post("/register")
async def register_user(user:UserRegistration):
    for u in registered_users:
        if user.email == u.email:
            return{"success":False, "message":"Email already registered."}
    registered_users.append(user)
    return {"success": True, "message": "Registration is successful!"}
        
@app.get("/users")
def get_registered_users():
    return registered_users

"""
def defines a regular (synchronous) function.
async def defines an asynchronous function (coroutine) that can use await to perform non-blocking operations.
In FastAPI:

Use async def if your endpoint will perform I/O-bound operations (e.g., database queries, HTTP requests) using async libraries.
Use def for CPU-bound or simple logic that does not require async operations.
"""