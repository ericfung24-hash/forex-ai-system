import pandas as pd

def load_data(path):

    try:
        df = pd.read_csv(path, encoding='utf-8')
    except:
        try:
            df = pd.read_csv(path, encoding='utf-16')
        except:
            df = pd.read_csv(path, encoding='latin1')

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp').reset_index(drop=True)

    return df
