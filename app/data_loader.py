import pandas as pd
import os

DATA_DIR = "data"

def read_csv_safe(path):

    try:
        return pd.read_csv(path, encoding='utf-8')
    except:
        try:
            return pd.read_csv(path, encoding='utf-16')
        except:
            return pd.read_csv(path, encoding='latin1')

def load_symbol(symbol, tf="H1"):
    for f in os.listdir(DATA_DIR):
        if symbol in f and tf in f:
            path = os.path.join(DATA_DIR, f)

            df = read_csv_safe(path)

            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = df.sort_values('timestamp').set_index('timestamp')

            return df

    raise Exception(f"{symbol} not found")

def load_all():
    symbols = [
        "EURUSD","GBPUSD","USDJPY","AUDUSD",
        "US30","GER40","JPN225",
        "UK100","EUSTX50","XAUUSD","VIX"
    ]

    data = {}
    for sym in symbols:
        data[sym] = load_symbol(sym)

    return data
