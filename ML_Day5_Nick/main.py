# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans

# df = pd.read_csv("dataset.csv")

# # Change all ? to NaN
# for column in df.columns:
#     try: df[column][df[column] == "?"] = np.nan
#     except: continue

# # Replace all NaN with mean
# for column in df.columns:
#     df[column] = df[column].fillna(df[column].mean())
#     # try: df[column][df[column] == np.nan] = df[column].mean()
#     # except: continue

# # Train a KMeans model
# model = KMeans().fit(df)

# print(model)

class Matter:
    def __init__(self):
        pass

    def Solid(self, style):
        self.style = style
        return self.style

    def Liquid(self):
        print("like water")

    def Gas(self, nature = "like oxygen"):
        self.nature = nature

    def Bose(self):
        self.nature = "like a condensate"
        print(self.nature)

def main():
    matter = Matter()
    matter.Solid("Solid like a rock")
    matter.Liquid()
    matter.Gas(self.nature)
    matter.Bose()

main()