#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/8/9 18:05
:Author:  lenjon
"""
import numpy as np


def multivariateGaussian(X, mu, sigma2):
    # 特征的个数
    k = mu.size

    if sigma2.ndim == 1 or (sigma2.ndim == 2 and (sigma2.shape[1] == 1 or sigma2.shape[0] == 1)):
        sigma2 = np.diag(sigma2)

    x = X - mu
    p = (2 * np.pi) ** (-k / 2) * np.linalg.det(sigma2) ** (-0.5) * np.exp(
        -0.5 * np.sum(np.dot(x, np.linalg.pinv(sigma2)) * x, axis=1))

    return p
