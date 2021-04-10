import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#_______nazwa___pliku__________

df = pd.read_excel(r'mat3.xlsx', sheet_name='Dane')
print(df)
# print(df)
# print("typ: ", type(df))

#________nazwa___kolumn_________

# Tab = pd.DataFrame(df, columns=['Nr', 'bn', 'Uwe^1', 'Uwev1', 'Uk1', 'bk1', 'bh1', 'Uwy^2', 'Uwyv2', 'Uk2', 'bk2', 'bh2'])
# T = pd.DataFrame(df, columns=['materiał', 'pH0', 'y0', 'pH30', 'y30', 'pH60', 'y60', 'pH90', 'y90'])
# Tab = pd.DataFrame(df, columns=['pH0', 'pH30', 'pH60', 'pH90'])
# # Tab = pd.DataFrame(df, columns=['y0', 'y30', 'y60', 'y90'])
# Tab.index = df['materiał']
# Tab = Tab.transpose()
# Tab1 = pd.DataFrame(df, columns=['xst', '2st', '3st'])
# Tab2 = pd.DataFrame(df, columns=['X', 'CD'])
# Tab = pd.DataFrame(df, columns=['f', 'K', 'fi takie'])
# Tab = pd.DataFrame(df, columns=['r', 'D/t', 'D/t-tlo'])
# TabCu = pd.DataFrame(df, columns=['cu x', 'cu dt', 'cu a', 'cu b'])
# TabAl = pd.DataFrame(df, columns=['al x', 'al dt', 'al a', 'al b'])
# Tab = pd.DataFrame(df, columns=['U','Rx','U2', 'Rx2', 'U3', 'Rx3'])
# Tab_2 = pd.DataFrame(df, columns=["l","k","t","Ti","Ti^2"])
# print(Tab)
# print(Tab_2)
# Tab = pd.DataFrame(df, columns=['f', 'K', 'fi takie'])
# Tab = pd.DataFrame(df, columns=['f','K OI', 'K_OI', 'K OIK', 'K_OIK', 'K K', 'K_K'])
# Tab = pd.DataFrame(df, columns=['r', 'D/t-tlo'])
Tab = pd.DataFrame(df, columns=['T1', 'dL1', 'Alpha'])
Tab2 = pd.DataFrame(df, columns=['T2', 'dl/l2', 'alp2'])
Tab3 = pd.DataFrame(df, columns=['T3', 'dL3', 'alp3'])
Tab4 = pd.DataFrame(df, columns=['T4', 'dL4', 'alp4'])





# x = Tab['Uk1']
# # x1 = Tab['Uwe^1']
# # x2 = Tab['Uwev1']
# x1 = Tab['Uwy^2']
# x2 = Tab['Uwyv2']
# y = Tab['Nr']


#wykres schodkowy
# # print(y2)
# plt.figure(figsize=(15,10))
# # plt.step(Tab_1['Uwe'], Tab_1['Uwy'], where='post', color = 'b', label = 'Uwy')
# # plt.plot(Tab_1['Uwe'], Tab_1['Uwe'], color = 'r', label = 'U teoretyczne komutacji')
# plt.plot(x, y, color = 'r', label = 'U komutacji CA')
# plt.scatter(x, y, color = 'r')
# plt.step(x1, y, where='post', color = 'g', label = 'Uwy ^')
# plt.step(x2, y, where='post', color = 'g', linestyle = '--',label = 'Uwy v')
#
# plt.ylabel('nr diody', fontsize = 12)
# plt.xlabel('U [V]', fontsize = 12)
# plt.axis('auto')
# plt.legend()
# plt.grid()
# plt.show()

