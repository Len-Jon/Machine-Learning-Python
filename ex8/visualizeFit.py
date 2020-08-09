#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/8/9 17:29
:Author:  lenjon
"""
import matplotlib.pyplot as plt
import numpy as np
from ex8.multivariateGaussian import multivariateGaussian


def visualizeFit(X, mu, sigma2):
    grid = np.arange(0, 35.5, 0.5)
    x1, x2 = np.meshgrid(grid, grid)

    Z = multivariateGaussian(np.c_[x1.flatten('F'), x2.flatten('F')], mu, sigma2)
    Z = Z.reshape(x1.shape, order='F')

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], marker='x', c='b', s=15, linewidth=1)

    # Do not plot if there are infinities
    if np.sum(np.isinf(X)) == 0:
        lvls = 10 ** np.arange(-20, 0, 3).astype(np.float)
        plt.contour(x1, x2, Z, levels=lvls, linewidths=0.7)
