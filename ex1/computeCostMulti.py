#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/27 20:19
:Author:  lenjon
"""
import numpy as np


def computeCostMulti(X, y, theta):
    """
    同computeCost
    """
    theta = theta.reshape(1, -1)
    m = X.shape[0]
    J = 0
    pass
    # inner = np.power((X @ theta.T - y), 2)
    # J = np.sum(inner) / (2 * m)

    return J