#wykres_schodkowy
# yn = Tab['Nr diody']
# plt.figure(figsize=(15,10))
# # plt.step(Tab_1['Uwe'], Tab_1['Uwy'], where='post', color = 'b', label = 'Uwy')
# # plt.plot(Tab_1['Uwe'], Tab_1['Uwe'], color = 'r', label = 'U teoretyczne komutacji')
# plt.step(y1, yn, where='post', color = 'b', label = 'napięcie wyjściowe UCA↑')
# plt.step(y2, yn, where='post', color = 'b', linestyle = '--',label = 'napięcie wyjściowe UCA↓')
# plt.plot(x1, x1*(16/5.5), color = 'r', label = 'zmiana Uwe')
# plt.plot(Tab['Utk'], yn, color = 'g', label = 'napięcie teoretyczne UAC komutacji')
# plt.scatter(Tab['Utk'], yn, color = 'g')
# plt.title('Wykres nr diody N(Uwy)', fontsize = 16)
# plt.ylabel('Nr diody', fontsize = 12)
# plt.xlabel('Uwy', fontsize = 12)
# plt.legend()
# plt.grid(str)
# plt.show()

#wykres kropkowy
# x1 = Tab_2['l']
# y1 = Tab_2['Ti']
# plt.figure(figsize = (10,15))
# plt.scatter(x1, y1, color = 'red', label = 'T(l)', alpha=1, marker='o', edgecolors='black')
# plt.title('Wykres T(l)', fontsize = 16)
# plt.ylabel('T [s]', fontsize = 12)
# plt.xlabel('l [m]', fontsize = 12)
# plt.grid(str)
# plt.show()

# #wykres liniowy
# x = Tab['U']
# y = Tab['Rx']
# x2 = Tab['U2']
# y2 = Tab['Rx2']
# x3 = Tab['U3']
# y3 = Tab['Rx3']
# y4 = Tab['K_OIK']
# y5 = Tab['K K']
# y6 = Tab['K_K']
# # # m, b = np.polyfit(x, y2, 1)
# # # print('a ', m)
# # # print('b ', b)
# #
# plt.figure(figsize = (16,9))
# plt.scatter(x, y2, color = 'red', label = 'T^2(l)', alpha=1, marker='o', edgecolors='black')
# plt.plot(x, y, 'b', label = 'H1')
# plt.plot(x2, y2, 'r', label = 'PY21W')
# plt.plot(x3, y3, 'g', label = 'W5W')
# plt.plot(x, y1, 'darkgreen')
# plt.plot(x, y1, 'b', linestyle = '--', label = 'K OI [dB]')
# plt.plot(x, y3, 'r', label = 'K OIK')
# plt.plot(x, y4, 'r', linestyle = '--', label = 'K OIK [dB]')
# plt.plot(x, y5, 'g', label = 'K K')
# plt.plot(x, y6, 'g', linestyle = '--', label = 'K K [dB]')
# plt.xscale('log')
# plt.ylabel('Rx [Ω]', fontsize = 12)
# plt.xlabel('U [V]', fontsize = 12)
# plt.legend()
# plt.grid(str)
# plt.show()
#
# plt.figure(figsize = (16,9))
# # plt.scatter(x, y2, color = 'red', label = 'T^2(l)', alpha=1, marker='o', edgecolors='black')
# plt.plot(x, y2, 'blue', label = 'K OI')
# plt.plot(x, y3, 'r', label = 'K OIK')
# plt.plot(x, y5, 'g', label = 'K K')
# plt.plot(x, y1, 'g', label = 'y1')
# plt.xscale('log')
# plt.ylabel('K', fontsize = 12)
# plt.xlabel('f [Hz]', fontsize = 12)
# plt.grid(str)
# plt.legend()
# # plt.show()
#
#
# fig, ax1 = plt.subplots(nrows=2, ncols=2, figsize=(16,9))

