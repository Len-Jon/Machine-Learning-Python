#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/8/9 22:15
:Author:  lenjon
"""
import numpy as np

def normalizeRatings(Y, R):
    m, n = Y.shape
    Ymean = np.zeros(m)
    Ynorm = np.zeros(Y.shape)
    for i in range(m):
        idx = np.where(R[i] == 1)
        Ymean[i] = np.mean(Y[i, idx])  # 计算每一部电影的平均评分 仅对有评分的数据计算
        Ynorm[i, idx] = Y[i, idx] - Ymean[i]  # 得到新的评分矩阵   对有评分的数据减去对应电影的平均评分

    return Ynorm, Ymean