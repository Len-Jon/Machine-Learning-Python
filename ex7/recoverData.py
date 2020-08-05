#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Compute the approximation of the data by projecting back
%               onto the original space using the top K eigenvectors in U.
%
%               For the i-th example Z(i,:), the (approximate)
%               recovered data for dimension j is given as follows:
%                    v = Z(i, :)';
%                    recovered_j = v' * U(j, 1:K)';
%
%               Notice that U(j, 1:K) is a row vector.
:Time:  2020/8/5 21:58
:Author:  lenjon
"""

import numpy as np


def recoverData(Z, U, K):
    X_rec = np.zeros((Z.shape[0], U.shape[0]))
    pass
    U_reduced = U[:, :K]
    X_rec = Z @ U_reduced.T
    return X_rec
