#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Complete the following code to make predictions using
%               your learned logistic regression parameters.
%               You should set p to a vector of 0's and 1's
:Time:  2020/7/28 13:40
:Author:  lenjon
"""
import numpy as np

from ex2.sigmoid import sigmoid


def predict(theta, X):
    m = X.shape[0]
    p = np.zeros((m, 1))
    pass
    probability = sigmoid(X @ theta.T)
    p = np.array([1 if x >= 0.5 else 0 for x in probability]).reshape(-1, 1)
    return p
