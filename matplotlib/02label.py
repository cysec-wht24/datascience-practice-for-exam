import matplotlib.pyplot as plt
import numpy as np

x = np.array([2024, 2025, 2026, 2027])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([10, 56, 43, 3])
y3 = np.array([27, 12, 67, 24])

plt.xlabel("Year", fontsize=20,
                  family="Arial",
                  fontweight="bold",
                  color="#2dbefc")

plt.ylabel("Students", fontsize=20,
                   family="Arial",
                   fontweight="bold",
                   color="#2dbefc")

plt.tick_params(axis="both",
                colors="red")

# customization
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.show()