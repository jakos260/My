import time as tm
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt

def our_interpolation(x, y, step,x_new, mode):
    # mode = linear/nearest

    y_new = np.zeros(len(x_new))
    a = int(step / (x_new[2] - x_new[1])) # new step

    if mode == 'linear':
        for i in range(len(x) - 1):
            for j in range(a):
                if a * i + j < len(x_new):
                    y_new[a*i+j] = y[i] + ((y[i+1] - y[i]) / (x[i+1] - x[i])) * (x_new[a*i+j] - x[i]) # y nowy = ostatni mijany y stary + wartość

    elif mode == 'nearest':
        for i in range(len(x) - 1):
            for j in range(a):
                if a * i + j < len(x_new):
                    if np.abs(x[i] - x_new[a * i + j]) <= np.abs(x[i + 1] - x_new[a * i + j]):
                        # print('|x-x_n|', np.abs(x[i] - x_new[a * i + j]), '|x-x_n+1|', np.abs(x[i + 1] - x_new[a * i + j]))
                        y_new[a * i + j] = y[i]
                    else:
                        y_new[a * i + j] = y[i + 1]

    return y_new

def mse(x1, x2):
    return np.mean(np.sqrt((x1-x2)**2))


start = 0
stop = 4*np.pi
step = 0.5

x = np.arange(start, stop + step, step)
y = np.cos(x)

y_interp_linear = interp.interp1d(x, y, kind='linear')
y_interp_nearest = interp.interp1d(x, y, kind='nearest')

divider = 5
x_dense = np.arange(start, stop + step/divider, step/divider)
t3 = tm.time()
y_linear = y_interp_linear(x_dense)
t4 = tm.time()
y_nearest = y_interp_nearest(x_dense)
t5 = tm.time()
y_ideal = np.cos(x_dense)

t0 = tm.time()
y_my_knn = our_interpolation(x, y, step, x_dense, 'nearest')
t1 = tm.time()
y_my_linear = our_interpolation(x, y, step, x_dense, 'linear')
t2 = tm.time()

plt.figure(dpi=150, figsize=(10,15))
plt.plot(x, y, "rP", label='y=f(x) before', ms=12)
plt.plot(x_dense, y_ideal, "m-", label='ideal')
plt.plot(x_dense, y_my_linear, "bo", label='my linear', ms=5)
plt.plot(x_dense, y_my_knn, "go", label='my nn', ms=5)
plt.plot(x_dense, y_linear, "b*", label='linear num', mec='k', mew=0.5)
plt.plot(x_dense, y_nearest, "g*", label='nearest num', mec='k', mew=0.5)

plt.grid(True)
plt.xlim([start, stop])
plt.legend(loc='lower right')
plt.show()

print('___ my linear elapsed time _____', t1 -t0, '_ mse _', mse(y_ideal, y_my_linear))
print('___ my nn elapsed time ________', t2 -t1, '_ mse _', mse(y_ideal, y_my_knn))
print('___ num linear elapsed time ____', t4 -t3, '_ mse _', mse(y_ideal, y_linear))
print('___ num nn elapsed time _______', t5 -t4, '_ mse _', mse(y_ideal, y_nearest))
