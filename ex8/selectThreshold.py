#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    % ====================== YOUR CODE HERE ======================
    % Instructions: Compute the F1 score of choosing epsilon as the
    %               threshold and place the value in F1. The code at the
    %               end of the loop will compare the F1 score for this
    %               choice of epsilon and set it to be the best epsilon if
    %               it is better than the current choice of epsilon.
:Time:  2020/8/9 20:30
:Author:  lenjon
"""

import numpy as np
import warnings


def selectThreshold(yval, pval):
    warnings.filterwarnings('ignore')
    f1 = 0
    # You have to return these values correctly
    best_eps = 0
    best_f1 = 0

    for epsilon in np.linspace(np.min(pval), np.max(pval), num=1001):
        pass
        # predictions = np.less(pval, epsilon)
        # fp = np.sum(np.logical_and(predictions, yval == 0))
        # fn = np.sum(np.logical_and(np.logical_not(predictions), yval == 1))
        # tp = np.sum(np.logical_and(predictions, yval))
        # precision = tp / (tp + fp)
        # recall = tp / (tp + fn)
        # f1 = (2 * precision * recall) / (precision + recall)
        pass
        if f1 > best_f1:
            best_f1 = f1
            best_eps = epsilon
    return best_eps, best_f1
