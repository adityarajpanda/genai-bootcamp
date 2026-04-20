from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return {"message": "Hello,World!"}

@app.get("/aditya")
def test_1():
    return "I am a Data Engineer"


# In  FastAPI, Uvicorn is the lightning-fast web server that actually runs your application. While FastAPI defines 
# the routes, logic, and data validation, it does not have a built-in server to listen for network requests; 
# it relies on Uvicorn to handle that low-level communication.

# To run the FastAPI application, you typically use Uvicorn from the command line like this:
# uvicorn main:app 
#     or
# uvicorn main:app --reload(auto-restart on code change)