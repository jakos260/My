"""
regresja liniowa - przykłady
http://scikit-learn.org/stable/modules/linear_model.html
https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Używaj tylko jednej funkcji
diabetes_X = diabetes_X[:, np.newaxis, 2]

# Podział danych na zestawy uczące / testowe
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Podział celi na zestawy treningowe / testowe
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# tworzenie modelu
model = linear_model.LinearRegression()

# trenowanie modelu
model.fit(diabetes_X_train, diabetes_y_train)

# utworzenie y przewidywanych
diabetes_y_pred = model.predict(diabetes_X_test)


print('współczynniki: \n', model.coef_)
print('Mean squared error: %.2f' % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print('współczynnik determinacji: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred)) # 1 oznacza idealne dopasowanie

plt.figure(figsize=(12,6))
plt.scatter(diabetes_X_test, diabetes_y_test,  color='k')
plt.plot(diabetes_X_test, diabetes_y_pred, color='b', linewidth=2)
plt.show()