import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
import seaborn
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score

#import data
df = pd.read_csv('train.csv')
print("Dataser loaded...")

#preprocessing
print("Preprocessing data...")
df.drop(['PassengerId','Name','Ticket','Fare','Cabin','Embarked'],1,inplace=True)
df.loc[df.Sex == 'male', 'Sex'] = 1  
df.loc[df.Sex == 'female', 'Sex'] = 0
df['Age'].fillna((df['Age'].mean()), inplace=True)
#print(df.isnull().sum())
df = shuffle(df)

#split feture and label
x = df.drop(['Survived'],1,inplace=False)
y = df['Survived']

#create datasets
print("Creating training and testing dataset...")
test_size = 0.2
split_index = int(test_size*len(x))
x_train = x[:-split_index]
y_train = y[:-split_index]
x_test = x[-split_index:]
y_test = y[-split_index:]

#trainting
print("Training Logistic Regression model...")
logreg = LogisticRegression()
logreg.fit(x_train, y_train)

#predict and accuracy
pred_label = logreg.predict(x_test)

print("Calculating accuracy on testing data...")
acc_log = round(logreg.score(x_test, y_test) * 100, 2)
print("Accuracy:",acc_log)

print("Accuracy is %.4f" % accuracy_score(pred_label, y_test))

print("Confusion matrix: ")
mat = confusion_matrix(y_test, pred_label)
print(mat)

print("%.4f" % precision_score(y_test, pred_label))
