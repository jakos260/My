import time
import numpy as np
import matplotlib.pyplot as plt
import torch as tc
import torch.nn.functional as F
from scipy import signal


step = 0.001
# errors = []
# steps = np.arange(0.0001, 1, 0.0001)
# for i in range(len(steps)):
# step = steps[i]
start = -3
stop = 3
samples = int((stop - start) / step)

x = np.linspace(start, stop, samples)
print(x.dtype)
y = x**2 + 3*x + 5
dy_real = 2*x + 3
dy_numerical = np.gradient(y, step)

nx = input('___next___')

def mse(x1, x2):
    return np.mean(np.sqrt((x1 - x2)**2))
error = mse(dy_real, dy_numerical)
# errors.append(error)
print("MSE: ", mse(dy_real, dy_numerical))
plt.figure(dpi=200)
plt.plot(x, y, "r-")
plt.plot(x, dy_real, "b-")
plt.plot(x, dy_numerical, "g-")
plt.grid(True)
plt.xlim([start, stop])
# plt.figure()
# plt.plot(steps, errors, "r-")
# plt.grid(True)
# plt.show()

nx = input('___next___')

step = 0.01
start = -3
stop = 3
samples = int((stop - start) / step)
noise_level = 0.0001

x = np.linspace(start, stop, samples)
y = x**2 + 3*x + 5
y_noise = y + np.random.randn(x.shape[0])*noise_level
dy_real = 2*x + 3
dy_numerical = np.gradient(y_noise, step)

error = mse(dy_real, dy_numerical)
print("MSE function: ", mse(y, y_noise))
print("MSE derivative: ", mse(dy_real, dy_numerical))
plt.figure(dpi=100)
plt.plot(x, y, "r-")
plt.plot(x, y_noise, "y-")
plt.plot(x, dy_real, "b-")
plt.plot(x, dy_numerical, "g-")
plt.grid(True)
plt.xlim([start, stop])

nx = input('___next___')

signal = np.array([4, 7, 2, -2, 4], dtype=np.float32)
result = np.gradient(signal)
print(result)

nx = input('___next___')

x1 = np.array([2, 3, 5, 1, 2, 6], dtype=np.float32)
x2 = np.array([1, 2, 3], dtype=np.float32)

# 3 2 1

# 0 2 3 5 1 2 6
# 3 2 1

# 2 3 5 1 2 6
# 3 2 1

# 2 3 5 1 2 6
#   3 2 1

# 2 3 5 1 2 6
#     3 2 1

# 2 3 5 1 2 6
#       3 2 1

# 2 3 5 1 2 6
#         3 2 1

# x 17 20 19 13 x

result = signal.convolve(x1, x2)
print(result)

result = signal.convolve(x2, x1)
print(result)

