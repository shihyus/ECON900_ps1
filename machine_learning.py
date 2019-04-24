import pandas as pd
import numpy as np
from sklearn import linear_model
import missingno as msno
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv("parsed_results/coinmarketcap_dataset.csv")
#print(dataset.head())
dataset.replace('None', np.nan, inplace=True)
dataset.fillna("0", inplace = True) 
#print(dataset.tail())


df = pd.DataFrame(dataset)
df['Rank'] = np.arange(len(df))
#missingdata = dataset.isnull().sum()
#print(missingdata)
#print(df)

#########################################################################

# OLS

target = dataset.iloc[:,10].values
print(target)

data = dataset.iloc[:,4:6]
print(data.head())

regression = linear_model.LinearRegression()
regression.fit(data,target)

X = [
	[100000,20000000],
	[5000,50000],
	[100,100],
]
print(X)

results = regression.predict(X)
print(results)


###########################################################

# KNN

data = dataset.iloc[:,4:6]
print(data.head())

target = dataset.iloc[:,3].values
print(target)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(data,target)

X = [
	[100000,20000000],
	[5000,50000],
	[100,100],
]
print(X)

results = knn.predict(X)
print(results)
