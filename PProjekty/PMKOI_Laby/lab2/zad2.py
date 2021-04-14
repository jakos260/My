import numpy as np
import time
import scipy.signal as sg


def our_convolution(x1, x2):
    bt = time.time()

    result = np.zeros((len(x1) + len(x2) - 1), dtype=np.float32)
    x2_r = np.zeros(len(x1) - 1)
    x2_r = np.append(x2_r, x2)
    x2_r = np.append(x2_r, np.zeros(len(x1) - 1))

    x1_rev = np.zeros(len(x1), dtype=np.float32)
    for i in range(len(x1)):
        x1_rev[i] = x1[(len(x1) - i - 1)]
        # print(x1_rev)

    for i in range(len(x2)+len(x1)-1):
        result[i] = np.sum(x1_rev * x2_r[i:i+len(x1_rev)])
        # print(i, result[i])

    et = time.time()
    print('my conv ___', result, ' ___ elapsed time:', et - bt, ' seconds')
    pass



x1 = np.array([1, 2, 3, 4], dtype=np.float32)
x2 = np.array([5, 6, 7, 8, 9], dtype=np.float32)
our_convolution(x1, x2)

bt = time.time()
result = sg.convolve(x1, x2)
et = time.time()
print(' scipy  ___', result, ' ___ elapsed time:', et - bt, ' seconds')