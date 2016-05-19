import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('/home/cdorman/PycharmProjects/Thinkful/git/Data_Science/loansData_clean.csv')

df['IR_TF'] = [0 if x < 12 else 1 for x in df['Interest.Rate']]

df['Intercept'] = 1.0

ind_vars = ['Intercept', 'Amount.Requested', 'FICO.Score']

def logistic_function(FicoScore, LoanAmount, coeff):
    prob = 1 / (1 + np.exp(coeff[0] + coeff[2] * FicoScore + coeff[1] * LoanAmount))
    if prob > 0.7:
        p = 1
    else:
        p = 0

    return prob, p

logit = sm.Logit(df['IR_TF'], df[ind_vars])

result = logit.fit()

coeff = result.params

prob = logistic_function(720, 10000, coeff)[0]
decision = logistic_function(720, 10000, coeff)[1]

print prob
print decision

## plotting: lets test different FICO score for 10,000 USD loan
Fico = range(550, 950, 10)
p_plus = []
p_minus = []
p = []
for j in Fico:
    p_plus.append(1/(1+ np.exp(coeff[0]+coeff[2]*j+coeff[1]*10000)))
    p_minus.append(1/(1+ np.exp(-coeff[0]-coeff[2]*j-coeff[1]*10000)))
    p.append(logistic_function(j, 10000,coeff)[1])

plt.plot(Fico, p_plus, label = 'p(x) = 1/(1+ exp(b+mx))', color = 'blue')
plt.hold(True)
# plt.plot(Fico, p_minus, label = 'p(x) = 1/(1+ exp(-b-mx))', color = 'green')
# plt.hold(True)
plt.plot(Fico, p, 'ro', label = 'Decision for 10000 USD')
plt.legend(loc='upper right')
plt.xlabel('Fico Score')
plt.ylabel('Probability and decision, yes = 1, no = 0')
plt.show()

