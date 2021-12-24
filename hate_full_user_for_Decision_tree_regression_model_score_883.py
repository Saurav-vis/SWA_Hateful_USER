# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 23:36:28 2021

@author: Saurav Pandey
"""

import numpy as np
import pandas as pd

#load dataset
dataset = pd.read_csv(r'users_neighborhood_anon.csv')

#dropping columns that are not useful
dataset = dataset.drop(columns=('hate_neigh'))
dataset = dataset.drop(columns=('normal_neigh'))
dataset = dataset.drop(columns=('is_50'))
dataset = dataset.drop(columns=('hashtags'))
dataset = dataset.drop(columns=('is_63'))
dataset = dataset.drop(columns=('is_50_2'))
dataset = dataset.drop(columns=('is_63_2'))

dataset = dataset.dropna()

#is_63','is_50_2','is_63_2'
x = dataset.iloc[0:5000,2:].values
y = dataset.iloc[0:5000,1].values


#standarize the data due to string value
from sklearn.preprocessing import LabelEncoder
label_encode = LabelEncoder()
#x = label_encode.fit_transform(x)
y = label_encode.fit_transform(y)

#training and testing data (divide the dataset into two part)
from sklearn.model_selection import train_test_split
X_train_old,X_test_old,Y_train,Y_test = train_test_split(x,y,test_size=0.2,random_state=0)


#reduce dimention
from sklearn.decomposition import PCA
pca = PCA(n_components=25)

#training model
X_train = pca.fit_transform(X_train_old)
X_test = pca.transform(X_test_old)



#impliment regression model
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor()
reg.fit(X_train,Y_train)
Y_predict = reg.predict(X_test)

Y_predict_new = []

for i in Y_predict:
    Y_predict_new.append(int(i))

#Find accurracy score
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(Y_test,Y_predict_new)
