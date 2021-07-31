from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv(r'records/record_10.csv')
# df2 = pd.read_csv(r'records/record_9.csv')
# df3 = pd.read_csv(r'records/record_8.csv')

x1 = df1['t']
V1 = df1['v']
print(f'size x :{x1.shape}, v :{V1.shape}')
# x2 = df2['t']
# V2 = df2['v1']
# x3 = df3['t']
# V3 = df3['v']

plt.plot(x1, V1, color='r', label='10')
# plt.plot(x2, V2, 'b', label='9')
# plt.plot(x3, V3, 'g', label='8')
plt.grid()
plt.xlabel('ms')
plt.ylabel('mV')
# plt.legend()
# plt.show()

