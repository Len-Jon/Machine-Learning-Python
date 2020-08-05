#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Compute the projection of the data using only the top K
%               eigenvectors in U (first K columns).
%               For the i-th example X(i,:), the projection on to the k-th
%               eigenvector is given as follows:
%                    x = X(i, :)';
%                    projection_k = x' * U(:, k);
:Time:  2020/8/5 21:55
:Author:  lenjon
"""
import numpy as np


def projectData(X, U, K):
    # 找K个最能代表原数据的向量
    Z = np.zeros((X.shape[0], K))
    pass
    # U_reduce = U[:, :K]
    # Z = X @ U_reduce
    return Z
