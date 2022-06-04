# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 09:49:06 2022

@author: pati_
"""
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("data/data.csv")

values = list(data[list(data.columns[:-1])].values)
targets = list(data['class'].values)


def split_data(data, classes, test_size):
  feat_train, feat_test, target_train, target_test = train_test_split(data, classes, test_size=test_size, shuffle=True)
  return feat_train, feat_test, target_train, target_test


feat_train, feat_test, target_train, target_test = split_data(values, targets, 0.2)

## -------------------------
## Decision Tree Classifier

print('\n--- Decision Tree Classifier ---')

grid_params_dtc = {
    'criterion': ['gini', 'entropy', 'log_loss'], 
    'splitter': ['best', 'random'],
    'max_depth': [5],
    'max_features': ['sqrt', 'log2', None],
    'max_leaf_nodes': [None],
}

# Create the classifier

gs_dtc = GridSearchCV(
    DecisionTreeClassifier(),
    grid_params_dtc,
    verbose = 1,
    n_jobs = 1,
    cv = 5,
    )

gs_results_dtc = gs_dtc.fit(feat_train, target_train)

print(gs_results_dtc.best_score_)
print(gs_results_dtc.best_params_)

## -------------------------
## K-nearest Neighbour

print('\n--- K-nearest Neighbour ---')

grid_params_knn = {
    'n_neighbors': [3,5,11,19], 
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan'],
}

gs_knn = GridSearchCV(
    KNeighborsClassifier(),
    grid_params_knn,
    verbose = 1,
    n_jobs = 1,
    cv = 5,
    )

gs_results_knn = gs_knn.fit(feat_train, target_train)

print(gs_results_knn.best_score_)
print(gs_results_knn.best_params_)

## -------------------------
