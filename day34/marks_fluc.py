import matplotlib.pyplot as plt
import numpy as np

average_mark = np.array([96, 93, 97, 97])
years = np.array([2023, 2024, 2025, 2026])

plt.suptitle("My marks fluctuations")

plt.subplot(2,1,1)
plt.bar(years, average_mark, width=0.3, color="green", edgecolor="red")
plt.ylim(90, 100)
plt.title("Bargraph")

plt.subplot(2,1,2)
plt.hist(average_mark, color="green", rwidth=0.8, edgecolor="red")
plt.title("Histogram")

plt.tight_layout()
plt.show()
