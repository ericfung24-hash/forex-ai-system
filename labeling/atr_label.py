import numpy as np

def create_labels(df):

    future_return = df['close'].shift(-1) - df['close']
    thr = 0.5 * df['atr']

    y = np.where(future_return > thr, 1,
        np.where(future_return < -thr, -1, 0)
    )

    df['label'] = y
    return df.dropna()
