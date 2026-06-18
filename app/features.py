import numpy as np

def add_indicators(df):
    df['ema12'] = df['close'].ewm(span=12).mean()
    df['ema26'] = df['close'].ewm(span=26).mean()
    df['macd'] = df['ema12'] - df['ema26']

    delta = df['close'].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rs = gain / loss

    df['rsi'] = 100 - (100 / (1 + rs))
    df['atr'] = (df['high'] - df['low']).rolling(14).mean()

    return df

def build_features(data):

    base = add_indicators(data["EURUSD"].copy())

    # returns
    for sym, df in data.items():
        base[f'{sym}_ret'] = df['close'].pct_change()

    # USD strength
    base['usd_strength'] = (
        - base['EURUSD_ret']
        - base['GBPUSD_ret']
        + base['USDJPY_ret']
    ) / 3

    # risk_on
    base['risk_on'] = (
        base['US30_ret'] +
        base['GER40_ret'] +
        base['JPN225_ret']
    ) / 3 - base['VIX_ret']

    # gold vs usd
    base['gold_div'] = base['XAUUSD_ret'] + base['EURUSD_ret']

    base = base.dropna()

    return base
