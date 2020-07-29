#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Initialize W randomly so that we break the symmetry while
%               training the neural network.

以下是PDF中的要求，所以必须要用到epsilon_init = 0.12
% Randomly initialize the weights to small values
epsilon init = 0.12;
W = rand(L out, 1 + L in) * 2 * epsilon init 􀀀 epsilon init;
:Time:  2020/7/29 12:19
:Author:  lenjon
"""
import numpy as np


def randInitializeWeights(L_in, L_out):
    W = np.zeros((L_out, 1 + L_in))
    pass
    epsilon_init = 0.12
    W = np.random.rand(L_out, 1 + L_in) * 2 * epsilon_init - epsilon_init
    print(W.shape)
    return W
