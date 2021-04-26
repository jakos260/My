#-*- coding: utf_8 -*-

import numpy as np
from scipy.linalg import lstsq

# Zasiêgi
distance = np.array([38098, 85692, 152220])

# prêdkoœci
speed = [400, 600, 800]

# kwadraty prêdkoœci
squared_speed = [n**2 for n in speed]

M = distance[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,squared_speed)
print "Wspó³czynnik odleg³oœci =", model[1]
print " Przesuniêcie =", model[0]

