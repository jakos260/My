import numpy as np

def kwadratsumy(x):
    result = 0
    for i in range(len(x)):
        result = result + x[i]
    return result**2

x = np.array([1, 2, 3, 4, 5, 6]) #liczby, których sumę chcemy podnieść do kwadratu
print('kwadrat sumy to', kwadratsumy(x))