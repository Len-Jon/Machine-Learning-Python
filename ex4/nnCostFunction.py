#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
:Time:  2020/7/29 0:22
:Author:  lenjon
"""
import numpy as np
from sklearn.preprocessing import OneHotEncoder

from ex4.sigmoid import sigmoid
from ex4.sigmoidGradient import sigmoidGradient


def forward_propagate(X, Theta1, Theta2):
    """
    前向传播
    :param X: 输入
    :param Theta1: 权重矩阵1
    :param Theta2: 权重矩阵2
    :return: 输出结果
    """
    m = X.shape[0]

    a1 = np.insert(X, 0, values=np.ones(m), axis=1)  # 添加偏置量
    z2 = a1 @ Theta1.T  # 第二层激活值（入参）样本数量 * 第二层神经元数量
    a2 = np.insert(sigmoid(z2), 0, values=np.ones(m), axis=1)  # 第二层所有单元，并添加偏置
    z3 = a2 @ Theta2.T  # 输出层激活值
    h = sigmoid(z3)  # 获得输出结果矩阵（样本数量 * 输出单元数量）

    return a1, z2, a2, z3, h


def nnCostFunction(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, _lambda):
    Theta1 = nn_params[0:hidden_layer_size * (input_layer_size + 1)].reshape(hidden_layer_size, input_layer_size + 1)
    Theta2 = nn_params[(hidden_layer_size * (input_layer_size + 1)):].reshape(num_labels, hidden_layer_size + 1)
    m = X.shape[0]

    J = 0
    Theta1_grad = np.zeros(Theta1.shape)
    Theta2_grad = np.zeros(Theta2.shape)
    pass
    # 由于是一对多，这里我们要把y展开
    # 上次我用的是 y_i = np.array([1 if label == i else 0 for label in y]).reshape(m, 1)
    # 这次我们用现成的库，
    """当然也可以参考MATLAB的解法
    yk=zeros(m,num_labels);
    for i=1:m
        yk(i,y(i))=1;
    end
    """
    encoder = OneHotEncoder(sparse=False)
    y_onehot = encoder.fit_transform(y)  # 这里可以检查一下是否为5000*10的矩阵，并且10代表0

    # 前向传播获取结果
    a1, z2, a2, z3, h = forward_propagate(X, Theta1, Theta2)
    # 计算代价函数
    J = np.sum(-y_onehot * np.log(h) - (1 - y_onehot) * np.log(1 - h)) / m \
        + (_lambda / (2 * m)) * (np.sum(np.power(Theta1[:, 1:], 2)) + np.sum(np.power(Theta2[:, 1:], 2)))

    # 以下为反向传播获取梯度

    for t in range(m):
        a1t = a1[t:t + 1, :]  # (1, 401)
        z2t = z2[t:t + 1, :]  # (1, 25)
        a2t = a2[t:t + 1, :]  # (1, 26)
        ht = h[t:t + 1, :]  # (1, 10)
        yt = y_onehot[t:t + 1, :]  # (1, 10)

        d3t = ht - yt  # (1, 10)

        Theta2_grad = Theta2_grad + d3t.T @ a2t

        z2t = np.insert(z2t, 0, values=np.ones(1))  # 补上偏置单元
        d2t = np.multiply((Theta2.T @ d3t.T).T, sigmoidGradient(z2t))  # 链式求导法则
        Theta1_grad = Theta1_grad + (d2t[:, 1:]).T @ a1t

    Theta1_grad = Theta1_grad / m
    Theta2_grad = Theta2_grad / m

    # 第八部分的时候再加上正则化
    Theta1_grad[:, 1:] = Theta1_grad[:, 1:] + (Theta1[:, 1:] * _lambda) / m
    Theta2_grad[:, 1:] = Theta2_grad[:, 1:] + (Theta2[:, 1:] * _lambda) / m

    return J, np.append(Theta1_grad.flatten(), Theta2_grad.flatten())
