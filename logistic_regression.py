import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('/home/cdorman/PycharmProjects/Thinkful/git/Data_Science/loansData_clean.csv')

df['IR_TF'] = [0 if x < 12 else 1 for x in df['Interest.Rate']]

df['Intercept'] = 1.0

ind_vars = ['Intercept', 'Interest.Rate', 'Amount.Requested', 'FICO.Score']

logit = sm.Logit(df['IR_TF'], df[ind_vars])

result = logit.fit()

coeff = result.params
print coeff
