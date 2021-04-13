import numpy as np
import torch as tc
import time


t0 = time.time()
np_rand = np.random.rand((10000000)).astype(np.float32)
t1 = time.time()
tc_rand = tc.rand(10000000, dtype=tc.float32)
t2 = time.time()

print('numpy -', t1 - t0)
print('pytorch -', t2 - t1)