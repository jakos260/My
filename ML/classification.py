import pandas as pd
from sklearn.linear_model import LogisticRegression

pd.options.display.max_rows = 5
df = pd.read_csv('titanic.csv')
df['Male'] = df['Sex'] == 'male'

# X = df[['Pclass', 'Male', 'Age', 'SibSp', 'Parch', 'Fare']].values
# print(X)
arr = df[['Survived', 'Fare', 'Age', 'Pclass', 'SibSp', 'Parch', 'Male']].values
arr = arr[arr[:,2] > -1]
# arr = arr[arr[:,6] < 2]
X = arr[:,1:7]
y = arr[:,0]
y = y.astype('int')
print(X)

model = LogisticRegression()
model.fit(X, y)
# print(model.coef_, model.intercept_)
pred_y = model.predict(X)

# print('bedzie zyl?', pred_y[:5])
# print('a zyje?', y[:5])

sum_all = y.shape[0]
sum_luck = (pred_y > y).sum()
sum_badluck = (pred_y < y).sum()
sum_pred = (pred_y == y).sum()

# sum_luck = 0
# sum_badluck = 0
# sum_pred = 0
# for i in range(sum_all):
#     if pred_y[i] > y[i]:
#         sum_badluck += 1
#     elif pred_y[i] < y[i]:
#         sum_luck += 1
#     elif pred_y[i] == y[i]:
#         sum_pred += 1

print('wszyscy _', sum_all, '\nmieli umrzeć a żyją _', sum_luck, '\nmieli żyć a umarli _', sum_badluck, '\npoprawnie przewidzano los _', sum_pred)
print('\ndokładność modelu ==>', sum_pred/y.shape[0])


