#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel

% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example,
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
:Time:  2020/8/1 18:35
:Author:  lenjon
"""
import numpy as np
from sklearn import svm


def dataset3Params(X, y, Xval, yval):
    C = 1
    sigma = 0.3
    C_values = (0.01, 0.03, 0.1, 0.3, 1., 3., 10., 30.)
    gamma = np.power(C_values, -2) / 2  # 从这里面选
    gamma = tuple(map(lambda x: (x ** -2) / 2, [x for x in C_values]))
    pass
    best_score = 0
    for c in C_values:
        for g in gamma:
            model = svm.SVC(C=c, kernel='rbf', gamma=g)
            model.fit(X, y.flatten())
            this_score = model.score(Xval, yval)
            if this_score > best_score:
                best_score = this_score
                C = c
                sigma = C_values[gamma.index(g)]
    return C, sigma
