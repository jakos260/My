import time as tm
import numpy as np
import scipy.interpolate as interp
import scipy.signal as sg
import matplotlib.pyplot as plt

def our_interpolate_2D(grid, values, points, mode):
    #mode = linear/nearest
    #grid - regular grid YxYx2
    #values - input values YxX
    #points - locations to intterpolate (Nx2)
    z_in = np.zeros(shape=())
    if mode == 'linear':
        pass
    elif mode == 'nearest':
        pass
    return z_in

start = -2*np.pi
stop = 2*np.pi
step = 0.2
samples = int((stop - start) / step)

x = np.linspace(start, stop, samples)
y = np.linspace(start, stop, samples)

xs, ys = np.meshgrid(x, y)
zs = np.cos(xs)*np.sin(ys)


rows = 1
cols = 3

plt.figure(dpi=150, figsize=(12, 5))


plt.subplot(rows, cols, 1)
plt.title('before')
plt.imshow(zs, cmap='gray')
plt.grid(False)
plt.axis('off')

plt.subplot(rows, cols, 2)
plt.title('linear')
plt.imshow(zs, cmap='gray')
plt.grid(False)
plt.axis('off')

plt.subplot(rows, cols, 3)
plt.title('knn')
plt.imshow(zs, cmap='gray')
plt.grid(False)
plt.axis('off')

plt.show()

