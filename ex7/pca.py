#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: You should first compute the covariance matrix. Then, you
%               should use the "svd" function to compute the eigenvectors
%               and eigenvalues of the covariance matrix.
%
% Note: When computing the covariance matrix, remember to divide by m (the
%       number of examples).
:Time:  2020/8/5 20:43
:Author:  lenjon
"""

import numpy as np


def pca(X):
    m, n = X.shape
    U = np.zeros(n)
    S = np.zeros(n)
    pass
    # Sigma = 1 / m * X.T @ X  # 求协方差矩阵
    # U, S, V = np.linalg.svd(Sigma)  # 求协方差矩阵特征值
    return U, S
