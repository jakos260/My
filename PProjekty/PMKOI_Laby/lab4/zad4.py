import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.integrate import trapz, simps, quadrature
import time as tm

def cubic_interpolation(x, f):
    inter = interp1d(x, f, kind='cubic')
    return inter

def my_cubic_interpolation(x, f, x_new):

    flist = []

    for i in range(len(x_new)):
        point_l, value_l = four_closest_points(x, f, x_new[i])
        array = make_equations(point_l)
        a = solve_equation(array, value_l) # a - współczynnik wielomianu
        y = final(a, x_new[i])
        flist = np.append(flist, y)
    return flist
def four_closest_points(x, f, x_new):
    point_list = []
    value_list = []

    for i in range(len(x)-2):
        if x_new - x[i] < x[i] - x[i+2]:
            point_list.append(x[i])
            value_list.append(f[i])
        if len(point_list) == 4:
            break
    return point_list, value_list
def make_equations(point_list):
    pl_3 = [i**3 for i in point_list]
    pl_2 = [i**2 for i in point_list]
    pl = np.ones(len(point_list))
    array = np.stack((pl, pl_2, pl_3), axis=1)
    return array
def solve_equation(array, value_list):
    rate = np.linalg.inv(array) @ value_list
    return rate
def final(rate, x):
    y = lambda x: rate[0] + rate[1]*x + rate[2]*x**2 + rate[3]*x**3
    return y(x)

def our_cubic_interpolation(x, f):
    dy1 = f.diff(x[0])
    dy2 = f.diff(x[-1])
    a = 2*f(0) - 2*f(x[-1]) + dy1 + dy1
    b = -3*f(0) - 2*f(x[-1]) - 2*dy1 - dy2
    c = dy1
    d = dy2
    y = lambda t: a*t**3 + b*t**2 + c*t + d
    return y(x)

start = 0
stop = 10
step = 0.5
divider = 3

x = np.arange(start, stop+step, step)
f = x**2 - 4*x + 7
x_dense = np.arange(start, stop + step/divider, step/divider)
f_inter_cubic = cubic_interpolation(x, f)
f_inter = f_inter_cubic(x_dense)


real_integr = (1/3)*x_dense**3 - 2*x_dense**2 + 7*x_dense
t0 = tm.time()
trapez_integr = trapz(f_inter, x_dense)
t1 = tm.time()
simps_integr = simps(f_inter, x_dense)
t2 = tm.time()
quad_integr = quadrature(f_inter_cubic, 0, 10)
t3 = tm.time()


print('___ real integral _______', real_integr[-1])
print('___ trapez integral _____', trapez_integr, '_ elapsed time _', t1 - t0)
print('___ simpson integral ____', simps_integr, '_ elapsed time _', t2 - t1)
print('___ quadrature integral _', quad_integr, '_ elapsed time _', t3 - t2)

