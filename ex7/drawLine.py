#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/8/5 20:53
:Author:  lenjon
"""


def drawLine(p1, p2, plt, linestyle='k-'):
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], linestyle)
