import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.3, 3, 0.01)
y = 1/x
plt.plot(x, y)

x1 = np.arange(0, 2, 0.01)
y1 = 2 - x1
plt.plot(x1, y1)
plt.plot([1], [1], 'ro')
plt.annotate('A', xy=(1.03, 1.03))
plt.annotate('C', xy=(2.03, 0.03))
plt.annotate('D', xy=(3.03, 0.43))

plt.show()