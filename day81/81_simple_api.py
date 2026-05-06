from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def default():
    return {"Message": "Hello World!"}

@app.get("/{name}")
def hello_func(name:str):
    return {"message": f"You are: {name}."}
