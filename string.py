# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 00:24:41 2019

@author: zhiqi
@ copyright reserved by Data structures and Algorithms in Python of Zongyan PEI
"""

'''
KMP Algo for string matching
'''
def matching_KMP(t, p, next):
    '''Main function of KMP algo'''
    j ,i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i == j+1, i+1
        else:
            i = pnext[i]
    if i == m:
        return j-i
    return -1