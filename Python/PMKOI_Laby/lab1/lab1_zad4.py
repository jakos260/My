import math as mt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 200)
y = np.log(x)

nojs = np.random.normal(0, 0.2, size=200)
y_noise = np.zeros(len(y))
for j in range(len(y)):
    y_noise[j] = y[j] + nojs[j]
    # print('y_noise',y_noise[j],'| y', y[j],'| nojs', nojs[j])


def okno(x, window):
    y_w = np.zeros(len(x))
    for i in range(len(x)):
        a = 0
        div = 0
        for j in range(window):
            if i+j<len(x):
                div = div + 1
                a = a + x[i+j]
        y_w[i] = a/div
        # print('y_n',i , y_w[i])
    return y_w


y_III = okno(y_noise, 3)
y_VII = okno(y_noise, 7)
y_XIII = okno(y_noise, 13)


fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 5), dpi=150)

ax[0].plot(x, y_III, color = 'g', label=('Averaged (N=3)'))
ax[1].plot(x, y_VII, color = 'g', label='Averaged (N=7)')
ax[2].plot(x, y_XIII, color = 'g', label='Averaged (N=13)')

ax[0].plot(x, y, color = 'r', label='original')
ax[0].plot(x, y_noise, color = 'b', label='+ Noise', linewidth=0.6)
ax[0].title.set_text('rozmiar okna = 3')
ax[0].grid()
ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')
legend = ax[0].legend(framealpha = 1, loc = 'lower right', facecolor='k')
for text in legend.get_texts():
    plt.setp(text, color = 'white')

ax[1].plot(x, y, color = 'r', label='original')
ax[1].plot(x, y_noise, color = 'b', label='+ Noise', linewidth=0.6)
ax[1].title.set_text('rozmiar okna = 7')
ax[1].grid()
ax[1].set_xlabel('X')
ax[1].set_ylabel('Y')
leg = ax[1].legend(framealpha = 1, loc = 'lower right', facecolor='k')
for text in leg.get_texts():
    plt.setp(text, color = 'w')

ax[2].plot(x, y, color = 'r', label='original')
ax[2].plot(x, y_noise, color = 'b', label='+ Noise', linewidth=0.6)
ax[2].title.set_text('rozmiar okna = 13')
ax[2].grid()
ax[2].set_xlabel('X')
ax[2].set_ylabel('Y')
leg = ax[2].legend(framealpha = 1, loc = 'lower right', facecolor='k')
for text in leg.get_texts():
    plt.setp(text, color = 'w')

# fig.suptitle('f(x) = log(x)', fontsize=18, y=1)
fig.tight_layout()
plt.show()


