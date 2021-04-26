#-*- coding: utf_8 -*-

import numpy as np
from scipy.linalg import lstsq

height = np.array([180,174,184,168,178])
weight = np.array([75,71,83,63,70])

M = height[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,weight)
print "a =", model[1]
print "b =", model[0]