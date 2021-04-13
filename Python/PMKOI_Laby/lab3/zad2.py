import scipy.integrate as integrate
import time as tm
import numpy as np
import matplotlib.pyplot as plt

def our_integrate_recurencyjnie(f, start, stop, h, mode):
    #method = {trapezoidal}

    if mode == 'trapezoidal':
        integr = np.zeros(int((stop-start)/h))
        integr[1] = (f(start) + f(stop))*(h/2)
        print('integr[ 1 ] =', integr[1])
        for k in range(2, int(stop/h)):
            f_sum = 0
            for i in range(1, 2**(k-2)):
                f_sum = f_sum + f(start + (h * (2*i - 1) / (2**(k-1))))
            print('integr[', k, '] =', integr[k-1], 'plus', (h/2**(k-1)) * f_sum)
            integr[int(k)] = integr[k-1] * 0.5 + (h/2**(k-1)) * f_sum


def our_integrate_rec(y, h, mode):
    #method = {trapezoidal, simpson_13, simpson_38}
    integr = np.zeros(len(y))

    if mode == 'trapezoidal':
        integr[0] = y[0]
        for i in range(1, len(y)-1):
            integr[i] = integr[i-1] + 2*y[i]
        integr[len(integr)-1] = y[len(y)-1]
        integr = integr * (h / 2)

    elif mode == 'simpson_13':
        integr[0] = y[0]
        for i in range(1, len(y) - 1):
            if i % 2 == 1:              #nieparzyste = 4*f(x)
                integr[i] = integr[i - 1] + 4*y[i]
            else:                       #nieparzyste = 2*f(x)
                integr[i] = integr[i - 1] + 2 * y[i]
        integr = integr * (h / 3)

    elif mode == 'simpson_38':
        integr[0] = y[0]
        for i in range(1, len(y) - 1):
            if i%3==0:
                integr[i]= integr[i-1] + y[i]
            else:
                integr[i] = integr[i - 1] + 3*y[i]

        integr = integr * (3 * h/8)

    return integr


start = 0
stop = 10
step = 0.1
samples = int((stop - start)/step)
x = np.linspace(start, stop, samples)
f = lambda x: 4*(x**2) - 40*x + 84
y = f(x)

t0 = tm.time()
my_in_t = our_integrate_rec(y, step, 'trapezoidal')
t1 = tm.time()
my_in_s13 = our_integrate_rec(y, step, 'simpson_13')
t2 = tm.time()
my_in_s38 = our_integrate_rec(y, step, 'simpson_38')
t3 = tm.time()
num_in_q = integrate.quadrature(f, start, stop-step)
t4 = tm.time()


plt.figure(figsize=(12,9))
plt.plot(x, y, "r-", label = 'y = f(x)')
plt.plot(x, np.cumsum(y)*step, "k-", label = 'y integral')
plt.plot(x, my_in_t, "b*", label = 'y integral trapez')
plt.plot(x, my_in_s13, "g*", label = 'y integral sim13')
plt.plot(x, my_in_s38, "y*", label = 'y integral sim38')
plt.grid(True)
plt.xlim([start, stop])
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()


print('___ my  integral trapezoidal ___', my_in_t[len(my_in_t)-2], '| elapsed time:', t1 - t0)
print('___ my  integral  simpson_13 ___', my_in_s13[len(my_in_s13)-2], '| elapsed time:', t2 - t1)
print('___ my  integral  simpson_38 ___', my_in_s38[len(my_in_s38)-2], '| elapsed time:', t3 - t2)
print('\n___ num integral Gaussian quadrature ___', num_in_q, '| elapsed time:', t4 - t3)
