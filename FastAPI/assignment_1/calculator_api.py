from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalculateRequest(BaseModel):
    a: float
    b: float
    operation: str

@app.post("/calculator")
def calculator(request: CalculateRequest):
    if request.operation == "add":
        result = request.a + request.b
    elif request.operation == "subtract":
        result = request.a - request.b
    elif request.operation == "multiply":
        result = request.a * request.b
    elif request.operation == "divide":
        if request.b == 0:
            return {"error": "Division by zero is not allowed."}
        result = request.a / request.b
    else:
        return {"error": "Invalid operation."}
    return {"result": result}   

"""
The request variable is an instance of the CalculateRequest class, which is created by FastAPI from the incoming JSON data.

request.operation gets the operation type (like "add", "subtract", etc.) from the request body.
request.a and request.b get the two numbers sent in the request.

Example:
If you send this JSON:
{
  "a": 5,
  "b": 3,
  "operation": "add"
}

FastAPI creates request with:
request.a = 5
request.b = 3
request.operation = "add"
So, if request.operation == "add": checks if the user wants to add, and result = request.a + request.b performs the addition.
"""
