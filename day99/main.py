from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import joblib

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

model = joblib.load("titanic_model.joblib")
features = joblib.load("model_features.joblib")
scaler = joblib.load("scaler.joblib")
#['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_female', 'Sex_male']

class Passenger(BaseModel):
  Pclass:int
  Age: float
  SibSp: int
  Parch: int
  Fare: float
  Sex_female: int
  Sex_male: int

@app.get("/")
def home():
  return {
      "message": "Welcome to Titanic Predictor Model",
      "endpoints": {
          "/health": "Check if the API is up",
          "/predict": "Get Predictions"
      }
  }

@app.get("/health")
def health():
  return {
      "message": "Running very well",
      "is_running": True
  }

@app.post("/predict")
def predict(passenger: Passenger):
  input_data = []
  for col in features:
    input_data.append(getattr(passenger,col))
  X = np.array([input_data])
  X_scaled = scaler.transform(X)
  prediction = model.predict(X_scaled)
  prediction_probability = model.predict_proba(X_scaled)
  if prediction[0]==1:
    prediction_word = "Survived"
  else:
    prediction_word = "Not Survived"
  return {
      "prediction": prediction_word,
      "probability_not_survived": float(np.round(prediction_probability[0][0],3)),
      "probability_survived": float(np.round(prediction_probability[0][1],3))
  }
