import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import numpy as np
import pandas as pd
from colorama import init
from colorama import Fore, Back, Style
init()

'''
FLUO
'''
# df = pd.read_excel(r'FL.xlsx', sheet_name='Arkusz2')
# print(df)
# x = np.array(df['Q KI'])
# y = np.array(df['I0I'])
# print(x, x.shape)
# print(y, y.shape)
# x_ = np.linspace(0, 0.16, 17)

# # ____________regresja________________
# regr = linear_model.LinearRegression()
# regr.fit(x.reshape(-1,1), y)
# y_pred = regr.predict(x_.reshape(-1,1))

# plt.figure(figsize=(12,6))
# plt.scatter(x, y, color = 'k', label='I0/I')
# plt.plot(x_, y_pred, 'b', label='dopasowanie liniowe I0/I')
# plt.xlabel('[Q] KI', fontsize = 12)
# plt.ylabel('I0/I')
# plt.legend()
# plt.grid()
# plt.show()

# print('współczynniki: \n', regr.coef_)

'''
AFM
'''
filename = 'kalibracja_lab_2a.txt'
data = np.loadtxt(filename, delimiter='	', skiprows=1, dtype=str)

# print(data[0:4])
T = np.array(data[:,0]).astype(np.float)
Z = np.array(data[:,1]).astype(np.float)
V = np.array(data[:,2]).astype(np.float)
print(Fore.RED + f'{T[0], V[0]}')
print(Fore.GREEN + f'{type(T), type(V)}')
print(Fore.WHITE + Back.BLUE + f'{np.max(T), np.max(V)}')
print(Style.RESET_ALL)


'''
regresja
'''
start = 0
stop = 0
f = True
level = -1.87
for i in range(len(V)):
    if V[i]>level:
        if f:
            start = i
            f = False
        if V[i]>V[i-1]:
            stop = i

V_rise = np.array(data[start:stop,2]).astype(np.float)
T_rise = np.array(data[start:stop,0]).astype(np.float)
regr = linear_model.LinearRegression()
regr.fit(T_rise.reshape(-1,1), V_rise)
y_pred = regr.predict(T_rise.reshape(-1,1))
print(Back.GREEN + Fore.BLACK + f'współczynnik kierunkowy: {regr.coef_}')
print(Style.RESET_ALL)

'''
przeliczanie V na F
'''
F = np.array(V*(10**-6)*0.02*float(regr.coef_)).astype(np.float)

# plt.figure(figsize=(12,6))
# plt.scatter(T, V, color = 'k', marker='.', label='Deflection')
# plt.scatter(T_rise.reshape(-1,1), V_rise, color = 'b', marker='.', label='wybrane zbocze ↗')
# plt.plot(T_rise, y_pred, 'r', label='dopasowanie liniowe dla zbocza ↗')
# plt.xlabel('T (s)', fontsize = 12)
# plt.ylabel('[V]')
# plt.xticks(np.arange(0, np.max(T), step=(np.max(T)/10)))
# plt.yticks(np.arange(np.min(V), np.max(V), step = 0.5))
# plt.legend()
# plt.grid()
# plt.show()

plt.figure(figsize=(12,6))
# plt.scatter(Z, F, color='b', marker = '.')
plt.plot(Z, F, color='b')
plt.xlabel('odległość [um]', fontsize = 12)
plt.ylabel('siła [N]')
plt.xticks(np.arange(0, np.max(Z), step=(np.max(Z)/10)))
# plt.yticks(np.arange(np.min(F), np.max(F), step = 0.5))
plt.legend()
plt.grid()
plt.show()
