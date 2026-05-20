from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()
model = joblib.load("titanic_model.joblib")
@app.get("/")
def home():
  return{
      "message": "Titanic prediction model",
      "endpoints": {
          "health/: ": "Check Model Healthy",
          "predict/: ": "Prediction endpoint"
      }
  }

@app.get("/health")
def health():
  return {
      "message": "Running very well",
      "is_running": True
  }

class Passenger(BaseModel):
  Pclass: int
  Age: float
  SibSp: int
  Parch: int
  Fare: float
  Sex_male: int #0 for female and 1 for male

@app.post("/predict")
def predict(passenger: Passenger):
  features = np.array([[
        passenger.Pclass,
        passenger.Age,
        passenger.SibSp,
        passenger.Parch,
        passenger.Fare,
        passenger.Sex_male
    ]])
  
  prediction = model.predict(features)[0]
  probability = model.predict_proba(features)[0]

  return{
    "prediction": int(prediction),
    "probability of the prediction": float(probability[1])
  }
