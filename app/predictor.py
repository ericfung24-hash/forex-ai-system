import pandas as pd
import numpy as np
from app.model import load_model
from app.indicators import add_indicators

model = load_model()

def fake_data():
    # Render测试用（之后换真实数据）
    data = {
        "close": np.random.rand(100)*1.1 + 1,
        "high": np.random.rand(100)*1.1 + 1,
        "low": np.random.rand(100)*1.1 + 1,
    }
    return pd.DataFrame(data)

def get_prediction(pair):

    df = fake_data()   # ✅ 后面换真实数据
    df = add_indicators(df)

    features = ['rsi', 'macd', 'atr']
    X = df[features].iloc[-1:]

    prob = model.predict_proba(X)[0][1]

    price = df['close'].iloc[-1]
    atr = df['atr'].iloc[-1]

    if prob > 0.6:
        signal = "BUY"
        tp = price + 1.5 * atr
        sl = price - 1.0 * atr
    elif prob < 0.4:
        signal = "SELL"
        tp = price - 1.5 * atr
        sl = price + 1.0 * atr
    else:
        signal = "HOLD"
        tp = None
        sl = None

    return {
        "pair": pair,
        "signal": signal,
        "confidence": float(prob),
        "price": float(price),
        "tp": tp,
        "sl": sl
    }
