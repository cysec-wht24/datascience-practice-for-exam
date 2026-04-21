import pandas as pd
import numpy as np

# ── a) STACK / UNSTACK ───────────────────────────────────────────
data = pd.DataFrame([[0,1,2],[3,4,5]],
                    index=['Ohio','Colorado'],
                    columns=['one','two','three'])

stacked = data.stack()     # wide → long (columns become rows)
print(stacked)
print(stacked.unstack())   # long → wide (back to original)

# ── b) PIVOT: long → wide ────────────────────────────────────────
df = pd.DataFrame({
    'Student': ['Rahul','Rahul','Anita','Anita'],
    'Subject': ['Math','Science','Math','Science'],
    'Marks':   [85, 90, 78, 82]
})

wide = df.pivot(index='Student', columns='Subject', values='Marks')
print(wide)

# ── c) MELT: wide → long ─────────────────────────────────────────
print(wide.reset_index().melt(id_vars='Student',
                               var_name='Subject',
                               value_name='Marks'))

# stack()    → columns into rows
# unstack()  → rows into columns
# pivot()    → long to wide
# melt()     → wide to long