import pandas as pd

df = pd.DataFrame({
    'name':   ['Alice', 'Bob', 'Charlie', 'David'],
    'score':  [30, 55, 75, 90]
})

# equal-width (same range)
df['cut']  = pd.cut(df['score'],  bins=[0,50,70,100], labels=['Low','Mid','High'])

# equal-frequency (same count)
df['qcut'] = pd.qcut(df['score'], q=2, labels=['Low','High'])

print(df)

# pd.cut()  → equal-width  (same range per bin)
# pd.qcut() → equal-freq   (same count per bin)