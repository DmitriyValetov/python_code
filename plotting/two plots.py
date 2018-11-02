import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(pd.Series(np.random.uniform(0,1,size=10)), color='g')
ax2 = ax1.twinx()
ax2.plot(pd.Series(np.random.uniform(0,17,size=10)), color='r')
ax2.grid(False)
plt.show()
