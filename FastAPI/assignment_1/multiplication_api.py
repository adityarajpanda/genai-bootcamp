from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MultiplyRequest(BaseModel):
    a: int
    b: int

@app.post("/multiply")
def multiply(request: MultiplyRequest):
    return {"result": request.a * request.b}

# FastAPI's automatic validation will return a clear error message if the input is not valid, so no extra code is needed for that.