# ax1.set_xlabel('f [Hz]')
# ax1.set_ylabel('K', color = 'red')
# ax1.plot(x, y1, color = 'r', label = 'K O. inercyjnego')
# ax1.plot(x, y3, color = 'salmon', label = 'K O. inercyjnego z korektorem')
# ax1.plot(x, y5, color = 'darkred', label = 'K Korektora')
# ax1.tick_params(axis='y', labelcolor = 'red')
# ax1.set_xscale('log')
# ax1.grid(linewidth=1, color = 'black')
#
# ax2 = ax1.twinx()
# ax2.set_ylabel('K [dB]', color = 'blue')
# ax2.plot(x, y2, color = 'blue', label = 'K O. inercyjnego')
# ax2.plot(x, y4, color = 'dodgerblue', label = 'K O. inercyjnego z korektorem')
# ax2.plot(x, y6, color = 'darkblue', label = 'K Korektora')
# ax2.tick_params(axis='y', labelcolor = 'blue')
# ax2.set_xscale('log')
# ax2.grid(linestyle='--')
#
# print(Tab)
# x_pH = [0,30,60,90]
# xt = np.arange(0,100,10)
# y1 = Tab['ceramika']
# y2 = Tab['Mg 1']
# y3 = Tab['Mg 2']
# y4 = Tab['włókno węglowe']
# y5 = Tab['PEG 1']
# y6 = Tab['PEG 2']
# y = Tab['H2O']
#
#
# x = Tab['f']
# koi = Tab['K OI']
# k_oi = Tab['K_OI']
# koik = Tab['K OIK']
# k_oik = Tab['K_OIK']
# kk = Tab['K K']
# k_k = Tab['K_K']
#
# plt.figure(dpi=150, figsize=(10,5))
# plt.plot(x, koi, color='r', label = 'K o.inercyjnego')
# plt.plot(x, koik, color='darkred', label = 'K o.inercyjnego z korektorem')
# plt.plot(x, kk, color='coral', label = 'K korektora')
# plt.grid()
# plt.xscale('log')
# plt.ylabel('K [V/V]')
# plt.xlabel('f [Hz]')
# plt.legend(loc='center left')
# plt.show()
#
# plt.figure(dpi=150, figsize=(10,5))
# plt.plot(x, k_oi, color='b', label = 'K o.inercyjnego')
# plt.plot(x, k_oik, color='darkblue', label = 'K o.inercyjnego z korektorem')
# plt.plot(x, k_k, color='skyblue', label = 'K korektora')
# plt.grid()
# plt.xscale('log')
# plt.ylabel('K [dB]')
# plt.xlabel('f [Hz]')
# plt.legend()
# plt.show()

#
# fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10,10), sharex=True)

# ax[0].set_title('K [V/V]')
# ax[0].plot(x, koi, color='r', label = 'K o.inercyjnego')
# ax[0].plot(x, koik, color='r', label = 'K o.inercyjnego z korektorem')
# ax[0].plot(x, kk, color='r', label = 'K korektora')
# ax[0].grid()
# ax[0].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
# ax[0].set_xscale('log')
# ax[0].set_ylabel('[V/V]', color='r')
# ax[0].tick_params(axis='y', labelcolor = 'r')

# ax[1].set_title('K obiektu inercyjnego z korektorem')
#
# ax[1].grid()
# ax[1].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
# ax[1].set_xscale('log')
# ax[1].set_ylabel('[V/V]', color='r')
# ax[1].tick_params(axis='y', labelcolor = 'r')
#
# ax[2].set_title('K korektora')
#
# ax[2].grid()
# ax[2].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
# ax[2].set_xscale('log')
# ax[2].set_ylabel('[V/V]', color='r')
# ax[2].tick_params(axis='y', labelcolor = 'r')
# ax[2].set_xlabel('f [Hz]')

# ax.tick_params(axis='y', labelcolor = 'red')
#
# ax[0] = ax[0].twinx()
# ax[1] = ax[1].twinx()
# ax[2] = ax[2].twinx()


# ax[0].set_yticks([10, 0, -10, -20, -30, -40, -50])
# ax[0].tick_params(axis='y', labelcolor = 'b')
# ax[0].set_ylabel('[dB]', color='b')

