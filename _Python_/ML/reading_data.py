import pandas as pd
pd.options.display.max_columns = 7
df = pd.read_csv('titanic.csv')
# print(df.describe())
#
# col = df['Fare']
# print('_fare_\n', col[0:3])
# col2 = df[['Age', 'Sex', 'Survived']]
# print('_col2_\n', col2.head())
# df['male'] = df['Sex'] == 'male'
# print(df.head())

# array = df[['Fare', 'Sex']]
# print(array.values)
# print('array shape =>', array.shape)
arr = df[['Pclass', 'Fare', 'Sex', 'Age']].values
# print(arr[0,0:2])
# print(arr[0])
# print(arr[1:3])
# print('[1,:]', arr[1,:])

mask = arr[:, 3] < 18
# print(mask)
print(arr[mask][0])
print(arr[arr[:, 3] < 18][0])
print('sum of true', mask.sum())
