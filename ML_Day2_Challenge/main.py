import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('AQ_data_sets.csv', index_col=False)

x1 = df['x1']
y1 = df['y1']

plt.scatter(x1, y1)
plt.show()
