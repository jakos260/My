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
poly_model =  PolynomialFeatures(degree = 2) #degree - stopień wielomianu
x_poly = poly_model.fit_transform(x_train)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y_train)

fig, ax = plt.subplots(nrows=1, ncols=2, sharey='row')

ax[0,0].scatter(x_test, y_test, 'r')
# ax[0,0].plot(x_test, lin_reg.predict(x_test), 'b')

# ax[0,1].scatter(x_test, y_test, 'r')
# ax[0,1].plot(x_test, lin_reg_2.predict(x_test))

fig.suptitle('regresja wielomianowa')
plt.show()
