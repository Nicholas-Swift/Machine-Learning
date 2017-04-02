import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('AQ_data_sets.csv', index_col=False)

data_sets = []
for i in range(1, 4+1):
    x = df['x{}'.format(i)]
    y = df['y{}'.format(i)]
    data_set = (x, y)
    data_sets.append(data_set)

plt.scatter(data_sets[0][0], data_sets[0][1])
plt.show()
