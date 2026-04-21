import numpy as np
import matplotlib.pyplot as plt

categories = np.array(["Grains", "Fruit", "Vegetables", "Dairy", "Protein", "Nuts", "Legumes", "Snacks"])
values = np.array([4, 3, 2, 5, 3, 1, 4, 2])

# plt.bar(categories, values, color="skyblue")
plt.barh(categories, values, color="skyblue")

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()