#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/8/5 12:07
:Author:  lenjon
"""

import numpy as np


def plotDataPoints(X, idx, K, plt):
    for i in range(K):
        x = X[np.where(idx == i)[0], :]
        plt.scatter(x=x[:, 0], y=x[:, 1], edgecolors='k')
