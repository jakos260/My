import scipy.integrate as integrate
import time as tm
import numpy as np
import matplotlib.pyplot as plt

def my_gauss(z, x_step, y_step):
    pass

start = 0
stop = 10
step = 0.1
samples = int((stop - start)/step)
x = np.linspace(start, stop, samples)
y = np.linspace(start, stop, samples)
x, y = np.meshgrid(x, y)
f = lambda y, x: x * y**2 + 2 * x*y + 4


t1 = tm.time()
# my_integr = my_gauss(y, x, y)
t2 = tm.time()
num_in_q = integrate.dblquad(f, 0, 4, lambda x: 0, lambda x: 3)
t3 = tm.time()

# print('___ my  integral  simpson_38 ___', my_integr[len(my_integr)-1], '| elapsed time:', t2 - t1)
print('\n___ num integral Gaussian quadrature ___', num_in_q, '| elapsed time:', t3 - t2)