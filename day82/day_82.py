from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Car(BaseModel):
    brand: str
    model: str
    year: int
    price: float
    is_electric: bool = False

@app.post("/add-car")
def create_car(car: Car):
    return {
        "status": "Car added successfully",
        "data": car
    }
