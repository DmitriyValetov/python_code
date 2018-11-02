import numpy as np
import matplotlib.pyplot as plt
from seaborn import barplot
import pandas as pd

fig, ax = plt.subplots()
ax2 = ax.twinx() # put a second plot on top of it, having the same y axis
data1 = np.random.random(10) #random in [0,1]
data2 = np.random.random(10)+1 #random in [1,2]

print(np.array(list(range(len(data1)))))
print(data1)
print(data2)

df = pd.DataFrame({'x': list(range(len(data1))), 'y1': data1, 'y2' : data2})

# ax.plot(np.arange(len(data1)), data1, kind='bar') # plot in the first plot
barplot(x='x', y='y1', data=df, ax=ax)
ax2.plot(np.arange(len(data2)),data2) # plot in the second plot
plt.show()