'''
opracowanie biblioteki pandas
'''
import pandas as pd

# ___________________tworzenie nowego data_frame_______________
df = pd.DataFrame([[1, 4, 2], [2, 6, 5]] ,columns=['A', 'B', 'C'])
# print(df)

# _________________tworzenie data_frame za pomocą klasy_______________
from dataclasses import make_dataclass as mc
point = mc('point', [('x', int), ('y', int)])
df2 = pd.DataFrame([point(2, 4), point(0, 9), point(8, 6)])
# print(df2)

# ______________________append______________________________
df3 = pd.DataFrame([point(7, 5), point(3, 4)])
df2 = df2.append(df3)
# print(df2)

df4 = pd.DataFrame([[2, 4, 5]], columns=['B', 'A', 'C'])
df = df.append(df4)
# print(df)

df5 = df2.append(df4)
# print(df5)

# ________________wywoływanie elementów____________________
a = df2['x'][1]
print(df2, '\ndf2[x][1]', a, type(a))

df6 = pd.DataFrame([[df2['x'], df2['y']]], columns=['x', 'y'])
print(df6, 'df6')
