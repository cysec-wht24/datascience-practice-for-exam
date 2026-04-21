import matplotlib.pyplot as plt
import numpy as np

# Bar chart = Circular chart divided into slices to show percentage
#             Good for visualizing distribution among categories.

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 250, 275, 225])
colors = ["red", "yellow", "blue", "green"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                #colors=colors,
                explode=[0, 0, 0, 2],
                shadow=True,
                startangle=42
                )

plt.title("First pie chart")

plt.show()
