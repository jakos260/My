import numpy as np
import matplotlib.pyplot as plt


start = -5
stop = 5
step = 1
samples = np.int((stop-start)/step)

x = np.linspace(start, stop, samples)
f = x ** 3 + 4 * (x ** 2) - 5 * x + 3
f_p = 3*(x**2) + 8*x - 5


def conv(f):
    conv = np.array([-1, 0, 1])
    df = np.zeros(len(f))
    for i in range(len(f)-1):
        for j in range(len(conv)):
            a = 0
            if i+j < len(df):
                a = a + (conv[j] * f[i+j]) / (2 * step)
            df[i] = a
        print('i', i, df[i])
    return df

df = conv(f)
# print(df)

plt.figure(dpi=150)
plt.plot(x, f, 'r', label = 'f')
plt.plot(x, f_p, 'b', label = 'df_rel')
plt.plot(x, df, 'g', label = 'df_conv')
plt.legend()
plt.show()


