from utils.loader import load_data
from features.indicators import add_indicators
from labeling.atr_label import create_labels
from models.xgb_model import train_xgb

df = load_data('data/EURUSD_H1_1000.csv')

df = add_indicators(df)
df = create_labels(df)

features = ['rsi', 'macd', 'atr']
X = df[features]
y = df['label']

model = train_xgb(X, y)

df['prob'] = model.predict_proba(X)[:,1]
