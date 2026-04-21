import matplotlib.pyplot as plt
import numpy as np

# Histogram = A visual representation of the distribution of quantitative data.
#             They group values into bins (intervals)
#             and counts how many fall in each range.

# with numpy you can generate random numbers

scores = np.random.normal(loc=80, scale=10, size=100)
# loc = location of center
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=20, color="red", edgecolor="blue")

plt.title("Exam Scores")
plt.xlabel("Score")
plt.ylabel("# of students")



plt.show()