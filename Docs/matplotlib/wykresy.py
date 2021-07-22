"""
różne wykresy, do wyboru do koloru :)

a na serio to:
> importowanie excelów,
> wybieranie z nich wektorów,
> przedstawianie ich na różnych wykresach

"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#_______nazwa___pliku__________

df = pd.read_excel(r'dane.xlsx', sheet_name='Dane')
print(df)

#________nazwa___kolumn_________

Tab = pd.DataFrame(df, columns=['T', 'L', 'H'])

t = Tab['T']
l = Tab['L']
h = Tab['H']


"""
______________wykres schodkowy___________

step(x, y, [fmt], *, data=None, where='pre', **kwargs)

Parametry:
> [fmt] = '[marker][line][color]'
> where = {'pre', 'post', 'mid'}
"""
# plt.figure(figsize=(12,6))
# plt.step(h, t, where='post', color = 'g', label = 'T')
# plt.xticks(np.arange(0, 50, step=5))
# plt.legend()
# plt.grid()
# plt.show()

"""
_____________wykres liniowy_______________

plot([x], y, [fmt], *, data=None, **kwargs)

Parametry:
> Linestyle:
        '-'	solid line style
        '--'	dashed line style
        '-.'	dash-dot line style
        ':'	dotted line style
> Colors:
        'b'	blue
        'g'	green
        'r'	red
        'c'	cyan
        'm'	magenta
        'y'	yellow
        'k'	black
        'w'	white
"""
# plt.figure(figsize=(12,6))
# plt.plot(h, l, color = 'r', linestyle = '--', label = 'L')
# plt.xlabel('hour', fontsize = 12)
# plt.xticks(np.arange(0, 50, step=5))
# plt.legend()
# plt.grid()
# plt.show()

"""
_________________wykres kropkowy_________________
plt.scatter(x, y, s, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)

Parametry:
> s = size kropek
> c = color kropek
> marker -> matplotlib.markers
> cmap = kolorki kropek (dla n-D wykresów)
> norm = skalowanie koloru (od 0 do 1)
> edgecolors = kolory krawędzi

"""
# plt.figure(figsize=(12,6))
# plt.scatter(h, l, c='r', s=20, marker='x', label='L')
# plt.xlabel('hour', fontsize = 12)
# plt.xticks(np.arange(0, 50, step=5))
# plt.legend()
# plt.grid()
# plt.show()


"""
_____________________wykres - 2 skale Y________________

fig, ax1 = plt.subplots()
    ax1(blablabla)
ax2 = ax1.twinx()
    ax2(blablabla)
fig.tight_layout()
"""

# ticks = np.arange(0,55,5) #generuje xticks'y
# fig, ax1 = plt.subplots(figsize=(12,7))

# ax1.set_xlabel('hour')
# ax1.set_ylabel('T', color = 'red')
# ax1.plot(h, t, color = 'r', label = 'T')
# ax1.tick_params(axis='y', labelcolor = 'red')
# # ax1.set_xscale('log') #rodzaj skali
# ax1.grid(linewidth=1, color = 'black')

# ax2 = ax1.twinx()
# ax2.set_ylabel('L', color = 'blue')
# ax2.plot(h, l, color = 'blue', label = 'L')
# ax2.tick_params(axis='y', labelcolor = 'blue')
# ax2.grid(linestyle='--')
# ax2.set_xticks(ticks) # wystarczy ustawić dla ostatniego
# ax2.set_title('T(hour) & L(hour)') # tak samo tytuł

# fig.text(0.5, 0.99, 'wykres podwójny', va='center', fontsize=14) #tytuł
# fig.tight_layout()
# plt.show()

"""
______________dużo wykresów___________
plt.subplots(nrows=i, ncols=j, sharex=False, sharey=False, squeeze=True, **fig_kw)

Parametry:
> nrow = ile wierszy
> ncols = ile kolumn
> sharex/sharey = współdzielenie osi x/y przez wykresy ['all','none','col','row']
> squeeze = ...
"""
# ticks = np.arange(0,50,10) #generuje xticks'y

# fig, ax = plt.subplots(nrows=2, ncols=2, sharey='row')

# ax[0,0].plot(h, t, 'r')
# ax[0,0].set_xticks(ticks)

# ax[0,1].plot(h, t, 'b')
# ax[0,1].set_xticks(ticks)

# ax[1,0].plot(h, l, 'k')
# ax[1,0].set_xticks(ticks)

# ax[1,1].plot(h, l, 'g')
# ax[1,1].set_xticks(ticks)
# ax[1,1].set_ylabel('label y [y_unit]')
# ax[1,1].set_xlabel('label x [x_unit]')

# fig.suptitle('kilka wykresów')

# plt.show()
