#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    这个好像不是作业内容
:Time:  2020/7/28 13:07
:Author:  lenjon
"""

import numpy as np

from ex2.plotData import plotData


def plotDecisionBoundary(theta, X, y):
    """
    绘制边界曲线
    :param X:
    :param y:
    :return: ax
    """
    ax = plotData(X[:, 1:3], y)
    plotting_x = np.linspace(30, 100, 100)
    plotting_y = (-theta[0] - theta[1] * plotting_x) / theta[2]
    ax.plot(plotting_x, plotting_y, 'y', label='Prediction', color='b')

    return ax
