import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("titanic_model.pkl")

app = FastAPI()

class Passanger(BaseModel):
    Pclass: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
@app.post("/predict")
def predict_survival(data: Passanger):
    passanger_dt = data.model_dump()
    input_df = pd.DataFrame([passanger_dt])
    prediction = model.predict(input_df)[0]
    return "Survived" if prediction>=0.5 else "Died"
