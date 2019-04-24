import pandas as pd
import numpy as np
from sklearn import linear_model
import missingno as msno
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn import metrics
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import neighbors




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

########################################################################

# OLS

target_ols = dataset.iloc[:,10].values
#print(target_ols)

data_ols = dataset.iloc[:,3:6]
#print(data_ols.head())

regression = linear_model.LinearRegression()
regression.fit(data_ols,target_ols)

X = [
	[999999999, 100000,20000000],
	[123456, 5000,50000],
	[30, 100,100],
	[1, 0.1, 10],
	[0,0,0],
]
print(X)

results_ols = regression.predict(X)
print("################################")
print("Results_ols", results_ols)
print("################################")

######################################################################

# KNN

data_knn = dataset.iloc[:,3:6]
#print(data_knn.head())

target_knn = dataset.iloc[:,10].values
#print(target_knn)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(data_knn,target_knn)

X = [
	[999999999, 100000,20000000],
	[123456, 5000,50000],
	[30, 100,100],
	[1, 0.1, 10],
	[0,0,0],
]
print(X)

results_knn = knn.predict(X)
print("################################")
print("Results_knn", results_knn)
print("################################")

####################################################################

# Train test split

data_cs = dataset.iloc[:,3:4]
#print(data_cs.head())

target_cs = dataset.iloc[:,10].values
#print(target_cs)

data_training, data_test, target_training, target_test = train_test_split(data_cs, target_cs, test_size = 0.25, random_state=0)

# print(data_training.head())
# print(data_test.head())
# print(target_training)
# print(target_test)

# print(data.shape)
# print(target.shape)
# print(data_training.shape)
# print(data_test.shape)
# print(target_training.shape)
# print(target_test.shape)

linear_machine = linear_model.LinearRegression()
linear_machine.fit(data_training,target_training)
predict = linear_machine.predict(data_test)
#print(predict)

plt.scatter(target_test,predict)
plt.xlabel('target test')
plt.ylabel('prediction')

plt.savefig("scatter_test_prediction.png")
print("Score = ", metrics.r2_score(target_test,predict))
print("################################")
#####################################################################################

# Kfold

data_cs = data_cs.values
#print(data)

kfold_machine = KFold(n_splits=10)
kfold_machine.get_n_splits(data_cs)
#print(kfold_machine)

for training_index, test_index in kfold_machine.split(data_cs):
	#print("Training:", training_index)
	#print("Test:", test_index)
	data_training, data_test = data_cs[training_index], data_cs[test_index]
	target_training, target_test = target_cs[training_index], target_cs[test_index]
	linear_machine = linear_model.LinearRegression()
	linear_machine.fit(data_training, target_training)
	predict = linear_machine.predict(data_test)
	print("Score = ",metrics.r2_score(target_test, predict))

