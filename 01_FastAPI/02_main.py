from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return {"message": "Hello,World!"}

@app.get("/aditya")
def test_1():
    return {"message": "I am a Data Engineer"}

people = [
        {"name": "Aditya", "city": "Bangalore", "profession": "Data Engineer"},
        {"name": "Josh", "city": "Mumbai", "profession": "Data Scientist"},
        {"name": "Sonia", "city": "Delhi", "profession": "Data Analyst"}
]

@app.get("/people")
def get_people():
    return {"people": people}

# parameterized endpoint to search for a person by name
@app.get("/people/{name}")
def people_search(name: str):
    for person in people:
        if person["name"].lower() == name.lower():
            return {"person":person}

@app.post("/add_people")
def add_people_diff(person: dict):
    people.append(person)
    return {"message": "Person added successfully", "people": people}

@app.post()

# In  FastAPI, Uvicorn is the lightning-fast web server that actually runs your application. While FastAPI defines 
# the routes, logic, and data validation, it does not have a built-in server to listen for network requests; 
# it relies on Uvicorn to handle that low-level communication.

# To run the FastAPI application, you typically use Uvicorn from the command line like this:
# uvicorn main:app 
#     or
# uvicorn main:app --reload(auto-restart on code change)