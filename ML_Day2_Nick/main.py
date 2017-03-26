import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zoo.csv', index_col=False)
column_names = ['animal', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'type']
df.columns = column_names


antelope = df.loc[df['animal'] == 'antelope']
boar = df.loc[df['animal'] == 'boar']
deer = df.loc[df['animal'] == 'deer']
carp = df.loc[df['animal'] == 'carp']
catfish = df.loc[df['animal'] == 'catfish']
bass = df.loc[df['animal'] == 'bass']
scorpion = df.loc[df['animal'] == 'scorpion']
wasp = df.loc[df['animal'] == 'wasp']

antelope_data = [antelope['legs'], antelope['hair']]
boar_data = [boar['legs'], boar['hair']]
deer_data = [deer['legs'], deer['hair']]
carp_data = [carp['legs'], carp['hair']]
catfish_data = [catfish['legs'], catfish['hair']]
bass_data = [bass['legs'], bass['hair']]
scorpion_data = [scorpion['legs'], scorpion['hair']]
wasp_data = [wasp['legs'], wasp['hair']]


plt.scatter(antelope_data[0], antelope_data[1], s=50, alpha=0.3, c='g')
plt.scatter(boar_data[0], boar_data[1], s=50, alpha=0.3, c='g')
plt.scatter(deer_data[0], deer_data[1], s=50, alpha=0.3, c='g')
plt.scatter(carp_data[0], carp_data[1], s=50, alpha=0.3, c='g')
plt.scatter(catfish_data[0], catfish_data[1], s=50, alpha=0.3, c='g')
plt.scatter(bass_data[0], bass_data[1], s=50, alpha=0.3, c='g')
plt.scatter(scorpion_data[0], scorpion_data[1], s=50, alpha=0.3, c='g')
plt.scatter(wasp_data[0], wasp_data[1], s=50, alpha=0.3, c='g')
plt.show()