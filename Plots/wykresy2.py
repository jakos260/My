import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import numpy as np
import pandas as pd

df = pd.read_excel(r'FL.xlsx', sheet_name='Arkusz2')
print(df)
x = np.array(df['Q KI'])
y = np.array(df['I0I'])
print(x, x.shape)
print(y, y.shape)
x_ = np.linspace(0, 0.16, 17)

# ____________regresja________________
regr = linear_model.LinearRegression()
regr.fit(x.reshape(-1,1), y)
y_pred = regr.predict(x_.reshape(-1,1))

plt.figure(figsize=(12,6))
plt.scatter(x, y, color = 'k', label='I0/I')
plt.plot(x_, y_pred, 'b', label='dopasowanie liniowe I0/I')
plt.xlabel('[Q] KI', fontsize = 12)
plt.ylabel('I0/I')
plt.legend()
plt.grid()
plt.show()

print('współczynniki: \n', regr.coef_)