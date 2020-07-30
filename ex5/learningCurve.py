#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Fill in this function to return training errors in
%               error_train and the cross validation errors in error_val.
%               i.e., error_train(i) and
%               error_val(i) should give you the errors
%               obtained after training on i examples.
:Time:  2020/7/30 14:29
:Author:  lenjon
"""
import numpy as np

from ex5.linearRegCostFunction import linearRegCostFunction
from ex5.trainLinearReg import trainLinearReg


def learningCurve(X, y, Xval, yval, _lambda):
    m = X.shape[0]
    error_train = np.zeros(m)
    error_val = np.zeros(m)
    pass
    # for i in range(m):
    #     result = trainLinearReg(X[:i + 1, :], y[:i + 1, :], _lambda)
    #     theta = result.x
    #     error_train[i], _ = linearRegCostFunction(X[:i + 1, :], y[:i + 1, :], theta, 0)  # lambda设置为0
    #     error_val[i], _ = linearRegCostFunction(Xval, yval, theta, 0)

    return error_train, error_val
