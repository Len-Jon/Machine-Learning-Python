#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
%PROCESSEMAIL preprocesses a the body of an email and
%returns a list of word_indices
%   word_indices = PROCESSEMAIL(email_contents) preprocesses
%   the body of an email and returns a list of indices of the
%   words contained in the email.
%

:Time:  2020/8/1 20:05
:Author:  lenjon
"""
import re
import nltk
import pandas as pd


def pre_solve(email_content):
    """
    做除了Word Stemming和Removal of non-words的所有处理
    :param email_content:
    :return:
    """
    email_content = email_content.lower()
    email_content = re.sub(r'<[^<>]+>', ' ', email_content)  # 匹配<开头，然后所有不是< ,> 的内容，直到>结尾，相当于匹配<...>
    email_content = re.sub(r'[\d]+', 'number', email_content)
    email_content = re.sub(r'(http|https)://[^\s]*', 'httpaddr', email_content)  # 匹配//后面不是空白字符的内容，遇到空白字符则停止
    email_content = re.sub(r'[^\s]+@[^\s]+', 'emailaddr', email_content)
    email_content = re.sub(r'[$]+', 'dollar', email_content)
    return email_content


def email2TokenList(email):
    """
    提取词干
    :param email:
    :return:
    """
    # I'll use the NLTK stemmer because it more accurately duplicates the
    # performance of the OCTAVE implementation in the assignment
    stemmer = nltk.stem.porter.PorterStemmer()
    email = pre_solve(email)
    # 将邮件分割为单个单词，re.split() 可以设置多种分隔符
    tokens = re.split(r'''[ @$/#.\-:&*+=\[\]?!(){},'">_<;%]''', email)
    # 遍历每个分割出来的内容
    tokenlist = []
    for token in tokens:
        # 删除任何非字母数字的字符
        token = re.sub(r'[^a-zA-Z0-9]', '', token)
        # Use the Porter stemmer to 提取词根
        stemmed = stemmer.stem(token)
        # 去除空字符串‘’，里面不含任何字符
        if not len(token):
            continue
        tokenlist.append(stemmed)
    print(' '.join(tokenlist))
    return tokenlist


def processEmail(email):
    print('==== Processed Email ====\n')
    """ 你要完成的是这里
    Instructions: Fill in this function to add the index of str to
    %               word_indices if it is in the vocabulary. At this point
    %               of the code, you have a stemmed word from the email in
    %               the variable str. You should look up str in the
    %               vocabulary list (vocabList). If a match exists, you
    %               should add the index of the word to the word_indices
    %               vector. Concretely, if str = 'action', then you should
    %               look up the vocabulary list to find where in vocabList
    %               'action' appears. For example, if vocabList{18} =
    %               'action', then, you should add 18 to the word_indices
    %               vector (e.g., word_indices = [word_indices ; 18]; ).
    """
    vocab = pd.read_table('./data/vocab.txt', header=None).iloc[:, -1]
    word_indices = []
    token = email2TokenList(email)  # 筛选出来的单词,源码过于冗杂，python可以优化
    pass
    vocab = list(vocab)
    # word_indices = [vocab.index(c) for c in token]
    for word in token:
        if word in vocab:
            word_indices.append(vocab.index(word) + 1)
    # 这样也可以，但是不好看自己的返回值是否正确，跟作业上的要求有区别，后面还要把它排序...
    # word_indices = [i + 1 for i in range(len(vocab)) if (vocab[i] in token)]

    return word_indices
