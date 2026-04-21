import matplotlib.pyplot as plt
import numpy as np

x = np.array([2024, 2025, 2026, 2027])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([10, 56, 43, 3])
y3 = np.array([27, 12, 67, 24])

line_style = dict(marker="v", 
                  ms=30, 
                  markerfacecolor="red", 
                  markeredgecolor="purple", 
                  linestyle="dashed",
                  linewidth=4)

# customization
plt.plot(x, y1, color="green" ,**line_style)
plt.plot(x, y2, color="red" ,**line_style)
plt.plot(x, y3, color="blue", **line_style)

plt.show()