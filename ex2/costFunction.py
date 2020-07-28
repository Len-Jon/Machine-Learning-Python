#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
:Time:  2020/7/28 11:05
:Author:  lenjon
"""
import numpy as np

from ex2.sigmoid import sigmoid


def costFunction(theta, X, y):
    # Initialize
    theta = theta.reshape(1, -1)
    m = X.shape[0]
    J = 0
    grad = np.zeros(theta.shape)
    pass
    h = sigmoid(X @ theta.T)
    J = np.sum(-y * np.log(h) - (1 - y) * np.log(1 - h)) / m
    grad = ((h - y).T @ X) / m
    return J, grad
