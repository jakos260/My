import numpy as np
from sklearn import datasets, linear_model

#tu zaimportuj dane

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, Y_train)
# Predict values
Y_predicted = regr.predict(X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean square error
error = np.mean((regr.predict(X_test) - Y_test) ** 2)
print("Residual sum of squares: {}".format(error))