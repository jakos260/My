#-*- coding: utf_8 -*-

import numpy as np
from scipy.linalg import lstsq

fahrenheit = np.array([5,14,23,32,41,50])
celsius = np.array([-15,-10,-5,0,5,10])

M = celsius[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,fahrenheit)
print "a =", model[1]
print "b =", model[0]