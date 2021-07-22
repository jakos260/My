#-*- coding: utf_8 -*-

# Przewidywanie przyszlego zysku
import numpy as np
from scipy.linalg import lstsq

year = np.array([2011,2012,2013,2014,2015,2016,2017])
profit = np.array([40000,43000,45000,50000,54000,57000,59000])

M = year[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,profit)

print "a =", model[1]
print "b = ", model[0]