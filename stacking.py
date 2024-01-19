# -*- coding: utf-8 -*-
"""Stacking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1njfdMbuwH2nBmsqxOtWcsMnMuyqGc9nL
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

sns.set()
# %matplotlib inline

data = pd.read_csv('pima-indians-diabetes.csv')

data.head()

data.describe()

plt.figure(figsize = (20, 25))
plotnumber = 1

for column in data:
    if plotnumber <= 9:
        ax = plt.subplot(3, 3, plotnumber)
        sns.distplot(data[column])
        plt.xlabel(column, fontsize = 15)
        
    plotnumber += 1
plt.show()

data.columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI' , 'DiabetesPedigreeFunction', 'Age', 'Class'] 

data.head()

data['BMI'] = data['BMI'].replace(0, data['BMI'].mean())
data['BloodPressure'] = data['BloodPressure'].replace(0, data['BloodPressure'].mean())
data['Glucose'] = data['Glucose'].replace(0, data['Glucose'].mean())
data['Insulin'] = data['Insulin'].replace(0, data['Insulin'].mean())
data['SkinThickness'] = data['SkinThickness'].replace(0, data['SkinThickness'].mean())

plt.figure(figsize = (20, 25))
plotnumber = 1

for column in data:
    if plotnumber <= 9:
        ax = plt.subplot(3, 3, plotnumber)
        sns.distplot(data[column])
        plt.xlabel(column, fontsize = 15)
        
    plotnumber += 1
plt.show()

fig, ax = plt.subplots(figsize = (15, 10))
sns.boxplot(data = data, width = 0.5, ax = ax, fliersize = 3)
plt.show()

outlier = data['Pregnancies'].quantile(0.98)
# removing the top 2% data from the pregnancies column
data = data[data['Pregnancies']<outlier]

outlier = data['BMI'].quantile(0.99)
# removing the top 1% data from BMI column
data = data[data['BMI']<outlier]

outlier = data['SkinThickness'].quantile(0.99)
# removing the top 1% data from SkinThickness column
data = data[data['SkinThickness']<outlier]

outlier = data['Insulin'].quantile(0.95)
# removing the top 5% data from Insulin column
data = data[data['Insulin']<outlier]

outlier = data['DiabetesPedigreeFunction'].quantile(0.99)
# removing the top 1% data from DiabetesPedigreeFunction column
data = data[data['DiabetesPedigreeFunction']<outlier]

outlier = data['Age'].quantile(0.99)
# removing the top 1% data from Age column
data = data[data['Age']<outlier]

plt.figure(figsize = (20, 25))
plotnumber = 1

for column in data:
    if plotnumber <= 9:
        ax = plt.subplot(3, 3, plotnumber)
        sns.distplot(data[column])
        plt.xlabel(column, fontsize = 15)
        
    plotnumber += 1
plt.show()

plt.figure(figsize = (16, 8))

corr = data.corr()
mask = np.triu(np.ones_like(corr, dtype = bool))
sns.heatmap(corr, mask = mask, annot = True, fmt = '.2g', linewidths = 1)
plt.show()

X = data.drop(columns = ['Class'])
y = data['Class']

from sklearn.model_selection import train_test_split

train, val_train, test, val_test = train_test_split(X, y, test_size = 0.5, random_state = 355)

X_train, X_test, y_train, y_test = train_test_split(train, test, test_size = 0.2, random_state = 355)

from sklearn.tree import DecisionTreeClassifier
lr = DecisionTreeClassifier(random_state=0)
lr.fit(X_train, y_train)

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)

from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train, y_train)



from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

accuracy=[]
models=["dec-svm","neigh-gnb","dec-neigh","dec-gnb","svm-neigh","svm-gnb"]
#1-2,3-4,1-3,1-4,2-3,2-4

predict_val1 = lr.predict(val_train)
predict_val2 = svm.predict(val_train)
predict_val3 = neigh.predict(val_train)
predict_val4 = gnb.predict(val_train)

predict_test1 = lr.predict(X_test)
predict_test2 = svm.predict(X_test)
predict_test3 = neigh.predict(X_test)
predict_test4 = gnb.predict(X_test)

predict_val = np.column_stack((predict_val2, predict_val4))

predict_test = np.column_stack((predict_test2, predict_test4))

from sklearn.ensemble import RandomForestClassifier
rand_clf = RandomForestClassifier()
rand_clf.fit(predict_val, val_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
stacking_acc = accuracy_score(y_test, rand_clf.predict(predict_test))
accuracy.append(stacking_acc*100)

print(accuracy)

print(classification_report(y_test, rand_clf.predict(predict_test)))

import seaborn as sns
models=["dec-svm","neigh-gnb","dec-neigh","dec-gnb","svm-neigh","svm-gnb"]
acc=[accuracy[0],accuracy[1],accuracy[2],accuracy[3],accuracy[4],accuracy[5]]
models = pd.DataFrame({'Model Names' : models, 'Accuracy Score' : acc})
#models.sort_values(by = 'Accuracy Score', ascending = False)

plt.figure(figsize = (8, 8))

sns.barplot(x = 'Model Names', y = 'Accuracy Score', data = models)
plt.title("Stacking Accuracy")
plt.show()