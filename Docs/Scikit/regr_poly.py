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
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
boston = datasets.load_boston()
df = pd.DataFrame(boston['data'], columns=boston['feature_names'])
df = pd.concat([df, pd.Series(boston['target'], name='MEDV')], axis=1)
X = df.iloc[:, [4,7]].values
y = df.iloc[:, 4].values
print(X.shape,'\n',y.shape)

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# print(x_test, '\n____', y_test)
# ____________regresja liniowa dla porównania___________
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_pred_lin = lin_reg.predict(X)

# __________nasz model wielomianowy____________

 # degree - stopień wielomianu
degree = 5
# poly_reg =  PolynomialFeatures(degree) # degree można też zdefiniować tu (5)
# x_transform = poly_reg.fit_transform(x)

# lin_reg_2 = LinearRegression()
# lin_reg_2.fit(x_transform, y) 



fig, (ax1, ax2) = plt.subplots(2)
ax1.scatter(X, y, color='k', marker='.')
ax1.plot(X, y_pred_lin, 'y')
ax1.set_title('regresja liniowa')

# ax2.scatter(x.iloc[:,0], y, color='k')
# ax2.plot(x, lin_reg_2.predict(x), color='g')
# ax2.plot(x, lin_reg_2.predict( poly_reg.fit_transform(x)), color='g')
ax2.set_title('regresja wielomianowa stopnia ' + str(degree))
plt.show()

# print("Wielomian\nŚredni błąd kwadratowy: ", np.mean((poly_regr.predict(x) - y) ** 2))
# print('współczynniki: ', lin_reg_2.intercept_, lin_reg_2.coef_)
# print("F liniowa\nŚredni błąd kwadratowy: ", np.mean((lin_reg.predict(x) - y) ** 2))

