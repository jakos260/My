import numpy as np

def gen(start, stop):
    return np.random.randint(start, stop)

for i in range(5):
    print(i+1,'liczba losowa =', gen(0, 10))