# ax[0].set_title('K [dB]')
# ax[1].plot(x, k_oik, color='b', label = 'K o.inercyjnego z korektorem [dB]')
# ax[1].plot(x, k_oi, color='b', label = 'K o.inercyjnego [dB]')
# ax[1].plot(x, k_k, color='b', label = 'K korektora [dB]')
# ax[1].set_yticks([10, 0, -10, -20, -30, -40, -50])
# ax[1].tick_params(axis='y', labelcolor = 'b')
# ax[1].set_ylabel('[dB]', color='b')


# ax[2].set_yticks([10, 0, -10, -20, -30, -40, -50])
# ax[2].tick_params(axis='y', labelcolor = 'b')
# ax[2].set_ylabel('[dB]', color='b')


# ax2.tick_params(axis='y', labelcolor = 'blue')
#
#
# ax[1,1].plot(x_pH, y5, color='b', label = 'PEG 1')
# ax[1,1].plot(x_pH, y6, color='orange', label = 'PEG 2')
# ax[1,1].plot(x_pH, y, color='gray', label = 'próbka kontrolna')
# ax[1,1].grid()
# ax[1,1].set_xticks(xt)
# ax[1,1].legend()

# fig.tight_layout()
#
# fig.text(0.5, 0.04, 'f [Hz]', ha='center', va='center', fontsize=14)
# fig.text(0.03, 0.5, 'K', ha='center', va='center', fontsize=14)
# plt.show()

#, rotation='vertical'
# x = Tab['f']
# y1 = Tab['RIGOL']
# y2 = Tab['V560']
# y3 = Tab['PE-2']
# xst = Tab1['xst']
# dst = Tab1['2st']
# tst = Tab1['3st']
# x = Tab2['X']
# CD = Tab2['CD']
#
# plt.figure(figsize = (16,9))
# plt.plot(xst, dst, 'b', label = 'wielomian 2 stopnia')
# plt.plot(xst, tst, 'g', label = 'wielomian 3 stopnia')
# plt.scatter(x, CD, color='red', label = 'zmierzone wartości')
# plt.plot(x, y1, 'darkgreen')
# plt.plot(x, y1, 'b', linestyle = '--', label = 'K OI [dB]')
# plt.plot(x, y3, 'r', label = 'K OIK')
# plt.plot(x, y4, 'r', linestyle = '--', label = 'K OIK [dB]')
# plt.plot(x, y5, 'g', label = 'K K')
# plt.plot(x, y6, 'g', linestyle = '--', label = 'K K [dB]')
# plt.xscale('log')
# plt.ylabel('Cd [pF*mm]', fontsize = 12)
# plt.xlabel('d [mm]', fontsize = 12)
# plt.legend()
# plt.grid(str)
# plt.show()

# x = 0.01 * Tab['r']
# y1 = Tab['D/t']
# y2 = Tab['D/t-tlo']
#
# plt.figure(figsize = (16,9))
# plt.plot(x, y1, 'b', label = 'D/t')
# plt.plot(x, y2, 'r', label = 'D/t - tło')
#
# plt.ylabel('D/t\n[µSv/h]', fontsize = 12)
# plt.xlabel('r [m]', fontsize = 12)
# plt.legend()
# plt.grid(str)
# plt.show()

# x = 0.01*TabCu['cu x']
# y1 = TabCu['cu dt']
# y2 = TabCu['cu a']*TabCu['cu x']+TabCu['cu b']
#
# plt.figure(figsize = (16,9))
# plt.plot(x, y1, 'b', label = 'ln(D/t)')
# plt.plot(x, y2, 'r', label = 'regr ln(D/t)')
#
# plt.ylabel('D/t\n[µSv/h]', fontsize = 12)
# plt.xlabel('r [m]', fontsize = 12)
# plt.legend()
# plt.grid(str)
# plt.show()


