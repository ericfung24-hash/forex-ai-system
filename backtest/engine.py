def backtest(df):

    balance = 10000
    position = 0

    for i in range(len(df)):

        signal = df.iloc[i]['signal']
        price = df.iloc[i]['close']

        if signal == 1:
            position = 1
            entry = price

        elif signal == -1:
            position = -1
            entry = price

        if position == 1:
            pnl = price - entry
        elif position == -1:
            pnl = entry - price

        balance += pnl

    return balance
