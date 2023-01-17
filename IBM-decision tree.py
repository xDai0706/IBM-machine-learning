#!/usr/bin/env python
# coding: utf-8

# import piplite
# await piplite.install(['pandas'])
# await piplite.install(['matplotlib'])
# await piplite.install(['numpy'])
# await piplite.install(['scikit-learn'])
# 
# import numpy as np 
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# import sklearn.tree as tree
# 
# from pyodide.http import pyfetch
# 
# async def download(url, filename):
#     response = await pyfetch(url)
#     if response.status == 200:
#         with open(filename, "wb") as f:
#             f.write(await response.bytes())
#   
# path= 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv'
# await download(path,"drug200.csv")
# path="drug200.csv"
# 
# my_data = pd.read_csv("drug200.csv", delimiter=",")
# my_data[0:5]
# 
# my_data.shape #size of data
# 
# 
# X = my_data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
# X[0:5]
# 
# 
# #As you may figure out, some features in this dataset are categorical, such as Sex or BP. Unfortunately, Sklearn Decision Trees does not handle categorical variables. We can still convert these features to numerical values using pandas.get_dummies() to convert the categorical variable into dummy/indicator variables
# 
# from sklearn import preprocessing
# le_sex = preprocessing.LabelEncoder()
# le_sex.fit(['F','M'])
# X[:,1] = le_sex.transform(X[:,1]) 
# 
# 
# le_BP = preprocessing.LabelEncoder()
# le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
# X[:,2] = le_BP.transform(X[:,2])
# 
# 
# le_Chol = preprocessing.LabelEncoder()
# le_Chol.fit([ 'NORMAL', 'HIGH'])
# X[:,3] = le_Chol.transform(X[:,3]) 
# 
# X[0:5]
# 
# y = my_data["Drug"]
# y[0:5]

# In[ ]:




#Setting up the Decision Tree
from sklearn.model_selection import train_test_split
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)
drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
drugTree # it shows the default parameters

drugTree.fit(X_trainset,y_trainset)

#Prediction
predTree = drugTree.predict(X_testset)

from sklearn import metrics
import matplotlib.pyplot as plt
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))

tree.plot_tree(drugTree)
plt.show()

