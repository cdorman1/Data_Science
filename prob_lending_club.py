import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


loansData = pd.read_csv('/home/cdorman/PycharmProjects/Thinkful/git/Data_Science/lending_club.csv')

loansData.dropna(inplace=True)

amount_funded_df = pd.DataFrame(loansData['Amount.Funded.By.Investors'])
print "Average", amount_funded_df.mean()

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

plt.figure('Amount Funded By Investor')
af_graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()

amount_requested_df = pd.DataFrame(loansData['Amount.Requested'])
print amount_requested_df.mean()

plt.figure('boxplot_of_Amount_Requested')
loansData.boxplot(column='Amount.Requested')
plt.show()
plt.savefig('boxplot_of_Amount_Requested.pdf')

plt.figure('histogram_of_Amount_Requested')
loansData.hist(column='Amount.Requested')
plt.show()
plt.savefig('histogram_of_Amount_Requested.pdf')

plt.figure('qqplot_of_Amount_Requested')
ar_qqgraph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()
plt.savefig('qqplot_of_Amount_Requested.pdf')


# The R squared is slightly lower for the Amount Requested than the Amount Funded by investors.
# The average amount of funds requested was ~$12,413
# The average amount of funds distributed by investors was ~$12,009
# It seems that loan requests of $10,000 or less were indeed funded.