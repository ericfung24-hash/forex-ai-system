import numpy as np
import pandas as pd

def detect_regime(df):

    score = 0

    equity = df[['US30_ret','GER40_ret','JPN225_ret']].mean(axis=1)
    score += np.where(equity > 0, 1, -1)

    score += np.where(df['VIX_ret'] < 0, 1, -1)
    score += np.where(df['XAUUSD_ret'] < 0, 1, -1)
    score += np.where(df['usd_strength'] < 0, 1, -1)

    df['risk_score'] = score

    df['regime'] = np.where(score >= 2, 'RISK_ON',
                     np.where(score <= -2, 'RISK_OFF', 'NEUTRAL'))

    return df

def currency_strength(df):

    strength = pd.DataFrame(index=df.index)

    strength['USD'] = (
        df['USDJPY_ret']
        - df['EURUSD_ret']
        - df['GBPUSD_ret']
        - df['AUDUSD_ret']
    )

    strength['EUR'] = df['EURUSD_ret']
    strength['GBP'] = df['GBPUSD_ret']
    strength['AUD'] = df['AUDUSD_ret']
    strength['JPY'] = -df['USDJPY_ret']

    strongest = strength.iloc[-1].idxmax()
    weakest = strength.iloc[-1].idxmin()

    return strength, strongest, weakest