# plt.figure(figsize = (15,10))
# plt.plot(Tab['f'], Tab['K'], color = 'g', label = 'K')
# plt.ylabel('K', fontsize = 12)
# plt.xlabel('f [Hz]', fontsize = 12)
# plt.xticks(np.arange(0, 2420, step=220))
# plt.grid(str)
# plt.show()
#
# plt.figure(figsize = (15,10))
# plt.plot(Tab['f'], Tab['fi takie'], color = 'b')
# plt.ylabel('φ', fontsize = 16)
# plt.xlabel('f [Hz]', fontsize = 12)
# plt.xticks(np.arange(0, 2420, step=220))
# plt.grid(str)
# plt.show()

# x = np.linspace(0, 2, 8)
# y_cu = 1.455655**(-0.960364*x)
# y_al = 1.350056**(-0.987432*x)
#
#
# plt.figure(figsize = (15,10))
# plt.plot(x, y_cu, color = 'g', label = 'Cu y=1.455655^(-0.960364*x)')
# plt.plot(x, y_al, color = 'b', label = 'Al y=1.350056^(-0.987432*x)')
# plt.ylabel('D/t\n[μSv/h]', fontsize = 12)
# plt.xlabel('X [cm]', fontsize = 12)
# # plt.xscale('log')
# plt.yticks([0,0.25,0.5,0.75,1,1.25])
# plt.legend()
# plt.grid(str)
# plt.show()


# x = Tab['r']
# y = Tab['D/t-tlo']
# p = np.poly1d(np.polyfit(x, y, 1))
#
#
#
# plt.figure(figsize = (15,10))
# plt.scatter(x, y, color = 'r')
# plt.plot(x, p(x), 'r--')
# plt.ylabel('D/t\n[μSv/h]', fontsize = 12)
# plt.xlabel('X [cm]', fontsize = 12)
# # plt.xscale('log')
# # plt.yticks([0,0.25,0.5,0.75,1,1.25])
# plt.grid(str)
# plt.show()

# x = np.linspace(0, 10, 12000)
# y = np.zeros(len(x))
# y_1 = np.zeros(len(y))
# y_2 = np.zeros(len(y))
# y_3 = np.zeros(len(y))
#
# filtr = np.zeros(2000)
# for i in range(len(filtr)-1):
#     filtr[i] = 1 - (i/2000)
#
# filtr2 = np.zeros(2000)
# for i in range(np.int((len(filtr2)-1)/2)):
#     filtr2[i] = 1 - (i/1000)
#
# filtr3 = np.zeros(2000)
# for i in range(np.int((len(filtr2)-1)/8)):
#     filtr3[i] = 1 - (i/250)
#
# print(filtr)
# print(filtr2)
#
# for i in range(3):
#
#     for a in range(2000):
#         indexa = i*4000+a
#         y[indexa] = 1
#         y_1[indexa] = y[indexa] - 0.2 * filtr[a] * np.sin(40 * x[a])
#         y_2[indexa] = y[indexa] - 0.1 * filtr2[a] * np.sin(40 * x[a])
#         y_3[indexa] = y[indexa] - 0.05 * filtr3[a] * np.sin(40 * x[a])
#
#     for b in range(2000):
#         indexb = i*4000+2000+b
#         y[indexb] = 3
#         y_1[indexb] = y[indexb] + 0.2 * filtr[b] * np.sin(40 * x[b])
#         y_2[indexb] = y[indexb] + 0.1 * filtr2[b] * np.sin(40 * x[b])
#         y_3[indexb] = y[indexb] + 0.05 * filtr3[b] * np.sin(40 * x[b])
#
# plt.figure(figsize = (15,10))
# plt.plot(x, y_1, color = 'b', label='Z1')
# plt.plot(x, y_2, color = 'g', label='Z2')
# plt.plot(x, y_3, color = 'r', label='Z3')
# plt.plot(x, y, color = 'k', label='sygnał wejściowy')
# plt.ylabel('U [V]', fontsize = 16)
# plt.xlabel('t [ms]', fontsize = 16)
# plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
# plt.legend(fontsize = 12)
# plt.grid(str)
# plt.show()


