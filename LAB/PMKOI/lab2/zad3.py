import numpy as np
import matplotlib.pyplot as plt
import time

def deriv(x, f, step, order, mode):
    #order = 1,2,3,4
    #mode = conv / seq

    if mode == 'seq':
        df = np.zeros(len(x))
        if order == 1:
            for i in range(len(x)):
                df[i] = (f(x[i] + step) - f(x[i] - step)) / (2*step)
            return df
        if order == 2:
            for i in range(len(x)):
                df[i] = (f(x[i] + step) + f(x[i] - step) - 2*f(x[i])) / (step**2)
            return df
        if order == 3:
            for i in range(len(x)):
                df[i] = (2*f(x[i] - step) - 2*f(x[i] + step) - f(x[i] - 2*step) + f(x[i] + 2*step)) / (2*(step**3))
            return df
        if order == 4:
            for i in range(len(x)):
                df[i] = (f(x[i] + 2*step) + f(x[i] - 2*step) + 6*f(x[i]) - 4*f(x[i] - step) - 4*f(x[i] + step)) / (step ** 4)
            return df

    if mode == 'conv':

        if order == 1:
            conv = np.array([-1, 0, 1])
            df = np.zeros(len(x))
            for i in range(1, len(x) - 1):
                df[i] = np.sum(conv*x[i-1:i+2])/(2*step)
                # print(df[i])
            return df

        if order == 2:
            conv = np.array([1, -2, 1])
            df = np.zeros(len(x))
            for i in range(1, len(x) - 1):
                df[i] = np.sum(conv*x[i-1:i+2])/(step**2)
            return df

        if order == 3:
            conv = np.array([-1, 2, 0, -2, 1])
            df = np.zeros(len(x))
            for i in range(2, len(x) - 2):
                df[i] = np.sum(conv * x[i-2:i+3])/(2*(step**3))
            return df

        if order == 4:
            conv = np.array([1, -4, 6, -4, 1])
            df = np.zeros(len(x))
            for i in range(2, len(x) - 2):
                df[i] = np.sum(conv * x[i-2:i+3])/(step**4)
            return df


def mse_num(y_rel, y, start, stop):
    print('MSE num ___', np.mean(np.sqrt((y_rel - y)**2)), ' ___time___ ', (stop-start))
    pass
def mse_seq(y_rel, y, start, stop):
    print('MSE seq ___', np.mean(np.sqrt((y_rel - y)**2)), ' ___time___ ', (stop-start))
    pass
def mse_conv(y_rel, y, start, stop):
    print('MSE conv ___', np.mean(np.sqrt((y_rel - y)**2)), ' ___time___ ', (stop-start))
    pass

start = -5
stop = 5
step = 0.5
samples = int((stop - start)/step)

x = np.linspace(start, stop, samples)
f = 2*(x**4) - x**3 + 4*(x**2) - 5*x + 3
func = lambda x: 2*(x**4) - x**3 + 4*(x**2) - 5*x + 3

#rzeczywiste pochodne
df_real = 8*(x**3) - 4*(x**2) + 8*x - 5
df2_real = 24*(x**2) - 8*x + 8
df3_real = 48 * x - 8
df4_real = 48 + x*0

#pochodne liczone za pomocą np.gradient()
start_num = time.time()
df_num = np.gradient(f, step)
num_1 = time.time()
df2_num = np.gradient(df_num, step)
num_2 = time.time()
df3_num = np.gradient(df2_num, step)
num_3 = time.time()
df4_num = np.gradient(df3_num, step)
num_4 = time.time()

#pochodne sekwencyjne
start_seq = time.time()
df_seq = deriv(x, func, step, 1, 'seq')
seq_1 =time.time()
df2_seq = deriv(x, func, step, 2, 'seq')
seq_2 =time.time()
df3_seq = deriv(x, func, step, 3, 'seq')
seq_3 =time.time()
df4_seq = deriv(x, func, step, 4, 'seq')
seq_4 =time.time()

#pochodne konwolucyjne
start_conv = time.time()
df_conv = deriv(x, func, step, 1, 'conv')
conv_1 =time.time()
df2_conv = deriv(x, func, step, 2, 'conv')
conv_2 =time.time()
df3_conv = deriv(x, func, step, 3, 'conv')
conv_3 =time.time()
df4_conv = deriv(x, func, step, 4, 'conv')
conv_4 =time.time()



fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12,8))

ax[0,0].plot(x, f, color='r', label = 'f(x)')
ax[0,0].plot(x, df_real, color='blue', label = 'dy_real')
ax[0,0].plot(x, df_num, color='green', label = 'dy_num')
ax[0,0].scatter(x, df_seq, color='black', marker='o', label = 'dy_seq')
ax[0,0].scatter(x, df_conv, color='yellow', marker='*', label = 'dy_conv')
ax[0,0].grid()
ax[0,0].title.set_text('1 stopień')
ax[0,0].legend()

ax[0,1].plot(x, f, color='r', label = 'f(x)')
ax[0,1].plot(x, df2_real, color='blue', label = 'dy2_real')
ax[0,1].plot(x, df2_num, color='green', label = 'dy2_num')
ax[0,1].scatter(x, df2_seq, color='black', marker='o', label = 'dy2_seq')
ax[0,1].scatter(x, df2_conv, color='yellow', marker='*', label = 'dy2_conv')
ax[0,1].grid()
ax[0,1].title.set_text('2 stopień')
ax[0,1].legend()

ax[1,0].plot(x, f, color='r', label = 'f(x)')
ax[1,0].plot(x, df3_real, color='blue', label = 'dy3_real')
ax[1,0].plot(x, df3_num, color='green', label = 'dy3_num')
ax[1,0].scatter(x, df3_seq, color='black', marker='o', label = 'dy3_seq')
ax[1,0].scatter(x, df3_conv, color='yellow', marker='*', label = 'dy3_conv')
ax[1,0].grid()
ax[1,0].title.set_text('3 stopień')
ax[1,0].legend()

ax[1,1].plot(x, f, color='r', label = 'f(x)')
ax[1,1].plot(x, df4_real, color='blue', label = 'dy4_real')
ax[1,1].plot(x, df4_num, color='green', label = 'dy4_num')
ax[1,1].scatter(x, df4_seq, color='black', marker='o', label = 'dy4_seq')
ax[1,1].scatter(x, df4_conv, color='yellow', marker='*', label = 'dy4_conv')
ax[1,1].grid()
ax[1,1].title.set_text('4 stopień')
ax[1,1].legend()

fig.suptitle('f(x) = 2x^4 - x^3 + 4x^2 - 5x + 3', fontsize=18)
fig.tight_layout()
plt.show()

print('\n___1.stopień___')
mse_num(df_real, df_num, start_num, num_1)
mse_seq(df_real, df_seq, start_seq, seq_1)
mse_conv(df_real, df_conv, start_conv, conv_1)


print('\n___2.stopień___')
mse_num(df2_real, df2_num, start_num, num_2)
mse_seq(df2_real, df2_seq, start_seq, seq_2)
mse_conv(df2_real, df2_conv, start_conv, conv_2)

print('\n___3.stopień___')
mse_num(df3_real, df3_num, start_num, num_3)
mse_seq(df3_real, df3_seq, start_seq, seq_3)
mse_conv(df3_real, df3_conv, start_conv, conv_3)

print('\n___4.stopień___')
mse_num(df4_real, df4_num, start_num, num_4)
mse_seq(df4_real, df4_seq, start_seq, seq_4)
mse_conv(df4_real, df4_conv, start_conv, conv_4)