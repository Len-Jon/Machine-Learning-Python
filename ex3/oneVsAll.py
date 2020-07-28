#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: You should complete the following code to train num_labels
%               logistic regression classifiers with regularization
%               parameter lambda.
:Time:  2020/7/28 21:14
:Author:  lenjon
"""
import numpy as np
from scipy.optimize import minimize

# 函数分离
from ex3.lrCostFunction import lrCostFunction


def cost(theta, X, y, _lambda):
    re, _ = lrCostFunction(theta, X, y, _lambda)
    return re


def gradient(theta, X, y, _lambda):
    _, re = lrCostFunction(theta, X, y, _lambda)
    return re


def oneVsAll(X, y, num_labels, _lambda):
    m = X.shape[0]
    n = X.shape[1]
    all_theta = np.zeros((num_labels, n))
    pass
    for i in range(1, num_labels + 1):  # 遍历每个种类
        theta = np.zeros(n).reshape(1, -1)  # 初始化theta
        y_i = np.array([1 if label == i else 0 for label in y]).reshape(m, 1)

        # 求最合适theta
        fmin = minimize(fun=cost, x0=theta, args=(X, y_i, _lambda), method='TNC', jac=gradient)
        all_theta[i - 1, :] = fmin.x
    return all_theta
