# Titanic Survival Predictor

A web app that predicts whether a passenger would have survived the Titanic sinking.
Built as the capstone project for the 100 Days of AI challenge.

## Project Structure

- data.csv                  → Titanic dataset 
- train_model.py            → Trains and saves the model
- main.py                   → FastAPI server
- titanic_model.joblib            → Trained RandomForest model
- model_features.joblib      → Feature names for prediction
- scaler.joblib                →  Scaler 
- requirements.txt          → Python dependencies
- render.yaml               → Render deployment config
- dvc.yaml                  → DVC pipeline (optional)
- frontend/
    - index.html           → Main prediction form
    - style.css             → Styling
    - script.js             → Handles form submission & API calls

## Tech stack
- **Model**: RandomForest 
- **Backend**: FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render (API) + GitHub Pages (frontend)
- **Versioning**: DVC 

## To use on your own computer

1. Clone the repo:
   ```bash
   git clone https://github.com/dagagalearn/100-days-of-ai.git
   cd 100-days-of-ai/day99
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (once):
   ```bash
   python train_model.py
   ```

4. Start the API server:
   ```bash
   uvicorn main:app --reload
   ```

5. Open `frontend/index.html` in your browser.

6. Enter passenger details and click "Predict".

## How It Works
1. User fills in passenger details (class, age, sex, fare, etc.)
2. Frontend sends a POST request to `/predict`
3. FastAPI loads the trained model and returns survival prediction
4. Result displayed with probability score

## Live Demo
- **API**:  — URL coming soon
- **Frontend**:  — URL coming soon

## Author
Dagaga Addisu
