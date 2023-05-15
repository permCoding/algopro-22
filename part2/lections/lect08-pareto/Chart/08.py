import matplotlib.pyplot as plt
import numpy as np


disk_sizes = np.asarray([128, 256, 320, 512])
prices = np.asarray([1020, 2000, 1950, 3200])
sales = np.asarray([76, 305, 212, 142])

plt.scatter(x=disk_sizes, y=prices, s=sales)
plt.show()
