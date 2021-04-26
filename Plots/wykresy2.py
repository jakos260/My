import matplotlib.pyplot as plt
from openpyxl import load_workbook
import numpy as np

def sk(x):
    sum=0
    for i in range(len(x)):
        sum += x[i]**2
    return np.sqrt(sum)/len(x)

data = np.loadtxt('drgania.txt')
means = data.mean(axis = 0)

x = data.T[2]
y = data.T[3]
z = data.T[4]

print("sk X: ", sk(x))
print("sk Y: ", sk(y))
print("sk Z: ", sk(z))