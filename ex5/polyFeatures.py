#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Given a vector X, return a matrix X_poly where the p-th
%               column of X contains the values of X to the p-th power.
:Time:  2020/7/30 15:56
:Author:  lenjon
"""

import numpy as np


def polyFeatures(X, p):
    m = X.shape[0]
    X_poly = np.zeros((m, p))
    pass
    for i in range(p):
        X_poly[:, i:i + 1] = np.power(X, i + 1)
    return X_poly
