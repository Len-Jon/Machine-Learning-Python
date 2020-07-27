#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/27 14:18
:Author:  lenjon
"""
import matplotlib.pyplot as plt


def plotData(x, y):
    """
    绘制散点图
    :param x:  x
    :param y:  y
    :return: None
    """
    pass
    plt.scatter(x=x, y=y, c='red', marker='x')
    plt.xlabel('Population')
    plt.ylabel('Profit')
    plt.show()
