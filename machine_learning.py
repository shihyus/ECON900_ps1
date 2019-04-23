import pandas as pd
import numpy as np
from sklearn import linear_model
import missingno as msno


dataset = pd.read_csv("parsed_results/coinmarketcap_dataset.csv")
#print(dataset.head())
dataset.replace('None', np.nan, inplace=True)
dataset.fillna("0", inplace = True) 
#print(dataset.tail())

#missingdata = dataset.isnull().sum()
#print(missingdata)

target = dataset.iloc[:,3].values
print(target)

data = dataset.iloc[:,4:10]
print(data.head())

regression = linear_model.LinearRegression()
regression.fit(data,target)

X = [
	[24,55,31,3,0,7],
	[40,50,2,5,1,8],
	[3,95,37,3,1,15],
]

results = regression.predict(X)
print(results)