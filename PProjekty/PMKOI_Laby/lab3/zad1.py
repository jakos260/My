import scipy.integrate as integrate
import time as tm
import numpy as np


def our_integrate(y, dx, method):
    #method = {trapezoidal, simpson_13, simpson_38

    if method == 'trapezoidal':
        integral = np.sum(2*y) - (y[0]+y[len(y)-1])
        integral = integral * (dx/2)

    if method == 'simpson_13':
        integral = np.sum(2*y) - (y[0]+y[len(y)-1])
        for i in range(1, len(y)-2, 2):
            integral = integral + 2*y[i]
        integral = integral * (dx / 3)

    if method == 'simpson_38':
        integral = np.sum(y*3) - 2*(y[0] + y[len(y)-1])
        for i in range(2, len(y)-2, 3):
            integral = integral - y[i]
        integral = integral * (3*dx / 8)

    return integral


start = 0
stop = 10
step = 0.0001
samples = np.int((stop - start)/step)

x = np.linspace(start, stop, samples)
y = 20*(x**2) + 3.5*x + 8


t0 = tm.time()
my_in_t = our_integrate(y, step, 'trapezoidal')
t1 = tm.time()
my_in_s13 = our_integrate(y, step, 'simpson_13')
t2 = tm.time()
my_in_s38 = our_integrate(y, step, 'simpson_38')
t3 = tm.time()
num_in_t = integrate.trapz(y, x)
t4 = tm.time()
num_in_s = integrate.simps(y, x)
t5 = tm.time()


print('___ my  integral trapezoidal ___', my_in_t, '| elapsed time:', t1 - t0)
print('___ my  integral  simpson_13 ___', my_in_s13, '| elapsed time:', t2 - t1)
print('___ my  integral  simpson_38 ___', my_in_s38, '| elapsed time:', t3 - t2)
print('\n___ num  integral  trapezoidal ___', num_in_t, '| elapsed time:', t4 - t3)
print('___ num integral simpson 13/38 ___', num_in_s, '| elapsed time:', t5 - t4)

# trapezy najszybciej