#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/27 18:50
:Author:  lenjon
"""

import numpy as np


def featureNormalize(X):
    """
    特征缩放
    :param X: 
    :return: 
    """
    X_norm = X
    mu = np.zeros((1, X.shape[1]))
    sigma = np.zeros((1, X.shape[1]))
    pass
    mu = np.mean(X_norm, axis=0)  # 列均值
    sigma = np.std(X_norm, axis=0)  # 列标准差
    X_norm = (X_norm - mu) / sigma
    return X_norm, mu, sigma
