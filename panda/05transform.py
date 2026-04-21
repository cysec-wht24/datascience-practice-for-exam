import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name':   ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'dept':   ['HR', 'IT', 'HR', 'Finance', 'IT'],
    'salary': [50000, -999, 72000, 68000, -999],
    'score':  [85, 92, 85, 200, 78]   # 200 is outlier
})

# a) DUPLICATES
print(df.duplicated())
df = df.drop_duplicates()

# b) MAPPING - add grade column
df['grade'] = df['score'].map(
    lambda x: 'A' if x >= 90 else 'B' if x >= 75 else 'C')

# c) REPLACE sentinel -999 with NaN
df['salary'] = df['salary'].replace(-999, np.nan)

# d) RENAME columns
df = df.rename(columns={'name': 'Name', 'dept': 'Department'})

# e) BINNING salary into Low/Mid/High
df['sal_band'] = pd.cut(df['salary'],
                         bins=[0, 60000, 70000, 100000],
                         labels=['Low', 'Mid', 'High'])

# f) OUTLIER detection
print(df[df['score'] > 150])          # 200 is outlier

# g) PERMUTATION - shuffle rows
print(df.take(np.random.permutation(len(df))))

# h) DUMMY VARIABLES
print(pd.get_dummies(df['Department']))

print(df)

# 8 concepts
# a) duplicated/drop_duplicates → Alice+HR repeated
# b) map()        → score to grade
# c) replace()    → -999 to NaN
# d) rename()     → snake_case to Title
# e) pd.cut()     → salary bands
# f) outlier      → score=200 flagged
# g) permutation  → shuffle rows
# h) get_dummies  → dept one-hot