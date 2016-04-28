import collections
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

testlist = [1, 4, 5, 6, 9, 9, 9]

frequency = collections.Counter(testlist)

for k, v in frequency.iteritems():
    print("%s is found %s times in the list!" % (k, v))

plt.figure('boxplot_of_testlist_data')
plt.boxplot(testlist)
plt.show()
plt.savefig('boxplot_of_testlist_data.pdf')

plt.figure('histogram_of_testlist_data')
plt.hist(testlist, histtype='bar')
plt.show()
plt.savefig('histogram_of_testlist_data.pdf')

plt.figure('qqplot_of_testlist_data')
testlist_graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.show()
plt.savefig('qqplot_of_testlist_data.pdf')
