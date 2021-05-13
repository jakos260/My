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
filename2 = 'podejscie3_ostrze6c_1_52__00001_2a_2.mi'
data2 = np.loadtxt(filename2, delimiter='	', skiprows=1, dtype=str)

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
            print(Fore.GREEN + f'start index: {start}')
            print(Style.RESET_ALL)
        if V[i]>V[i-1]:
            stop = i
            
print(Fore.RED + f'ostateczny stop index: {stop}')
print(Style.RESET_ALL)


V_rise = np.array(data[start:stop,2]).astype(np.float)
Z_rise = np.array(data[start:stop,1]).astype(np.float)
regr = linear_model.LinearRegression()
regr.fit(Z_rise.reshape(-1,1), V_rise)
y_pred = regr.predict(Z_rise.reshape(-1,1))
print(Back.GREEN + Fore.BLACK + f'współczynnik kierunkowy: {regr.coef_}')
print(Style.RESET_ALL)

'''
przeliczanie V na F
'''
F = np.array(V*(10**-6)*0.02*abs(float(regr.coef_))).astype(np.float)
V_m = np.array(data2[:,2]).astype(np.float)
T_m = np.array(data2[:,0]).astype(np.float)
Z_m = -np.array(data2[:,1]).astype(np.float)
F_m = np.array(-V_m*(10**-6)*0.02*float(regr.coef_)).astype(np.float)

'''
wykres 1 - kalibracja
'''
# plt.figure(figsize=(10,7))
# plt.scatter(-Z + 1.5, V, color = 'k', marker='.', label='Deflection')
# plt.scatter(-Z_rise.reshape(-1,1) +1.5, V_rise, color = 'b', marker='.', label='wybrane zbocze ↗')
# plt.plot(-Z_rise +1.5, y_pred, 'r', label=f'dopasowanie liniowe dla zbocza ↗ \na = {abs(round(float(regr.coef_), 4))}')
# plt.xlabel('Z [um]', fontsize = 12)
# plt.ylabel('[V]')
# # plt.xticks(np.arange(0, -np.max(Z)+1.5, step=((np.max(Z) +1.5)/10)))
# plt.yticks(np.arange(np.min(V), np.max(V), step = 0.5))
# plt.legend()
# plt.grid()
# plt.show()


F = np.array(F+ 2*10**-7).astype(np.float)
stop_m = np.argmax(F) + 1

'''
wykres 2 - siła
'''

# plt.figure(figsize=(10,7))
# # plt.scatter(Z_m, F_m, color='k', marker='*')
# plt.scatter(Z_m[0:stop_m], F_m[0:stop_m], color='k', marker='.', label='siła F')
# plt.plot(-Z[start:stop] +2.13, F[start:stop], color='r', label='siła F - kalibracja')
# plt.xlabel('odległość [um]', fontsize = 12)
# plt.ylabel('siła [N]')
# # plt.xticks(np.arange(0, np.max(T), step=(np.max(T)/10)))
# # plt.yticks(np.arange(np.min(V), np.max(V), step = 0.5))
# plt.legend()
# plt.grid()
# plt.show()


'''
wykres 3 - indentacja
'''

ind_start = 0
for i in range(len(Z_m[start:stop])):
    ind_start=i
ind = Z_m[start:stop] - Z[start:stop]

plt.figure(figsize=(10,7))
plt.scatter(F[start:stop], ind, color='k', marker='.', label='indentacja')
plt.xlabel('odległość [um]', fontsize = 12)
plt.ylabel('siła [N]')
# plt.xticks(np.arange(0, np.max(T), step=(np.max(T)/10)))
# plt.yticks(np.arange(np.min(V), np.max(V), step = 0.5))
plt.legend()
plt.grid()
plt.show()