import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'a': [100, 200, 150, 175],
                   'b': [430, 30, 20, 10]})

fig, ax1 = plt.subplots(figsize=(15, 10))

df['b'].plot(kind='bar', color='y')
df['a'].plot(kind='line', marker='d')

plt.show()