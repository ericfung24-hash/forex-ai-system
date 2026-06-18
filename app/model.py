import joblib

def load_models():
    return {
        "EURUSD": joblib.load("models/eurusd.pkl"),
        "GBPUSD": joblib.load("models/gbpusd.pkl"),
        "USDJPY": joblib.load("models/usdjpy.pkl"),
        "AUDUSD": joblib.load("models/audusd.pkl"),
    }
