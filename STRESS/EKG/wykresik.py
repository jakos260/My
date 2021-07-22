import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_excel(r'data.xlsx', sheet_name='data')
# df2 = pd.read_excel(r'2.xlsx', sheet_name='data')
# df3 = pd.read_excel(r'3.xlsx', sheet_name='data')

x1 = df1['ms']
V1 = df1['mV']
# x2 = df2['mS']
# V2 = df2['mV']
# x3 = df3['mS']
# V3 = df3['mV']

plt.plot(x1, V1, 'r', label='bez filtra')
# plt.plot(x2, V2, 'b', label='10uF')
# plt.plot(x3, V3, 'g', label='20uF')
plt.grid()
plt.xlabel('ms')
plt.ylabel('mV')
# plt.legend()
plt.show()