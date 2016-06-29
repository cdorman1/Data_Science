import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.metrics import mean_squared_error

# Set seed for reproducible results
np.random.seed(414)

# Gen toy data
X = np.linspace(0, 15, 1000)
y = 3 * np.sin(X) + np.random.normal(1 + X, .2, 1000)

train_X, train_y = X[:700], y[:700]
test_X, test_y = X[700:], y[700:]

train_df = pd.DataFrame({'X': train_X, 'y': train_y})

test_df = pd.DataFrame({'X': test_X, 'y': test_y})
# Linear Fit
poly_1 = smf.ols(formula='y ~ 1 + X', data=train_df).fit()

# Quadratic Fit
poly_2 = smf.ols(formula='y ~ 1 + X + I(X**2)', data=train_df).fit()

# Use mean squared error as a metric,
# compare the performance of different
# polynomial curves in the training set and in the testing set
ols_predict = poly_1.predict(train_df['X'])[:700]
#Quadratic model
quad_predict = poly_2.predict(train_df['X'])[:700]

## similarly if you use test set

# ols_predict = poly_1.predict(test_df['X'])[700:]
#
# # Quadratic model
# quad_predict = poly_2.predict(test_df['X'])[700:]



# Use mean squared error as a metric,
# compare the performance of different
# polynomial curves in the training set and in the testing set
# Evaluation with training mean-square error (MSE)
# Linear model
print mean_squared_error(train_df['y'], ols_predict)
# Quadratic model
# mean_squared_error(train_df['y'], quad_predict)
