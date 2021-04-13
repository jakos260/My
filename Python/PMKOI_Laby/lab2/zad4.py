import numpy as np
import time
import scipy.signal as sg

def grad(x1, step = 1):

    result = np.zeros((x1.shape[0] + 2, x1.shape[1] + 2, x1.shape[2] + 2))
    for x in range(1, x1.shape[0]+1):
        for y in range(1, x1.shape[1]+1):
            for z in range(1, x1.shape[2]+1):
                a = (x1[x+1][y-1][z-1] - x1[x-1][y-1][z-1])/2
                b = (x1[x+1][y-1][z+1] - x1[x-1][y-1][z+1])/2
                c = (x1[x+1][y+1][z-1] - x1[x-1][y+1][z-1])/2
                d = (x1[x+1][y+1][z+1] - x1[x-1][y+1][z+1])/2

                result[x+1][y+1][z+1] = (((d-b)/2)-((c-a)/2))/2
    return result

def nd_array(l, N):
    araj = np.zeros((l,) * N)
    for x in range(araj.shape[0]):
        for y in range(araj.shape[1]):
            for z in range(araj.shape[2]):
                araj[x][y][z] = np.random.randint(0, 10)
    return araj

x1 = nd_array(4, 3)
print('_x1_\n', x1)

conv = np.array([[[-1, 0, 1],
                 [0, 0, 0],
                 [1, 0, -1]],

                [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]],

                [[1, 0, -1],
                 [0, 0, 0],
                 [-1, 0, 1]]])

t0 = time.time()
conv_num = sg.convolve(x1, conv)
t1 = time.time()
conv_my = grad(x1)
t2 = time.time()

print('\n ___ scipy ___\n', conv_num, '\n___ elapsed time:', t1 - t0, ' seconds')
print('\n ___  my   ___\n', conv_my, '\n___ elapsed time:', t2 - t1, ' seconds')

