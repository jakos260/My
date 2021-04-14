import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.misc import derivative

def deriv(x, step, mode):

    df = np.zeros(len(x), dtype=np.float32)
    if mode == 'central':
        for i in range(1, len(x)-1):
            df[i] = (x[i+1] - x[i-1])/(2*step)
        return df

    elif mode =='forward':
        for i in range(len(x)-1):
            df[i] = (x[i+1] - x[i])/(step)
        return df

    elif mode == 'backward':
        for i in range(1, len(x)):
            df[i] = (x[i] - x[i-1])/(step)
        return df


def mse(y):
    return np.mean(np.sqrt((np.cos(x) - y)**2))


start = -5
stop = 5
samples = 50
step = (stop - start)/samples

x = np.linspace(start, stop, samples)
f = np.sin(x)
df_num = np.gradient(f, step)

t_0 = time.time()
df_c = deriv(f, step, 'central')
t_1 = time.time()
df_f = deriv(f, step, 'forward')
t_2 = time.time()
df_b = deriv(f, step, 'backward')
t_3 = time.time()

print('___elapsed time___\ndf_central -', t_1-t_0, '\ndf_forward -', t_2-t_1, '\ndf_backward -', t_3-t_2)


plt.figure(dpi=150)
plt.plot(x, f, 'red')
plt.plot(x, df_num, 'black')
plt.scatter(x, df_c, color='green', marker='o', label = 'central')
plt.scatter(x, df_f, color='yellow', marker='^', label = 'forward')
plt.scatter(x, df_b, color='blue', marker='*', label = 'backward')
plt.legend()
plt.grid(True)
plt.show()





