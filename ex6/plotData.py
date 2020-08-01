#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/8/1 10:37
:Author:  lenjon
"""

import matplotlib.pyplot as plt
import numpy as np


def plotData(X, y):
    fig, ax = plt.subplots(figsize=(9, 7))
    pos = np.where(y == 1)[0]
    neg = np.where(y == 0)[0]
    ax.scatter(X[pos, 0], X[pos, 1], s=100, c='k', marker='+', edgecolors='k', label='pos')
    ax.scatter(X[neg, 0], X[neg, 1], s=100, c='#ffff00', marker='o', edgecolors='k', label='neg')
    return ax
