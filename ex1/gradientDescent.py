#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/27 17:35
:Author:  lenjon
"""
from ex1.computeCost import computeCost
import numpy as np


def gradientDescent(X, y, theta, alpha, num_iters):
    theta = theta.reshape(1, -1)
    cost = np.zeros(num_iters)  # 记录代价函数的值
    m = X.shape[0]
    for i in range(num_iters):
        theta -= alpha / m * ((X @ theta.T - y).T @ X)  # 矩阵乘法替代求和
        cost[i] = computeCost(X, y, theta)
    return theta, cost
