#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/7/30 16:17
:Author:  lenjon
"""


def featureNormalize(X):
    """
    求特征缩放
    :param X:
    :return: 每列平均值 标准差
    """
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    X = (X - mu) / sigma
    return X, mu, sigma
