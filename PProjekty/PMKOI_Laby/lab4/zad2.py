import time as tm
import numpy as np
import scipy.interpolate as interp
import scipy.signal as sg
import matplotlib.pyplot as plt

start = 0
stop = 2*np.pi
step = 0.5

x = np.arange(start, stop + step, step)
# y = x**3 - 4*x**2 + 40*x - 84
y = np.cos(x)

y_interp_linear = interp.interp1d(x, y, kind='linear')
y_interp_cubic = interp.interp1d(x, y, kind='cubic')
y_interp_nearest = interp.interp1d(x, y, kind='nearest')
y_interp_rbf = interp.Rbf(x, y, function='thin-plate')

divider = 3
x_dense = np.arange(start, stop + step/divider, step/divider)
y_linear = y_interp_linear(x_dense)
y_cubic = y_interp_cubic(x_dense)
y_nearest = y_interp_nearest(x_dense)
y_rbf = y_interp_rbf(x_dense)

# podwójnie pierwsza pochodna
conv1 = [-1, 0, 1]
h = step/divider
dy1_int_linear = sg.convolve((sg.convolve(y_linear, conv1)/(2*h)), conv1)/(2*h)
dy1_int_cubic = sg.convolve((sg.convolve(y_cubic, conv1)/(2*h)), conv1)/(2*h)
dy1_int_nearest = sg.convolve((sg.convolve(y_nearest, conv1)/(2*h)), conv1)/(2*h)
dy1_int_rbf = sg.convolve((sg.convolve(y_rbf, conv1)/(2*h)), conv1)/(2*h)

#druga pochodna
conv2 = [1, -2, 1]
dy2_int_linear = sg.convolve(y_linear, conv2)/(h**2)
dy2_int_cubic = sg.convolve(y_cubic, conv2)/(h**2)
dy2_int_nearest = sg.convolve(y_nearest, conv2)/(h**2)
dy2_int_rbf = sg.convolve(y_rbf, conv2)/(h**2)

# dy = 6*x_dense + 8
dy = np.sin(x_dense)

plt.figure(dpi=150, figsize=(12,5))
plt.subplot(1, 4, 1)
plt.title('nn', loc='center', fontsize=12)
plt.plot(x_dense, dy1_int_nearest[2:len(dy1_int_nearest)-2], "bo", label='ppp', ms=5)
plt.plot(x_dense, dy2_int_nearest[1:len(dy2_int_nearest)-1], "b*", label='dp', mec='k', mew=0.5)
plt.plot(x_dense, dy, "r-", label='orginal dy')
plt.legend()
plt.grid(True)
plt.xlim([start, stop])

plt.subplot(1, 4, 2)
plt.title('linear', loc='center', fontsize=12)
plt.plot(x_dense, dy1_int_linear[2:len(dy1_int_linear)-2], "go", label='ppp', ms=5)
plt.plot(x_dense, dy2_int_linear[1:len(dy2_int_linear)-1], "g*", label='dp', mec='k', mew=0.5)
plt.plot(x_dense, dy, "r-", label='orginal dy')
plt.legend()
plt.grid(True)
plt.xlim([start, stop])

plt.subplot(1, 4, 3)
plt.title('cubic', loc='center', fontsize=12)
plt.plot(x_dense, dy1_int_cubic[2:len(dy1_int_cubic)-2], "yo", label='ppp', ms=5)
plt.plot(x_dense, dy2_int_cubic[1:len(dy2_int_cubic)-1], "y*", label='dp', mec='k', mew=0.5)
plt.plot(x_dense, dy, "r-", label='orginal dy')
plt.legend()
plt.grid(True)
plt.xlim([start, stop])

plt.subplot(1, 4, 4)
plt.title('rbf', loc='center', fontsize=12)
plt.plot(x_dense, dy1_int_rbf[2:len(dy1_int_rbf)-2], "mo", label='ppp', ms=5)
plt.plot(x_dense, dy2_int_rbf[1:len(dy2_int_rbf)-1], "m*", label='dp', mec='k', mew=0.5)
plt.plot(x_dense, dy, "r-", label='orginal dy')
plt.legend()
plt.grid(True)
plt.xlim([start, stop])

plt.show()