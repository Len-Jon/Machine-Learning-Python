#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/27 15:33
:Author:  lenjon
"""
import numpy as np


def computeCost(X, y, theta):
    theta = theta.reshape(1, -1)
    inner = np.power((X @ theta.T - y), 2)
    return np.sum(inner) / (2 * X.shape[0])
