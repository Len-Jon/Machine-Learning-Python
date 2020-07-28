#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Complete the following code to make predictions using
%               your learned logistic regression parameters (one-vs-all).
%               You should set p to a vector of predictions (from 1 to
%               num_labels).
:Time:  2020/7/28 21:32
:Author:  lenjon
"""
import numpy as np

from ex3.sigmoid import sigmoid


def predictOneVsAll(all_theta, X):
    m = X.shape[0]
    num_labels = all_theta.shape[0]
    p = np.zeros((m, 1))
    pass
    # h = sigmoid(X @ all_theta.T)
    # p = (np.argmax(h, axis=1) + 1).reshape(-1, 1)
    return p
