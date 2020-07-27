#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/27 15:33
:Author:  lenjon
"""
import numpy as np


def computeCost(X, y, theta):
    """
    计算代价函数
    :param X: 样本矩阵，行数为样本数量，列数为自变量
    :param y: 结果样本，行数为样本数量
    :param theta: 权重向量，行数为1
    :return: 该theta对应的代价
    """
    theta = theta.reshape(1, -1)
    m = X.shape[0]  # 样本数量m
    J = 0
    pass
    # inner = np.power((X @ theta.T - y), 2)
    # J = np.sum(inner) / (2 * m)

    return J
