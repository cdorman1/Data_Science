import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df_adv = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col =0)
X = df_adv[['TV', 'Radio']]
y = df_adv['Sales']

## fit a OLS model with intercept on TV and Radio
X = sm.add_constant(X)
est = smf.ols(formula='Sales ~ TV + Radio', data=df_adv).fit()

print est.summary()