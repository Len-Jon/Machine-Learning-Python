#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不是作业
:Time:  2020/7/28 11:10
:Author:  lenjon
"""
import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))
