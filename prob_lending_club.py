import matplotlib.pyplot as plt

import pandas as pd

loansData = pd.read_csv('/home/cdorman/PycharmProjects/Thinkful/git/Data_Science/lending_club.csv')

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Funded.By.Investors', return_type='dict')

plt.show()
