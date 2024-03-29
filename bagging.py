# -*- coding: utf-8 -*-
"""Bagging.ipynb
"""

#Importing the libraries

from sklearn import model_selection 
from sklearn.ensemble import BaggingClassifier 
from sklearn.tree import DecisionTreeClassifier 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import os
import psutil

dataset = pd.read_csv('pima-indians-diabetes.csv')

accuracy_score = []
precision_scores = []
recall_scores = []
f_score_scores = [] 
ram_usage = []
cpu_usage = []

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

dataset.columns = ['PN', 'PGC', 'BP', 'SFT', 'SI', 'BMI' , 'DPF', 'Age', 'Class'] 

dataset.head()

dataset.isna().sum()
dataset.describe()

X.shape

y.shape

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
seed = 8
kfold = model_selection.KFold(n_splits = 3,random_state = None)
base_cls = DecisionTreeClassifier() 
num_trees = 10
model = BaggingClassifier(base_estimator = base_cls, n_estimators = num_trees, random_state = seed) 
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Model Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)
accuracy_score.append(metrics.accuracy_score(y_test, y_pred)*100)
from sklearn import metrics
# Print a classification report
#print(metrics.classification_report(y_test,y_pred))
print("Precision Score:",precision_score(y_test,y_pred))
precision_scores.append(precision_score(y_test,y_pred))
print("Recall Score:",recall_score(y_test,y_pred))
recall_scores.append(precision_score(y_test,y_pred))
print("f1-Score:",f1_score(y_test,y_pred))
f_score_scores.append(f1_score(y_test,y_pred))



probs = model.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)


plt.title('Bagging-DecisionTree')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

import psutil

cpu_usg = psutil.cpu_percent()
cpu_usage.append(cpu_usg)
print('CPU % used:',cpu_usg)

ram_usg = psutil.virtual_memory()[2]
ram_usage.append(ram_usg)
print('RAM memory % used:', ram_usg)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
seed = 8
kfold = model_selection.KFold(n_splits = 3,random_state = None)
base_cls = DecisionTreeClassifier() 
num_trees = 20
model = BaggingClassifier(base_estimator = base_cls, n_estimators = num_trees, random_state = seed) 
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Model Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)
accuracy_score.append(metrics.accuracy_score(y_test, y_pred)*100)
from sklearn import metrics
# Print a classification report
#print(metrics.classification_report(y_test,y_pred))
print("Precision Score:",precision_score(y_test,y_pred))
precision_scores.append(precision_score(y_test,y_pred))
print("Recall Score:",recall_score(y_test,y_pred))
recall_scores.append(precision_score(y_test,y_pred))
print("f1-Score:",f1_score(y_test,y_pred))
f_score_scores.append(f1_score(y_test,y_pred))



probs = model.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)


plt.title('Bagging-DecisionTree')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

import psutil

cpu_usg = psutil.cpu_percent()
cpu_usage.append(cpu_usg)
print('CPU % used:',cpu_usg)

ram_usg = psutil.virtual_memory()[2]
ram_usage.append(ram_usg)
print('RAM memory % used:', ram_usg)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
seed = 8
kfold = model_selection.KFold(n_splits = 3,random_state = None)
base_cls = DecisionTreeClassifier() 
num_trees = 50
model = BaggingClassifier(base_estimator = base_cls, n_estimators = num_trees, random_state = seed) 
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Model Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)
accuracy_score.append(metrics.accuracy_score(y_test, y_pred)*100)
from sklearn import metrics
# Print a classification report
#print(metrics.classification_report(y_test,y_pred))
print("Precision Score:",precision_score(y_test,y_pred))
precision_scores.append(precision_score(y_test,y_pred))
print("Recall Score:",recall_score(y_test,y_pred))
recall_scores.append(precision_score(y_test,y_pred))
print("f1-Score:",f1_score(y_test,y_pred))
f_score_scores.append(f1_score(y_test,y_pred))



probs = model.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)


plt.title('Bagging-DecisionTree')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

import psutil

cpu_usg = psutil.cpu_percent()
cpu_usage.append(cpu_usg)
print('CPU % used:',cpu_usg)

ram_usg = psutil.virtual_memory()[2]
ram_usage.append(ram_usg)
print('RAM memory % used:', ram_usg)

from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification
#X, y = make_classification(n_samples=100, n_features=4,n_informative=2, n_redundant=0,random_state=0, shuffle=False)
model = BaggingClassifier(base_estimator=SVC(),n_estimators=10, random_state=0).fit(X, y)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Model Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)
accuracy_score.append(metrics.accuracy_score(y_test, y_pred)*100)
print("Precision Score:",precision_score(y_test,y_pred))
precision_scores.append(precision_score(y_test,y_pred))
print("Recall Score:",recall_score(y_test,y_pred))
recall_scores.append(precision_score(y_test,y_pred))
print("f1-Score:",f1_score(y_test,y_pred))
f_score_scores.append(f1_score(y_test,y_pred))



probs = model.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)


plt.title('Bagging-SVC')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()


import psutil

cpu_usg = psutil.cpu_percent()
cpu_usage.append(cpu_usg)
print('CPU % used:',cpu_usg)

