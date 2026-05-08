from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2 
from psycopg2.extras import RealDictCursor

app = FastAPI()

import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise ValueError("DATABASE_URL environment variable not set")

class Item(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

def get_connection_url():
    conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
    return conn

def save_item_to_file(data):
    with open("item.txt", "a") as file:
        file.write(f"{data.name}, {data.description}, {data.price}, {data.quantity}\n")

@app.post("/items/db/insert")
def store_item_in_db(item: Item):
    conn = get_connection_url()
    cursor = conn.cursor()
    insert_query = """
        INSERT INTO item (name, description, price, quantity)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (item.name, item.description, item.price, item.quantity))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Item data saved to database successfully", "item": item}

@app.post("/items/")
def create_item(item: Item):
    save_item_to_file(item)
    return {"message": "Item data saved to file successfully", "item": item}

"""
Here, we are using Neon which is a serverless Postgres database and it provides
free instances. We will connect to it using psycopg2, a popular PostgreSQL 
adapter for Python.
"""