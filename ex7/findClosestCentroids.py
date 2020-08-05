#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Go over every example, find its closest centroid, and store
%               the index inside idx at the appropriate location.
%               Concretely, idx(i) should contain the index of the centroid
%               closest to example i. Hence, it should be a value in the
%               range 1..K
%
% Note: You can use a for-loop over the examples to compute this.
:Time:  2020/8/4 23:49
:Author:  lenjon
"""
import sys

import numpy as np


def findClosestCentroids(X, centroids):
    # Set K
    K = centroids.shape[0]
    # You need to return the following variables correctly.
    idx = np.zeros((X.shape[0], 1), dtype=int)
    pass
    # for i in range(X.shape[0]):
    #     min_dist = sys.maxsize
    #     for j in range(K):
    #         dist = np.sum((X[i, :] - centroids[j, :]) ** 2)
    #         if dist < min_dist:
    #             min_dist = dist
    #             idx[i] = j
    return idx
