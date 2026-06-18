from app.data_loader import load_all
from app.features import build_features
from app.regime import detect_regime, currency_strength
from app.models import load_models

models = load_models()

def predict():

    data = load_all()

    df = build_features(data)
    df = detect_regime(df)

    strength_df, strongest, weakest = currency_strength(df)

    latest = df.iloc[-1:]

    features = [
        'rsi','macd','atr',
        'usd_strength','risk_on','gold_div'
    ]

    X = latest[features]

    results = {}

    for pair, model in models.items():

        prob = model.predict_proba(X)[0][1]

        if prob > 0.6:
            signal = "BUY"
        elif prob < 0.4:
            signal = "SELL"
        else:
            signal = "HOLD"

        results[pair] = {
            "signal": signal,
            "confidence": float(prob)
        }

    return {
        "regime": df['regime'].iloc[-1],
        "strongest": strongest,
        "weakest": weakest,
        "signals": results
    }
