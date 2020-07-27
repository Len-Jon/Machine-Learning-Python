#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/27 19:40
:Author:  lenjon
"""
import numpy as np


def normalEqn(X, y):
    """
    正规方程求解
    :param X:
    :param y:
    :return: 最优解,注意返回的是列向量,我也不知道MATLAB的源码为啥要这样搞
    """
    theta = np.zeros((X.shape[1], 1))
    pass
    # theta = np.linalg.inv(X.T @ X) @ X.T @ y
    return theta
