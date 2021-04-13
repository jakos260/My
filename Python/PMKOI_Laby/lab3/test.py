import numpy as np
from scipy import integrate

start = 0
stop = 10
step = 0.1
samples = int((stop - start)/step)
x = np.linspace(start, stop, samples)
f = lambda y, x: x * y ** 2 + 2 * x * y + 4

# using scipy.integrate.dblquad() method
geek = integrate.dblquad(f, 1, 4, lambda x: 0, lambda x: 1)

print(geek)