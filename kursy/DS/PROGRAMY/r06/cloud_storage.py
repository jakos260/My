#-*- coding: utf_8 -*-

import numpy as np
from scipy.linalg import lstsq

month = np.array([1,2,3,4,5])
bill = np.array([120.0,131.2,142.1,152.9,164.3])

M = month[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,bill)
print "Wspolczynnik miesieczny =", model[1]
print "Koszt bazowy =", model[0]
