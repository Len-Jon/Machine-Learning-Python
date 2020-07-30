#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Compute the cost and gradient of regularized linear
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
:Time:  2020/7/30 13:04
:Author:  lenjon
"""
import numpy as np


def linearRegCostFunction(X, y, theta, _lambda):
    """

    :param X:
    :param y:
    :param theta:
    :param _lambda:
    :return:
    """
    theta = theta.reshape(1, -1)
    m = X.shape[0]
    J = 0
    grad = np.zeros(theta.shape)
    pass
    h = X @ theta.T
    J = np.sum(np.power(h - y, 2)) / (2 * m)
    J_reg = (_lambda / (2 * m)) * np.sum(np.power(theta[:, 1:theta.shape[1]], 2))
    J += J_reg

    grad = ((h - y).T @ X) / m
    grad_reg = _lambda / m * theta
    grad_reg[0, 0] = 0
    grad += grad_reg
    return J, grad
