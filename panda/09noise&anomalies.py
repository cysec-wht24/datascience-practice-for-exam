import pandas as pd
from scipy import stats

df = pd.DataFrame({
    'score': [80, 82, 85, 300, 78]  # 300 = outlier
})

# ── 1. OUTLIER ───────────────────────────────────────────────────
# IQR
Q1, Q3 = df['score'].quantile([0.25, 0.75])
IQR = Q3 - Q1
print(df[(df['score'] < Q1-1.5*IQR) | (df['score'] > Q3+1.5*IQR)])  # outlier

# Z-score
df['z'] = stats.zscore(df['score'])
print(df[df['z'].abs() > 2])                          # outlier via z

# ── 2. NOISE ─────────────────────────────────────────────────────
df['smoothed'] = df['score'].rolling(2).mean()         # moving average
df['clean']    = df['score'].apply(lambda x: df['score'].median() if x > 150 else x)

# ── 3. ANOMALY ───────────────────────────────────────────────────
tests = pd.DataFrame({'score': [88, 90, 15, 91]})     # 15 = anomaly
print(tests[tests['score'] < 40])                      # flag it

print(df)

# Outlier → IQR or Z-score    (300 flagged)
# Noise   → smooth or replace (300 → median)
# Anomaly → condition check   (15 flagged)