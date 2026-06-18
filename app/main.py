from fastapi import FastAPI
from app.predictor import get_prediction

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Forex AI API running ✅"}

@app.get("/predict")
def predict(pair: str = "EURUSD"):
    result = get_prediction(pair)
    return result
