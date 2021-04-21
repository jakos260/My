import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import numpy as np


tab = np.loadtxt("CUSO4_2A.DAT.txt")

print(tab[0])

x = np.reshape(tab[:, 2], (-1, 1))
y = np.reshape(tab[:, 0], (-1, 1))

print(x[0], y[0])

model = linear_model.LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

y_cl = []
x_cl = []
for i in range(len(y)):
    if abs(y[i] - y_pred[i]) < 1:
        y_cl = np.append(y_cl, y[i])
        x_cl = np.append(x_cl, x[i])


plt.figure(figsize=(12,6))
plt.scatter(x, y,  color='k', marker='o' )
plt.scatter(x_cl, y_cl,  color='r', marker='.')
# plt.plot(x, y_pred, color='b', linewidth=2)
plt.show()
