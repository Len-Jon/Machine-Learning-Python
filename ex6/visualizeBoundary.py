#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/8/1 15:45
:Author:  lenjon
"""
import numpy as np

from ex6.plotData import plotData


def visualizeBoundary(X, y, model):
    xmin, xmax, ymin, ymax = min(X[:, 0]), max(X[:, 0]), min(X[:, 1]), max(X[:, 1])
    ax = plotData(X, y)
    x = np.linspace(xmin - 0.1 * abs(xmin), xmax + 0.1 * abs(xmax), 500)
    y = np.linspace(ymin - 0.1 * abs(ymin), ymax + 0.1 * abs(ymax), 500)
    xx, yy = np.meshgrid(x, y)
    z = model.predict(np.c_[xx.ravel(), yy.ravel()])  # column方向并列链接，同理有个r_
    zz = z.reshape(xx.shape)
    ax.contour(xx, yy, zz)
