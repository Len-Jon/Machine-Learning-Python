#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/8/5 11:52
:Author:  lenjon
"""
from ex7.computeCentroids import computeCentroids
from ex7.findClosestCentroids import findClosestCentroids
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as display

from ex7.plotProgresskMeans import plotProgresskMeans


def runkMeans(X, initial_centroids, max_iters, plot_progress=False):
    m, n = X.shape
    K = initial_centroids.shape[0]
    centroids = initial_centroids
    previous_centroids = [centroids]
    idx = np.zeros((m, 1))

    for i in range(max_iters):
        print('K-Means iteration %d/%d...' % (i + 1, max_iters))
        idx = findClosestCentroids(X, centroids)  # 聚类
        if plot_progress:
            plt.figure(figsize=(10, 6))
            plotProgresskMeans(X, centroids, previous_centroids, idx, K, i, plt)
            previous_centroids.append(centroids)
            plt.title('Iteration number {}'.format(i))
            plt.show()
            if i != max_iters - 1:
                print('Press enter to continue.')
                input()
                display.clear_output(True)
        centroids = computeCentroids(X, idx, K)  # 更新聚类中心
    return centroids, idx
