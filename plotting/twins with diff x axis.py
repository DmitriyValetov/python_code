import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax2 = ax.twiny() # put a second plot on top of it, having the same y axis
data1 = np.random.random(10) #random in [0,1]
data2 = np.random.random(15)+1 #random in [1,2]

ax.plot(np.arange(len(data1)), data1) # plot in the first plot
ax2.plot(np.arange(len(data2)),data2) # plot in the second plot
plt.show()