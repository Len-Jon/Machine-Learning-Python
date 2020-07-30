#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/7/30 16:57
:Author:  lenjon
"""
import numpy as np

from ex5.polyFeatures import polyFeatures


def plotFit(min_x, max_x, mu, sigma, theta, p, ax):
    x = np.arange(min_x - 15, max_x + 25, 0.05).reshape(-1, 1)  # 节省运算时间
    X_poly = polyFeatures(x, p)
    m = X_poly.shape[0]
    X_poly -= np.tile(mu, (m, 1))
    X_poly /= np.tile(sigma, (m, 1))
    X_poly = np.insert(X_poly, 0, np.ones(m), axis=1)
    ax.plot(x, X_poly @ theta, '--')
