#-*- coding: utf_8 -*-

import numpy as np
from scipy.linalg import lstsq

# Zasi�gi
distance = np.array([38098, 85692, 152220])

# pr�dko�ci
speed = [400, 600, 800]

# kwadraty pr�dko�ci
squared_speed = [n**2 for n in speed]

M = distance[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,squared_speed)
print "Wsp�czynnik odleg�o�ci =", model[1]
print " Przesuni�cie =", model[0]

