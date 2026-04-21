import pandas as pd

df = pd.DataFrame({
    'name':   ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'dept':   ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'salary': [50000, 72000, 68000, 85000, 60000]
})

print(df.head())      # first 5 rows
print(df.tail())      # last 5 rows
print(df.info())      # structure - dtypes, non-null count
print(df.describe())  # stats - mean, std, min, max

# 4 methods 
# head()     → first 5 rows
# tail()     → last 5 rows
# info()     → structure (dtypes, nulls)
# describe() → stats (mean, std, min, max)