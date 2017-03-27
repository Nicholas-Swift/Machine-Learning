import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('winequality-red.csv', index_col=False)

# print(df.describe())

total_sulfur_dioxide = df.ix[:,8]
quality = df.ix[:,11]

plt.scatter(total_sulfur_dioxide, quality)
plt.show()
