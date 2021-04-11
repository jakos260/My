import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(12,6))
plt.step(x, y, where='post', color = 'g')
plt.grid()
plt.show()