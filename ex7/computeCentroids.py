#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Go over every centroid and compute mean of all points that
%               belong to it. Concretely, the row vector centroids(i, :)
%               should contain the mean of the data points assigned to
%               centroid i.
:Time:  2020/8/5 9:29
:Author:  lenjon
"""

import numpy as np


def computeCentroids(X, idx, K):
    m, n = X.shape
    centroids = np.zeros((K, n))
    pass
    # for i in range(K):
    #     indices = np.where(idx == i)[0]
    #     centroids[i, :] = (np.sum(X[indices, :], axis=0) / indices.shape[0]).ravel()  # 各维度与聚类中心的平均距离
    return centroids
