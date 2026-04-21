import pandas as pd

# ─────────────────────────────────────────
# 1. SERIES — a single column of data
# ─────────────────────────────────────────
# Think of it like a list, but with labels (index)

marks = pd.Series([88, 92, 75, 60], index=["Maths", "Science", "English", "History"])
print(marks)
print(marks["Maths"])       # access by label
print(marks[0])             # access by position

# WHY index? So you can access data by name, not just position.


# ─────────────────────────────────────────
# 2. DATAFRAME — multiple columns = a table
# ─────────────────────────────────────────
# WHY {}  → because you're passing a dictionary: { "column_name": [values] }
# WHY []  → because each column's values are a list

data = {
    "Name":   ["Alice", "Bob", "Charlie"],   # column 1
    "Age":    [22, 25, 23],                  # column 2
    "Score":  [88, 92, 75],                  # column 3
}

df = pd.DataFrame(data)
print(df)

# Series  = one column  (1D)
# DataFrame = many columns (2D table)
# A DataFrame is basically multiple Series glued together.


# ─────────────────────────────────────────
# 3. ACCESSING DATA
# ─────────────────────────────────────────

print(df["Name"])              # single column  → returns a Series
print(df[["Name", "Score"]])   # multiple columns → still a DataFrame (double bracket needed)

print(df.loc[0])               # row by label/index
print(df.iloc[1])              # row by position (integer)

print(df.loc[0, "Score"])      # specific cell: row 0, column Score


# ─────────────────────────────────────────
# 4. BASIC INFO
# ─────────────────────────────────────────

print(df.shape)        # (rows, columns)
print(df.dtypes)       # data type of each column
print(df.head(2))      # first 2 rows
print(df.tail(1))      # last 1 row
print(df.describe())   # stats: mean, min, max etc (numeric columns only)


# ─────────────────────────────────────────
# 5. FILTERING ROWS (most used thing in pandas)
# ─────────────────────────────────────────

print(df[df["Score"] > 80])            # rows where score > 80
print(df[df["Name"] == "Alice"])       # find specific person


# ─────────────────────────────────────────
# 6. ADDING / MODIFYING COLUMNS
# ─────────────────────────────────────────

df["Passed"] = df["Score"] >= 75       # new column based on condition
df["Score"] = df["Score"] + 5          # update existing column
print(df)


# ─────────────────────────────────────────
# 7. HANDLING MISSING DATA
# ─────────────────────────────────────────

import numpy as np

df2 = pd.DataFrame({
    "Name":  ["Alice", "Bob", "Charlie"],
    "Score": [88, None, 75]
})

print(df2.isnull())              # where are the NaNs?
print(df2.dropna())              # remove rows with NaN
print(df2.fillna(0))             # replace NaN with 0


# ─────────────────────────────────────────
# 8. READ / WRITE FILES
# ─────────────────────────────────────────

# df.to_csv("output.csv", index=False)      # save to CSV
# df = pd.read_csv("data.csv")              # load from CSV
# df = pd.read_excel("data.xlsx")           # load from Excel


# ─────────────────────────────────────────
# QUICK CHEATSHEET
# ─────────────────────────────────────────
# pd.Series([...])              → 1D labeled array
# pd.DataFrame({...})           → 2D table
# df["col"]                     → one column (Series)
# df[["col1","col2"]]           → multiple columns (DataFrame)
# df.loc[row, col]              → by label
# df.iloc[row, col]             → by number
# df[df["col"] > x]             → filter rows
# df["new"] = ...               → add column
# df.dropna() / df.fillna(x)   → handle missing