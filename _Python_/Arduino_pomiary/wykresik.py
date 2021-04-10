# import pandas as pd
#
# col = ['A', 'B', 'C']
#
# df = pd.DataFrame(columns=col)
# for i in range(5):
#     df = df.append(pd.DataFrame([[0, 2, i]], columns=col), ignore_index=True)
#
# print(df)

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'temp_rekord.xlsx', sheet_name='Dane')


T = df['T']
L = df['L']
H = df['H']

fig, ax1 = plt.subplots(figsize = (10,6))

color = 'tab:red'
ax1.set_xlabel('czas')
ax1.set_ylabel('T [˚C]', color=color)
ax1.plot(H, T, color=color, label = 'T')
# ax1.tick_params(axis='y', which='major', labelcolor=color)
# ax1.grid(linewidth=0.9, color = 'black')

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('L', color=color)
ax2.plot(H, L, color=color, label = 'L')
# ax2.tick_params(axis='y', labelcolor=color)
# ax2.grid(linewidth=0.5, color = color)

fig.text(0.5, 0.98, '∆L = f(T) dla ZrO2', ha='center', va='center', fontsize=14)
fig.tight_layout()
plt.show()