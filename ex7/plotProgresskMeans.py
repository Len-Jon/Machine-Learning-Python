#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/8/5 11:59
:Author:  lenjon
"""
from ex7.plotDataPoints import plotDataPoints
import numpy as np


def plotProgresskMeans(X, centroids, previous, idx, K, i, plt):
    plotDataPoints(X, idx, K, plt)
    for i in range(K):
        points = np.array([[x[i, :][0], x[i, :][1]] for x in previous])
        plt.plot(points[:, 0], points[:, 1], marker='x', lw=3, ms=10, mew=3, )  # mec='k'
