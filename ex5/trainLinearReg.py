#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/7/30 13:26
:Author:  lenjon
"""
import numpy as np
from scipy.optimize import minimize

from ex5.linearRegCostFunction import linearRegCostFunction


def trainLinearReg(X, y, _lambda):
    initial_theta = np.zeros(X.shape[1])

    def costFunction(theta):
        return linearRegCostFunction(X, y, theta, _lambda)

    result = minimize(fun=costFunction,
                      x0=initial_theta,
                      method='TNC',
                      jac=True,
                      options={'maxiter': 200})
    return result
