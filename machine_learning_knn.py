import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv("parsed_results/coinmarketcap_dataset.csv", header = None)
#print(dataset.head())

data = dataset.iloc[:,4:10]
#print(data.head())

target = dataset.iloc[:,3].values
#print(target)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(data,target)

X = [
	[5.9, 1.0, 5.1, 1.8],
	[3.4, 2.0, 1.1, 4.8],
	[6.0, 3.0, 2.4, 2.0],
	[6.8, 0.0, 1.7, 8.5],
]

print(X)

results = knn.predict(X)

print(results)
