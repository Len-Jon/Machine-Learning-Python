#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/8/9 21:39
:Author:  lenjon
"""

import numpy as np


def cofiCostFunc(params, Y, R, num_users, num_movies, num_features, lmd):
    X = params[0:num_movies * num_features].reshape((num_movies, num_features))
    theta = params[num_movies * num_features:].reshape((num_users, num_features))

    cost = 0
    X_grad = np.zeros(X.shape)
    theta_grad = np.zeros(theta.shape)
    pass
    hypothesis = (np.dot(X, theta.T) - Y) * R  # 只计算有打分的

    cost = (1 / 2) * np.sum(hypothesis ** 2) + (lmd / 2) * np.sum(theta ** 2) + (lmd / 2) * np.sum(X ** 2)

    X_grad = hypothesis @ theta + lmd * X
    theta_grad = hypothesis.T @ X + lmd * theta
    pass

    grad = np.concatenate((X_grad.flatten(), theta_grad.flatten()))
    return cost, grad
