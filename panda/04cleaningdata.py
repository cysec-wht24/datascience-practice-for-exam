import pandas as pd
import numpy as np
from numpy import nan as NA

# ── 1. HANDLING MISSING DATA ─────────────────────────────────────
s = pd.Series([1, NA, 3.5, NA, 7])

print(s.isnull())          # detect NaN
print(s.dropna())          # remove NaN
print(s[s.notnull()])      # same as dropna

# ── 2. DATAFRAME dropna ──────────────────────────────────────────
df = pd.DataFrame([[1., 6.5, 3.],
                   [1., NA,  NA ],
                   [NA, NA,  NA ],
                   [NA, 6.5, 3. ]])

print(df.dropna())              # drop any row with NaN
print(df.dropna(how='all'))     # drop only all-NaN rows
print(df.dropna(axis=1, how='all'))  # drop all-NaN columns
print(df.dropna(thresh=2))      # keep rows with at least 2 non-NaN

# ── 3. FILLING MISSING DATA ──────────────────────────────────────
print(df.fillna(0))             # fill all NaN with 0
print(df.fillna({1: 0.5, 2: 0}))    # different value per column
print(df.fillna(method='ffill'))     # forward fill
print(df.fillna(df.mean()))          # fill with column mean

s = pd.Series([1., NA, 3.5, NA, 7])
print(s.fillna(s.mean()))       # fill with mean

# isnull()          → detect NaN
# dropna()          → remove NaN rows/cols
# dropna(how='all') → only drop all-NaN rows
# dropna(thresh=n)  → keep rows with n+ non-NaN
# fillna(0)         → fill with constant
# fillna(method='ffill') → forward fill
# fillna(df.mean()) → fill with mean