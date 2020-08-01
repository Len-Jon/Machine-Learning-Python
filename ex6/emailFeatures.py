#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return a feature vector for the
%               given email (word_indices). To help make it easier to
%               process the emails, we have have already pre-processed each
%               email and converted each word in the email into an index in
%               a fixed dictionary (of 1899 words). The variable
%               word_indices contains the list of indices of the words
%               which occur in one email.
:Time:  2020/8/1 21:35
:Author:  lenjon
"""
import numpy as np


def emailFeatures(word_indices):
    n = 1899  # 词汇总数
    x = np.zeros(n)
    pass
    x[word_indices] = 1
    return x


