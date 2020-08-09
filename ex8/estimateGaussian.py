#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Compute the mean of the data and the variances
%               In particular, mu(i) should contain the mean of
%               the data for the i-th feature and sigma2(i)
%               should contain variance of the i-th feature.
%
:Time:  2020/8/9 17:21
:Author:  lenjon
"""
import numpy as np


def estimateGaussian(X):
    m, n = X.shape
    mu = np.zeros((n, 1))
    sigma2 = np.zeros((n, 1))
    pass
    # mu = X.mean(axis=0)
    # sigma2 = X.var(axis=0)
    return mu, sigma2