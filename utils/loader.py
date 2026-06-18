import pandas as pd

def load_data(path):

    # ✅ 处理编码
    try:
        df = pd.read_csv(path, encoding='utf-8')
    except:
        try:
            df = pd.read_csv(path, encoding='utf-16')
        except:
            df = pd.read_csv(path, encoding='latin1')

    # ✅ 标准化列名（全部转小写）
    df.columns = [c.lower() for c in df.columns]

    # =========================
    # ✅ 1️⃣ 情况：已有 timestamp
    # =========================
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])

    # =========================
    # ✅ 2️⃣ 情况：date + time
    # =========================
    elif 'date' in df.columns and 'time' in df.columns:
        df['timestamp'] = pd.to_datetime(df['date'] + ' ' + df['time'])

    # =========================
    # ✅ 3️⃣ 情况：只有 time
    # =========================
    elif 'time' in df.columns:
        df['timestamp'] = pd.to_datetime(df['time'])

    # =========================
    # ✅ 4️⃣ fallback（第一列当时间）
    # =========================
    else:
        df['timestamp'] = pd.to_datetime(df.iloc[:,0])

    # ✅ 设索引
    df = df.sort_values('timestamp')
    df = df.set_index('timestamp')

    return df
