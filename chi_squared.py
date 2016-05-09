import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('/home/cdorman/PycharmProjects/Thinkful/git/Data_Science/lending_club.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.xlabel("Open Credit Lines")
plt.ylabel("Count")
plt.show()

chi, p = stats.chisquare(freq.values())
print chi
print p