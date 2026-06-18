from sklearn.model_selection import TimeSeriesSplit

def split_data(X, y):

    tscv = TimeSeriesSplit(n_splits=5)

    for train_idx, test_idx in tscv.split(X):
        yield X.iloc[train_idx], X.iloc[test_idx], \
              y.iloc[train_idx], y.iloc[test_idx]
