import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age':  [15, 25, 45, 70],
    'score':[10, 20, 30, 40]
})

# a) CLASSING - age groups using pd.cut - aka categorization or data binning
# -> involves converting continuous numerical data into discrete categories or groups.
# -> Useful for grouping ages, income brackets, or performance scores into manageable categories for analysis or visualization
df['age_group'] = pd.cut(df['age'],
                          bins=[0, 20, 40, 60, 100],
                          labels=['Child','Young','Adult','Senior'])

# b) MANUAL STANDARDIZATION - z = (x - mean) / std
df['score_manual'] = (df['score'] - df['score'].mean()) / df['score'].std()

# c) SKLEARN STANDARDIZATION
df['score_sklearn'] = StandardScaler().fit_transform(df[['score']])

print(df)

# pd.cut()        → classing  (group into categories)
# (x-mean)/std    → manual standardization
# StandardScaler  → sklearn standardization