ram_usg = psutil.virtual_memory()[2]
ram_usage.append(ram_usg)
print('RAM memory % used:', ram_usg)

from sklearn.neighbors import KNeighborsClassifier
#X, y = make_classification(n_samples=100, n_features=4,n_informative=2, n_redundant=0,random_state=0, shuffle=False)
model = BaggingClassifier(base_estimator=KNeighborsClassifier(n_neighbors=7),n_estimators=10, random_state=0).fit(X, y)
#model = BaggingClassifier(base_estimator=KNeighborsClassifier(n_neighbors=7),n_estimators=10, random_state=0).fit(X, y)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Model Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)
accuracy_score.append(metrics.accuracy_score(y_test, y_pred)*100)
print("Precision Score:",precision_score(y_test,y_pred))
precision_scores.append(precision_score(y_test,y_pred))
print("Recall Score:",recall_score(y_test,y_pred))
recall_scores.append(precision_score(y_test,y_pred))
print("f1-Score:",f1_score(y_test,y_pred))
f_score_scores.append(f1_score(y_test,y_pred))



probs = model.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)


plt.title('Bagging-KNN')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()


cpu_usg = psutil.cpu_percent()
cpu_usage.append(cpu_usg)
print('CPU % used:',cpu_usg)

ram_usg = psutil.virtual_memory()[2]
ram_usage.append(ram_usg)
print('RAM memory % used:', ram_usg)

from sklearn.naive_bayes import GaussianNB
#X, y = make_classification(n_samples=100, n_features=4,n_informative=2, n_redundant=0,random_state=0, shuffle=False)
model = BaggingClassifier(base_estimator=GaussianNB(),n_estimators=10, random_state=0).fit(X, y)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Model Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)
accuracy_score.append(metrics.accuracy_score(y_test, y_pred)*100)
print("Precision Score:",precision_score(y_test,y_pred))
precision_scores.append(precision_score(y_test,y_pred))
print("Recall Score:",recall_score(y_test,y_pred))
recall_scores.append(precision_score(y_test,y_pred))
print("f1-Score:",f1_score(y_test,y_pred))
f_score_scores.append(f1_score(y_test,y_pred))



probs = model.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)


plt.title('Bagging-NaiveBayes')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()


cpu_usg = psutil.cpu_percent()
cpu_usage.append(cpu_usg)
print('CPU % used:',cpu_usg)

ram_usg = psutil.virtual_memory()[2]
ram_usage.append(ram_usg)
print('RAM memory % used:', ram_usg)

import seaborn as sns
models = [
          'Decision Tree(10)',
          'Decision Tree(20)',
          'Decision Tree(50)',
          'SVC',
          'KNN',
          'Naive Bayes']
models = pd.DataFrame({'Model' : models, 'Accuracy' : accuracy_score})
plt.figure(figsize = (6,8))
plt.title("Bagging Accuracy")
sns.barplot(x = 'Model', y = 'Accuracy', data = models)
plt.show()

models = [
          'Decision Tree(10)',
          'Decision Tree(20)',
          'Decision Tree(50)',
          'SVC',
          'KNN',
          'Naive Bayes']
models = pd.DataFrame({'Model' : models, 'precision' : precision_scores})
plt.figure(figsize = (6,8))
plt.title("Bagging Precision")
sns.barplot(x = 'Model', y = 'precision', data = models)
plt.show()

models = [
          'Decision Tree(10)',
          'Decision Tree(20)',
          'Decision Tree(50)',
          'SVC',
          'KNN',
          'Naive Bayes']
models = pd.DataFrame({'Model' : models, 'recall' : recall_scores})
plt.figure(figsize = (6,8))
plt.title("Bagging Recall")
sns.barplot(x = 'Model', y = 'recall', data = models)
plt.show()

models = [
          'Decision Tree(10)',
          'Decision Tree(20)',
          'Decision Tree(50)',
          'SVC',
          'KNN',
          'Naive Bayes']
models = pd.DataFrame({'Model' : models, 'f_score' : f_score_scores})
plt.figure(figsize = (6,8))
plt.title("Bagging F score")
sns.barplot(x = 'Model', y = 'f_score', data = models)
plt.show()

print("ram usage:",ram_usage)
print("cpu usage:",cpu_usage)
print("accuracy scores:",accuracy_score)
print("precision scores:",precision_scores)
print("recall scores:",recall_scores)
print("f scores:",f_score_scores)

models = [
          'Decision Tree(10)',
          'Decision Tree(20)',
          'Decision Tree(50)',
          'SVC',
          'KNN',
          'Naive Bayes']
models = pd.DataFrame({'Model' : models, 'cpu usage' : cpu_usage})
plt.figure(figsize = (6,8))
plt.title("Bagging Cpu usage")
sns.barplot(x = 'Model', y = 'cpu usage', data = models)
plt.show()

models = [
          'Decision Tree(10)',
          'Decision Tree(20)',
          'Decision Tree(50)',
          'SVC',
          'KNN',
          'Naive Bayes']
models = pd.DataFrame({'Model' : models, 'ram usage' : ram_usage})
plt.figure(figsize = (6,8))
plt.title("Bagging ram usage")
sns.barplot(x = 'Model', y = 'ram usage', data = models)
plt.show()
