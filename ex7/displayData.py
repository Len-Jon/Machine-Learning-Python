#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/8/5 22:45
:Author:  lenjon
"""
import math

import numpy as np
import matplotlib.pyplot as plt


def displayData(X, single=False):
    all_a = int(math.sqrt(X.shape[0]))  # 总边长
    length = int(math.sqrt(X.shape[1]))  # 单个图片边长
    if single:
        fig, ax = plt.subplots(figsize=(1, 1))
        ax.matshow(X.reshape((20, 20)).T, cmap='gray')
        plt.xticks([])
        plt.yticks([])
        return
    fig, ax_array = plt.subplots(nrows=all_a, ncols=all_a, sharex='all', sharey='all', figsize=(all_a, all_a))
    for r in range(all_a):
        for c in range(all_a):
            ax_array[r, c].matshow(np.array(X[all_a * r + c].reshape((length, length))).T, cmap='gray')
    plt.xticks([])
    plt.yticks([])
