import numpy as np

tab1 = np.arange(0,101,2)
tab2 = np.arange(100,-1,-2)

print(tab1)
print(tab2)

print('dodawanie',np.add(tab1,tab2))
print('mnożenie',np.multiply(tab1,tab2))
print('odejmowanie',np.subtract(tab1[0:10],tab2[-10:]))
print('co trzeci?',tab1[0:101:4])
print('podzielne przez 3',tab1[tab1%3==0])

