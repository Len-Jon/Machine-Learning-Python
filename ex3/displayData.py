#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/7/28 20:16
:Author:  lenjon
"""
import matplotlib.pyplot as plt
import numpy as np


def displayData(X):
    fig, ax_array = plt.subplots(nrows=10, ncols=10, sharex='all', sharey='all', figsize=(12, 12))
    for r in range(10):
        for c in range(10):
            ax_array[r, c].matshow(np.array(X[10 * r + c].reshape((20, 20))).T, cmap='gray_r')
    plt.xticks([])
    plt.yticks([])
