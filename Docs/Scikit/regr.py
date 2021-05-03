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

while False:
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

https://ichi.pro/pl/regresja-wielomianowa-w-pythonie-73720766034197
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse, r2_score


boston = datasets.load_boston()
df = pd.DataFrame(boston['data'], columns=boston['feature_names'])
df = pd.concat([df, pd.Series(boston['target'], name='MEDV')], axis=1)
X = np.array(df['DIS'])
y = np.array(df['NOX'])
# print(X.shape,'\n',y.shape)

# from sklearn.model_selection import train_test_split # fajna funkcja, polecam obczaić
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)


# ____________regresja liniowa dla porównania___________
lin_reg = LinearRegression()
lin_reg.fit(X.reshape(-1,1), y)
y_pred_lin = lin_reg.predict(X.reshape(-1,1))

# ________________nasz model wielomianowy________________
'''
Tworzymy obiekt PolynomialF poly_reg> i wymieniamy wymagany stopień wielomianu.
Stworzymy kolejny obiekt regresji liniowej <pol_reg>, za pomocą którego dopasujemy nasze X_poly i Y.
X_grid zawiera posortowane wartości X, (tylko w przypadku plotowanie, na scatterze nie widać kolejności)
'''

degree = 4
poly_reg =  PolynomialFeatures(degree)  # PF(degree=4)
X_poly = poly_reg.fit_transform(X.reshape(-1,1))
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)
X_grid = np.arange(min(X), max(X), 0.1) 
X_grid = X_grid.reshape(-1, 1)
y_pred_pol = pol_reg.predict(poly_reg.fit_transform(X_grid))


# ______________wykresujemy___________________
while True:
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.scatter(X, y, color='k', marker='.')
    ax1.plot(X, y_pred_lin, 'y')
    ax1.set_title('regresja liniowa')

    ax2.scatter(X, y, color='k', marker='.')
    ax2.plot(X_grid, y_pred_pol, color='r')
    ax2.set_title('regresja wielomianowa stopnia' + str(degree))
    plt.show()

    '''
    coef_ oszacowane współczynniki, wielkość zaleźna od liczy celów (y)
    interprecet_ współczynnik niezależny
    r2_score współczynnik determinacji (1-super, 0-źle) R^2 = (wariancja_pred)/(wariancja_true)
    '''

    print("|______stopień______|", degree)
    print('|________MSE________|', mse(pol_reg.predict(poly_reg.fit_transform(X.reshape(-1,1))), y))
    print('|________R^2________|', r2_score(y, pol_reg.predict(poly_reg.fit_transform(X.reshape(-1,1)))))
    print('|___współczynniki___|', pol_reg.coef_)
    print('|__wsp. niezależny__|', pol_reg.intercept_)
    print('___________________________________________')
    print('|______stopień______|', 1)
    print('|________MSE________|', mse(lin_reg.predict(X.reshape(-1,1)), y))
    print('|________R^2________|', r2_score(y, lin_reg.predict(X.reshape(-1,1))))
    print('|___współczynniki___|', lin_reg.coef_)
    print('|__wsp. niezależny__|', lin_reg.intercept_)
    break
