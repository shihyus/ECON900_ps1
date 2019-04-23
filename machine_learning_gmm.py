import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn import metrics
import numpy as np

dataset = pd.read_csv("parsed_results/coinmarketcap_dataset.csv",header=1)
dataset.replace('None', np.nan, inplace=True)
dataset.fillna("0", inplace = True) 
#print(dataset.head())

data = dataset.iloc[:,3:10]
print(data.head())

plt.scatter(data[0],data[1])
# plt.sacefig("scatter.png")