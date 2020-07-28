#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
:Time:  2020/7/28 14:41
:Author:  lenjon
"""
import numpy as np

from ex2.costFunction import costFunction
from ex2.sigmoid import sigmoid


def costFunctionReg(theta, X, y, _lambda):
    theta = theta.reshape(1, -1)
    m = X.shape[0]
    J = 0
    grad = np.zeros(theta.shape)
    pass
    # J, grad = costFunction(theta, X, y)
    #
    # J_reg = (_lambda / (2 * m)) * np.sum(np.power(theta[:, 1:theta.shape[1]], 2))
    # grad_reg = _lambda / m * theta
    # grad_reg[0, 0] = 0
    #
    # J += J_reg
    # grad += grad_reg
    return J, grad
