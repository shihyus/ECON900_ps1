import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn import metrics
import numpy as np

dataset = pd.read_csv("parsed_results/coinmarketcap_dataset.csv")
dataset.replace('None', np.nan, inplace=True)
dataset.fillna("0", inplace = True) 
# print(dataset.tail())

data = dataset.iloc[:,3:10]
#print(data)

df = pd.DataFrame(data)
df['Rank'] = np.arange(len(df))
#print(df)

Diff_hl = data['High']-data['Low']
#print(Diff_hl)
Diff_oc = data['OpenPrice']-data['ClosePrice']
# print(Diff_oc)

plt.scatter(data['Rank'],Diff_oc)
plt.savefig("scatter.png")


