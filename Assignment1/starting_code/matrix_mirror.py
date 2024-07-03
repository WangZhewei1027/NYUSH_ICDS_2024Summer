#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:45:08 2020

@author: xg7
"""


def fun1(m):
    l = len(m)
    print(l)
    w, h = l, l
    t = [[0 for x in range(w)] for y in range(h)]
    for i in range(0, l):
        for j in range(0, l):
            t[i][l-1-j] = m[i][j]
    for i in range(l):
        for j in range(l):
            m[i][j] = t[i][j]


# Tests
if __name__ == "__main__":
    n = 3
    m = [[(i)*n + j + 1 for j in range(n)] for i in range(n)]
    print("input m:", m)
    fun1(m)
    print("after running fun1:", m)

    n = 4
    m = [[(i)*n + j + 1 for j in range(n)] for i in range(n)]
    print("input m:", m)
    fun1(m)
    print("after running fun1:", m)
