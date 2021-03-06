import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.cross_validation import KFold
import collections

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('/Users/chrisdorman/PycharmProjects/Thinkful/git/Data_Science/lending_club.csv')
# Drop null rows
loansData.dropna(inplace=True)

interest_rates = loansData['Interest.Rate']
loansData['Interest.Rate'] = map(lambda x: float(x.strip('%')), interest_rates)

loan_length = loansData['Loan.Length']
loansData['Loan.Length'] = map(lambda x: x.strip('months'), loan_length)

fico_range = loansData['FICO.Range']
loansData['FICO.Score'] = map(lambda x: int(tuple(x.split('-'))[0]), fico_range)

loan_amount = loansData['Amount.Requested']
loansData['Amount.Requested'] = map(lambda x: int(x), loan_amount)

loansData.to_csv('loansData_clean.csv', header=True, index=False)

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']


# The dependent variable
y = np.matrix(intrate).transpose()
# #The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1, x2])



kf = KFold(len(x), n_folds=10)
for train, test in kf:
    print('%s, %s' %(train, test))
    # mean_squared_error()
    # mean_absolute_error()
    # r2_score()
