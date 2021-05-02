import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

'''
______________Regresja liniowa_______________

interpolacja y = ax + b
'''

X, y = datasets.load_diabetes(return_X_y=True) 
# return_X_y >>> True - return data, target; False - return bunch(data, target)
X = X[:, np.newaxis, 2]

# Podział danych na zestawy uczące / testowe
X_train = X[:-20]
X_test = X[-20:]

# Podział celi na zestawy treningowe / testowe
y_train = y[:-20]
y_test = y[-20:]

# tworzenie modelu
model = linear_model.LinearRegression()

# trenowanie modelu
model.fit(X_train, y_train)

# utworzenie y przewidywanych
y_pred = model.predict(X_test)

while True:
    print('współczynniki: \n', model.coef_)
    print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))
    print('współczynnik determinacji: %.2f' % r2_score(y_test, y_pred)) # 1 oznacza idealne dopasowanie

    plt.figure(figsize=(12,6))
    plt.scatter(X_test, y_test,  color='k')
    plt.plot(X_test, y_pred, color='b', linewidth=2)
    plt.show()
    break

'''
____________regresja wielomianowa_____________

y = b0 + b1x1 + b2x2^2 + ... bnxn^n
n danych można dopasować wielomianem n-tego stopnia
'''
