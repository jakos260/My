import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

# filename = 'kalibracja_lab_2a.txt'
# krzywa_kalibracji = np.loadtxt(filename, delimiter='	', skiprows=1, dtype=str)
# filename2 = 'podejscie3_ostrze6c_1_52__00001_2a_2.txt'
# krzywa = np.loadtxt(filename2, delimiter='	', skiprows=1, dtype=str)

krzywa = pd.read_csv('krzywa.txt', sep = r'\s+', header = 0,
names = ['Time (s)', 'Z (um)', 'Deflection (V)', 'nan1', 'nan2', 'nan3'],
usecols = ['Time (s)', 'Z (um)', 'Deflection (V)'])

krzywa_kalibracji = pd.read_csv('kalibracja.txt', sep = r'\s+', header = 0,
names = ['Time (s)', 'Z (um)', 'Deflection (V)', 'nan1', 'nan2', 'nan3'],
usecols = ['Time (s)', 'Z (um)', 'Deflection (V)'])


# print(krzywa_kalibracji)

# krzywa_kalibracji = pd.read_csv('Krzywa_kalibracji.csv', sep =';')
deflection = np.array(krzywa_kalibracji['Deflection (V)'])
Z = np.array(krzywa_kalibracji['Z (um)'])

start_k = 680 #Początek naszego wektora wartości kalibracji
stop_k = 1000 #Koniec wektora kalibracji

zreg = np.array(Z[start_k:stop_k]) - Z[stop_k]
defreg = np.flip(deflection[start_k:stop_k] - deflection[start_k])

#Linear regression
defreg = defreg.reshape((-1, 1))

model = LinearRegression()
model.fit(defreg, zreg)
model = LinearRegression().fit(defreg, zreg)
r_sq = model.score(defreg, zreg)

print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print(f'1/slope: {1/model.coef_}')

df_pred = model.predict(defreg)
df_pred = np.array(df_pred)

k = 0.02
f = model.coef_ * k * deflection #wynik w uN

plt.figure(1, figsize=(10,7))
plt.scatter(Z[start_k:stop_k] - Z[stop_k], np.flip(deflection[start_k:stop_k] - deflection[start_k]), s = 0.7, color ='k', label ='krzywa kalibracyjna')
plt.scatter(Z[start_k:stop_k] - Z[stop_k], (zreg / (model.coef_)), s = 0.7, color ='r', label ='krzywa kalibracyjna - regresja')
plt.legend()
plt.title('AFM')
plt.xlabel('Z(um)')
plt.ylabel('U(V)')
plt.grid(True)
# plt.show()

# krzywa = pd.read_csv('Krzywa.csv', sep=';')
deflection_krzywa = np.array(krzywa['Deflection (V)'])
Z_krzywa = np.array(krzywa['Z (um)'])

# 660 - 780 (potęga = 1.504)
# 643 - 780 (potęga = 2.011)
start = 643 #Przesunięcia krzywej swobodnie
stop = 780 #odcięcie do kawałka nas interesującego

plt.figure(2, figsize=(10,7))
plt.scatter(Z[start_k:stop_k] - Z[stop_k], np.flip(deflection[start_k:stop_k] - deflection[start_k]), s = 1.5, color ='k', label ='krzywa kalibracyjna')
plt.scatter(Z[start_k:stop_k] - Z[stop_k], (zreg / (model.coef_)), s = 1.5, color ='r', label ='krzywa kalibracyjna - regresja')
# plt.scatter(Z_krzywa[start:stop] - Z_krzywa[stop], np.flip(deflection_krzywa[start:stop]) - deflection_krzywa[start], s = 1.5, color ='b', label ='krzywa')
plt.legend()
plt.title('AFM')
plt.xlabel('Z(um)')
plt.ylabel('U(V)')
plt.grid(True)

z_krzywej = Z_krzywa[start:stop] - Z_krzywa[stop]
Z_kalibracja_nowa = np.flip(deflection_krzywa[start:stop] - deflection_krzywa[start]) * model.coef_


plt.scatter(Z_kalibracja_nowa, np.flip(deflection_krzywa[start:stop] - deflection_krzywa[start]), s = 0.7, color ='g', label ='krzywa znormalizowana \ndo krzywej pomiarowej')
plt.scatter(Z_krzywa[start:stop] - Z_krzywa[stop], np.flip(deflection_krzywa[start:stop]) - deflection_krzywa[start], s = 0.7, color ='b', label ='krzywa pomiarowa (odcięta)')
plt.legend()
plt.title('AFM')
plt.xlabel('Z(um)')
plt.ylabel('U(V)')
plt.grid(True)

delta_z = abs(z_krzywej - Z_kalibracja_nowa)

plt.figure(3, figsize=(10,7))
plt.scatter(delta_z, np.flip(deflection_krzywa[start:len(delta_z) + start] - deflection_krzywa[start]), s = 0.7, color ='g', label ='krzywa znormalizowana \ndo krzywej pomiarowej')
plt.legend()
plt.title('AFM')
plt.xlabel('Z(um)')
plt.ylabel('U(V)')
plt.grid(True)

przesuniecie = len(delta_z)-1
force = np.flip(f[start:len(delta_z) + start]) - f[start]
plt.figure(4, figsize=(10,7))
plt.scatter(np.flip(delta_z), np.flip(force), s = 0.7, color = 'g', label = 'krzywa znormalizowana')
plt.legend()
plt.title('AFM')
plt.xlabel('Z(um)')
plt.ylabel('F(uN)')
plt.grid(True)

def fit(x, a, b):
    return a*x**b

A, _ = curve_fit(fit, np.flip(delta_z), np.flip(force))
print("Współczynnik kierunkowy", A[0])
print("Potega", A[1])


v = 0.5
alfa = 5*np.pi/36
R = 50*10**-3 # w mikrometrach

plt.figure(5, figsize=(10,7))
plt.scatter(Z_kalibracja_nowa, model.coef_ * k * np.flip(deflection_krzywa[start:stop] - deflection_krzywa[start]), s = 0.7, color ='g', label ='krzywa kalibracyjna')
plt.scatter(np.flip(delta_z), np.flip(force), s = 0.7, color = 'r', label = 'krzywa znormalizowana')
plt.scatter(np.flip(delta_z), (np.flip(delta_z)**A[1])*A[0], s = 0.7, color = 'brown', label = 'krzywa dofitowana')
plt.legend()
plt.title('AFM')
plt.xlabel('Z(um)')
plt.ylabel('F(uN)')
plt.grid(True)
plt.show()

E1 = (A[0]*3*(1-v**2))/(4*np.sqrt(R))
E2 = A[0]*np.pi*(1-v**2)/(2*np.tan(alfa))
print('Moduł Younga dla sferycznego', E1, '[MPa]')
print('Moduł Younga dla piramidalnego:', E2, '[MPa]')
print(f'E śr = {(E1+E2)/2}')