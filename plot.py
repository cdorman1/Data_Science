import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as ml

mean = 0
variance = 1
sigma = np.sqrt(variance) # this is the standard deviation
x = np.linspace(-3,3,100)
plt.plot(x, ml.normpdf(x,mean,sigma))

plt.show()