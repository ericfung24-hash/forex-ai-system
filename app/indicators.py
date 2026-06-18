import pandas as pd

def add_indicators(df):

    df['ema_12'] = df['close'].ewm(span=12).mean()
    df['ema_26'] = df['close'].ewm(span=26).mean()
    df['macd'] = df['ema_12'] - df['ema_26']

    delta = df['close'].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()

    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))

    df['atr'] = (df['high'] - df['low']).rolling(14).mean()

    return df.dropna()