x = Tab['T1']
y = Tab['dL1']
a = Tab['Alpha']
x2 = Tab2['T2']
y2 = Tab2['dl/l2']
a2 = Tab2['alp2']
x3 = Tab3['T3']
y3 = Tab3['dL3']
a3 = Tab3['alp3']
x4 = Tab4['T4']
y4 = Tab4['dL4']
a4 = Tab4['alp4']





# plt.figure(figsize = (15,10))
# plt.plot(x, y, color = 'g', label = 'dL')
# plt.plot(x, a, color = 'r', label = 'α')
# plt.title('∆L = f(T) dla ZrO2', fontsize = 20)
# # plt.plot(x, y_al, color = 'b', label = 'Al y=1.350056^(-0.987432*x)')
# plt.ylabel('∆L [mm]', fontsize = 12)
# plt.xlabel('T [˚C]', fontsize = 12)
# # plt.xscale('log')
# # plt.yticks([0,0.25,0.5,0.75,1,1.25])
# plt.legend()
# plt.grid(str)
# plt.show()

fig, ax1 = plt.subplots(figsize = (10,6))

color = 'tab:red'
ax1.set_xlabel('T [˚C]')
ax1.set_ylabel('∆L [mm]', color=color)
ax1.plot(x, y, color=color, label = 'dL')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(linewidth=0.9, color = 'black')

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('α', color=color)
ax2.plot(x, a, color=color)
ax2.tick_params(axis='y', labelcolor=color)
# ax2.grid(linewidth=0.5, color = color)

fig.text(0.5, 0.98, '∆L = f(T) dla ZrO2', ha='center', va='center', fontsize=14)
fig.tight_layout()
plt.show()



# fig, ax1 = plt.subplots(figsize = (16,9))
#
# color = 'tab:red'
# ax1.set_xlabel('T [˚C]')
# ax1.set_ylabel('∆L/L [mm]', color=color)
# ax1.plot(x2, y2, color=color, label = '∆L/L')
# ax1.tick_params(axis='y', labelcolor=color)
# ax1.grid(linewidth=0.9, color = 'black')
#
# ax2 = ax1.twinx()
#
# color = 'tab:blue'
# ax2.set_ylabel('α', color=color)
# ax2.plot(x2, a2, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
# # ax2.grid(linewidth=0.5, color = color)
#
# fig.text(0.5, 0.98, '∆L = f(T) dla SiO2', ha='center', va='center', fontsize=14)
# fig.tight_layout()
# plt.show()



# fig, ax1 = plt.subplots(figsize = (16,9))
#
# color = 'tab:red'
# ax1.set_xlabel('T [˚C]')
# ax1.set_ylabel('∆L [μm]', color=color)
# ax1.plot(x3, y3, color=color, label = '∆L')
# ax1.tick_params(axis='y', labelcolor=color)
# ax1.grid(linewidth=0.9, color = 'black')
#
# ax2 = ax1.twinx()
#
# color = 'tab:blue'
# ax2.set_ylabel('α', color=color)
# ax2.plot(x3, a3, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
# # ax2.grid(linewidth=0.5, color = color)
#
# fig.text(0.5, 0.98, '∆L = f(T) dla SiC', ha='center', va='center', fontsize=14)
# fig.tight_layout()
# plt.show()


#
# fig, ax1 = plt.subplots(figsize = (16,9))
#
# color = 'tab:red'
# ax1.set_xlabel('T [˚C]')
# ax1.set_ylabel('∆L [μm]', color=color)
# ax1.plot(x4, y4, color=color, label = '∆L')
# ax1.tick_params(axis='y', labelcolor=color)
# ax1.grid(linewidth=0.9, color = 'black')
#
# ax2 = ax1.twinx()
#
# color = 'tab:blue'
# ax2.set_ylabel('α', color=color)
# ax2.plot(x4, a4, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
# # ax2.grid(linewidth=0.5, color = color)
#
# fig.text(0.5, 0.98, '∆L = f(T) dla Cu', ha='center', va='center', fontsize=14)
# fig.tight_layout()
# plt.show()