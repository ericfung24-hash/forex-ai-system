from xgboost import XGBClassifier

def train_xgb(X_train, y_train):

    model = XGBClassifier(
        max_depth=4,
        n_estimators=200,
        learning_rate=0.05
    )

    model.fit(X_train, y_train)
    return model
