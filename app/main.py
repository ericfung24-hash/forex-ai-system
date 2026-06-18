from fastapi import FastAPI
from app.predictor import predict

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Forex AI running ✅"}

@app.get("/predict")
def get_prediction():
    return predict()
