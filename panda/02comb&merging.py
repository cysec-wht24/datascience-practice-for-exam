import pandas as pd
import numpy as np

# ── 1. MERGE (SQL-style joins) ───────────────────────────────────
df1 = pd.DataFrame({'key': ['a', 'b', 'b', 'c'], 'data1': [1, 2, 3, 4]})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],       'data2': [10, 20, 30]})

print(pd.merge(df1, df2, on='key', how='inner'))  # only matching keys
print(pd.merge(df1, df2, on='key', how='left'))   # all from left
print(pd.merge(df1, df2, on='key', how='right'))  # all from right
print(pd.merge(df1, df2, on='key', how='outer'))  # all from both

# ── 2. MERGE ON INDEX ────────────────────────────────────────────
left  = pd.DataFrame({'key': ['a', 'b', 'c'], 'val': [1, 2, 3]})
right = pd.DataFrame({'group': [10, 20]}, index=['a', 'b'])  # index = key

print(pd.merge(left, right, left_on='key', right_index=True, how='left'))

# ── 3. CONCAT ────────────────────────────────────────────────────
s1 = pd.Series([1, 2], index=['a', 'b'])
s2 = pd.Series([3, 4], index=['c', 'd'])

print(pd.concat([s1, s2]))           # stack vertically (axis=0)
print(pd.concat([s1, s2], axis=1))   # side by side   (axis=1)

# with keys → hierarchical index
print(pd.concat([s1, s2], keys=['first', 'second']))

# ── 4. COMBINE FIRST (patch NaN values) ─────────────────────────
s1 = pd.Series([1, np.nan, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30],   index=['a', 'b', 'c'])

# NaN in s1 gets filled by s2
print(s1.combine_first(s2))   # output: a=1, b=20, c=3

# 4 concepts, one line each:

# | Concept               | What it does                  |
# |-----------------------|-------------------------------|
# | merge                 | Join tables on a common key   |
# | merge(right_index=True) | Use index as the join key   |
# | concat                | Stack Series/DataFrames       |
# | combine_first         | Fill NaN from another object  |