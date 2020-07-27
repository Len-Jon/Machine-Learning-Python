#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/27 20:00
:Author:  lenjon
"""
from ex1.computeCostMulti import computeCostMulti
import numpy as np


def gradientDescentMulti(X, y, theta, alpha, num_iters):
    """
    同gradientDescent
    """
    theta = theta.reshape(1, -1)
    J_history = np.zeros(num_iters)
    m = X.shape[0]

    for i in range(num_iters):
        pass
        theta -= alpha / m * ((X @ theta.T - y).T @ X)
        J_history[i] = computeCostMulti(X, y, theta)
    return theta, J_history
