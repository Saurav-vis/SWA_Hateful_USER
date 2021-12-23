# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:17:16 2021

@author: Saurav Pandey
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#load dataset
dataset = pd.read_csv(r'users_neighborhood_anon.csv')


#Plotting pie chart
#plot pi-chart
hateful_list = ['hateful','normal','other']
hateful_csv = dataset.iloc[:,1]
hateful_hatefuluser = 0
hateful_normaluser = 0
hateful_otheruser = 0


#lable encode
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
hateful_csv = labelencoder.fit_transform(hateful_csv)

for i in hateful_csv:
    if i==0:
        hateful_hatefuluser = hateful_hatefuluser + 1
    elif i==1:
        hateful_normaluser = hateful_normaluser + 1
    elif i==2:
        hateful_otheruser = hateful_otheruser + 1
    else:
        pass

hateful_number = [hateful_hatefuluser ,hateful_normaluser, hateful_otheruser]


plt.pie(hateful_number, labels = hateful_list)
plt.show()

# Dropping some unwanted columns like is_63','is_50_2','is_63_2'
dataset = dataset.drop(columns=('hate_neigh'))
dataset = dataset.drop(columns=('normal_neigh'))
dataset = dataset.drop(columns=('is_50'))
dataset = dataset.drop(columns=('hashtags'))
dataset = dataset.drop(columns=('is_63'))
dataset = dataset.drop(columns=('is_50_2'))
dataset = dataset.drop(columns=('is_63_2'))

#dropping NAN values in Dataset
dataset = dataset.dropna()


x = dataset.iloc[0:5000,2:].values
y = dataset.iloc[0:5000,1].values


#standarize the data due to string value
from sklearn.preprocessing import LabelEncoder
label_encode = LabelEncoder()
#x = label_encode.fit_transform(x)
y = label_encode.fit_transform(y)

#training and testing data (divide the dataset into two part)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2,random_state=0)


#reduce dimention
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)



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



#rad data by test
test_data_hateful = pd.read_csv(r'Hateful_test.csv')

#delete some column
# test_data_x.drop(['label','text', 'post_id' , 'sentence_range', 'id', 'social_timestamp'], axis=1, inplace=True)
test_data_hateful = test_data_hateful.drop(columns=('hate_neigh'))
test_data_hateful = test_data_hateful.drop(columns=('normal_neigh'))
test_data_hateful = test_data_hateful.drop(columns=('is_50'))
test_data_hateful = test_data_hateful.drop(columns=('hashtags'))
test_data_hateful = test_data_hateful.drop(columns=('is_63'))
test_data_hateful = test_data_hateful.drop(columns=('is_50_2'))
test_data_hateful = test_data_hateful.drop(columns=('is_63_2'))


# test_data_hateful['hate'] = labelencoder.fit_transform(test_data_hateful['hate'])

test_data_hateful = test_data_hateful.dropna()


test_X = test_data_hateful.iloc[:,:].values

pca = PCA(n_components=1)
test_X = pca.fit_transform(test_X)
predict_Y = reg.predict(test_X)


predict_Y_new = []

for i in predict_Y:
    predict_Y_new.append(int(i))


