'''
convolve - splot

(a*v)[n] = sum(a[m]v[n-m]) gdzie m ∈ (-∞, ∞)

'''

import numpy as np

print(np.convolve([1,2,1,],[1,1,1]))

