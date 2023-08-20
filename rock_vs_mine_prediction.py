# -*- coding: utf-8 -*-
"""Rock vs mine prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MRmpSk4X1_s0M2noGjte6yLZM6qx25DE

Importing Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Data Processing"""

#loading to pandas dataframe
sonar_data = pd.read_csv('/content/Copy of sonar data.csv', header=None)

sonar_data.head()

sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()

#separating the data and labels
X=sonar_data.drop(columns=60, axis=1)
Y=sonar_data[60]

print(X)

print(Y)

"""Train and Test Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training --> Logistic Regression"""

model = LogisticRegression()

print(X_train)
print(Y_train)

#Training the Model with training data
model.fit(X_train, Y_train)

"""Model Evaluation"""

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('The accuracy on training data is: ', training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('The accuracy on test data is: ', test_data_accuracy)

"""Making a predective system"""

input_data = (0.0123,0.0309,0.0169,0.0313,0.0358,0.0102,0.0182,0.0579,0.1122,0.0835,0.0548,0.0847,0.2026,0.2557,0.1870,0.2032,0.1463,0.2849,0.5824,0.7728,0.7852,0.8515,0.5312,0.3653,0.5973,0.8275,1.0000,0.8673,0.6301,0.4591,0.3940,0.2576,0.2817,0.2641,0.2757,0.2698,0.3994,0.4576,0.3940,0.2522,0.1782,0.1354,0.0516,0.0337,0.0894,0.0861,0.0872,0.0445,0.0134,0.0217,0.0188,0.0133,0.0265,0.0224,0.0074,0.0118,0.0026,0.0092,0.0009,0.0044)
# changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#Input data to a numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0] == 'R'):
  print("The object is a rock")
else:
  print("The object is a mine")
