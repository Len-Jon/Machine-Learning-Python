#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Fill in this function to return training errors in
%               error_train and the validation errors in error_val. The
%               vector lambda_vec contains the different lambda parameters
%               to use for each calculation of the errors, i.e,
%               error_train(i), and error_val(i) should give
%               you the errors obtained after training with
%               lambda = lambda_vec(i)
:Time:  2020/7/30 17:56
:Author:  lenjon
"""

import numpy as np

from ex5.linearRegCostFunction import linearRegCostFunction
from ex5.trainLinearReg import trainLinearReg


def validationCurve(X, y, Xval, yval):
    # Selected values of lambda (you should not change this)
    lambda_vec = [0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10]
    error_train = np.zeros((len(lambda_vec)))
    error_val = np.zeros((len(lambda_vec)))
    pass
    # for i in range(len(lambda_vec)):
    #     _lambda = lambda_vec[i]
    #     result = trainLinearReg(X, y, _lambda)
    #     theta = result.x
    #     error_train[i], _ = linearRegCostFunction(X, y, theta, 0)
    #     error_val[i], _ = linearRegCostFunction(Xval, yval, theta, 0)
    return lambda_vec, error_train, error_val
