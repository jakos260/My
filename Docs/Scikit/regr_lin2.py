import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model


diabetes = datasets.load_diabetes()

f, axarr = plt.subplots(5,2, sharex=True, sharey=True,figsize=(10,7))
for i in range(0,5):
    for j in range(0,2):
        X = diabetes.data[:, np.newaxis, i*2+j]
        
        # Dzielimy dane na zestawy szkoleniowe i testowe
        X_train = X[:-20]
        X_test = X[-20:]
        
        # tak samo z celami
        y_train = diabetes.target[:-20]
        y_test = diabetes.target[-20:]
        
        # tworzymy model regresji...
        regr = linear_model.LinearRegression()
        
        # ... i trenujemy go odpowiednim zestawem
        regr.fit(X_train, y_train)
        
        
        print('Współczynniki: \n', regr.coef_)
        print("Średni błąd kwadratowy: %.2f"
              % np.mean((regr.predict(X_test) - y_test) ** 2))
        print('Wynik wariancji: %.2f' % regr.score(X_test, y_test)) # 1 - super, 0 - źle
        
        axarr[i,j].scatter(X_test, y_test,  color='red')
        axarr[i,j].plot(X_test, regr.predict(X_test), color='blue', linewidth=1)
        
plt.show()