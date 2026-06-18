def generate_signal(row):

    p = row['prob']

    if p > 0.6 and row['atr'] > row['atr'].rolling(50).mean():
        return 1
    elif p < 0.4:
        return -1
    else:
        return 0
