'''
____________regresja wielomianowa_____________

y = b0 + b1x1 + b2x2^2 + ... bnxn^n
n danych można dopasować wielomianem n-tego stopnia

https://ichi.pro/pl/regresja-wielomianowa-w-pythonie-73720766034197
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
x, y = datasets.load_diabetes(return_X_y=True)
x = x[:, np.newaxis, 2]

# Podział danych na zestawy uczące / testowe
x_train = x[:-20]
x_test = x[-20:]

# Podział celi na zestawy treningowe / testowe
y_train = y[:-20]
y_test = y[-20:]

# regresja liniowa dla porównania
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

# nasz model wielomianowy
poly_model =  PolynomialFeatures(degree = 10) #degree - stopień wielomianu
x_poly = poly_model.fit_transform(x_train)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y_train)


fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('regresja wielomianowa')

ax1.scatter(x_test, y_test, color='r')
ax1.plot(x_test, lin_reg.predict(x_test), 'b')

ax2.scatter(x_test, y_test, color='r')
ax2.plot(x_test, lin_reg_2.predict(poly_model.fit_transform(x_test)), color='b')

plt.show()
