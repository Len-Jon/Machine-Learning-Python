#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/27 14:18
:Author:  lenjon
"""
import matplotlib.pyplot as plt


def plotData(x, y):
    plt.scatter(x=x, y=y, c='red', marker='x')
    plt.xlabel('Population')
    plt.ylabel('Profit')
    plt.show()
