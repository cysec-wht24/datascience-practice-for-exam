import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="yellow", edgecolor="black")

plt.title("# of pokemon by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")
# plt.tight_layout() # hehe
plt.show()