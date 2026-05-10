from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message":"The app is running well!"}

@app.get("/predict/{number}")
def predict(number: int):
    prediction = 2*number
    return {"number": number,"prediction":prediction}
