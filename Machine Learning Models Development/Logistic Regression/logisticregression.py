# -*- coding: utf-8 -*-
"""LogisticRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g147Q1CC7N6_zgj3dj0eng2DR_YI4oSM

**Import**
```

```
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

"""**Data Collection and** **Processing** """

#loading the csv data to a Pandas DataFrame
effects_data=pd.read_csv('/content/dataSet.csv',encoding='cp1252')

"""**Display Data**"""

effects_data

#print first five rows of the dataset
effects_data.head()

#print last 5 data of the dataset
effects_data.tail()



#Display some info about data
effects_data.info()

# check for the null values
effects_data.isnull().sum()

#number of rows and columns of the dataset
effects_data.shape

#statistical measures about the data
effects_data.describe()

"""**Data Preprocessing**

Replace variable values into Numerical form & display the value counts
"""

#Male - 1 Female -0
effects_data.Sex=effects_data.Sex.map({'Male':1,'Female':0})
effects_data['Sex'].value_counts()

#Living area DownTown -1 Outskirt -0

effects_data.Living_Area=effects_data.Living_Area.map({'Downtown':1,'Outskirt':0})
effects_data['Living_Area'].value_counts()

#Vaccine Type
#Pfizer':0 'Moderna':1 'Sinopharm':2 'Astrazeneca':3

effects_data.vaccine_type=effects_data.vaccine_type.map({'Pfizer':0,'Moderna':1,'Sinopharm':2,'Astrazeneca':3})
effects_data['vaccine_type'].value_counts()

#Blood Group

#A+ :0 A- :1  AB+ :2   AB- :3  B+ :4  B- :5  O+ :6  O- :7

effects_data.blood_group=effects_data.blood_group .map({'A+':0,'A-':1,'AB+':2,'AB-':3,'B+':4,'B-':5,'O+':6,'O-':7})
effects_data['blood_group'].value_counts()

# get the side effects and store them in an array
sideEffects=effects_data.columns[7:23].tolist()
print(sideEffects)
print('size = ' ,len(sideEffects))

# a loop to fromat side effets
for index in range(0,len(sideEffects)):
  name=sideEffects[index]
  effects_data[name]=effects_data[name].map({'Yes':1,'No':0})
  effects_data[name].value_counts()

# a loop to view formated side effects
for index in range(0,len(sideEffects)):
  print(effects_data[sideEffects[index]].value_counts())
  print('\n')

"""**Splitting features and targets**"""

#Features

X=effects_data.iloc[:,0:7]

X

# function to get predictions on side effects
# One side effect per time

def get_predictions(Y,X,input):

  X=X.values

  # split the dataset 80% train data , 20% test data
  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
  #print(X.shape,X_train.shape,X_test.shape)

  # Get the model
  model=LogisticRegression()
  # train the svm model with train data
  model.fit(X_train,Y_train)

  # get the predtions for the user inputs
  output=model.predict(input)
  return output


# a function to get model accuracy on a particular side effect
def get_model_accuracy(Y):

  # split the dataset 80% train data , 20% test data
  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

  # Get the model
  model=LogisticRegression()
  # train the svm model with train data
  model.fit(X_train,Y_train)
  

  #Accuracy on Test data
  Y_test_prediction=model.predict(X_test)
  test_data_accuracy=accuracy_score(Y_test_prediction,Y_test)
  print('Accuracy on test data: ',test_data_accuracy)


  #Accuracy of the trainning dataset
  X_train_prediction=model.predict(X_train)
  training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

  print('Accuracy on trainning data: ',training_data_accuracy)




# model accuracy using confusing mtarix
def accuracy_confusion_matrix(Y):

  # split the dataset 80% train data , 20% test data
  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

  # Get the model
  model=LogisticRegression()
  # train the svm model with train data
  model.fit(X_train,Y_train)
  

  #Accuracy on Test data
  Y_test_prediction=model.predict(X_test)
  test_data_accuracy=confusion_matrix(Y_test_prediction,Y_test)
  print(test_data_accuracy)

# example on user inputs
input=[[1,51,1,1.71,82,2,0]]


# an array to store possible side effects
possible_side_effects=[]


index=0
for count in range(7,23):
  if(sideEffects[index]!='Itching'):  # to avoid column 'Itching'
    Y=effects_data.iloc[:,count]
    output=get_predictions(Y,X,input)
    if(output==0):
      result='No'
    else:
      result='Yes'
      possible_side_effects.append(sideEffects[index])

    #print(sideEffects[index]+' = ',result)
  index=index+1

print('Possible Sideeffects =',possible_side_effects)

# accurcy on all side effects (using accuracy scores)
index=0
for count in range(7,23):
  if(sideEffects[index]!='Itching'):  # to avoid column 'Itching'
    Y=effects_data.iloc[:,count]
    print('Accuracy on '+sideEffects[index])
    get_model_accuracy(Y)
    print('\n')

  index=index+1