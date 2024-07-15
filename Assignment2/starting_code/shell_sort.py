#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:06:22 2024

@author: bing
"""


def insertion_sort_with_gap(lst, g):
    n = len(lst)
    for i in range(g, n):
        v = lst[i]
        j = i - g
        while j >= 0 and lst[j] > v:
            lst[j+g] = lst[j]
            j -= g
        lst[j+g] = v


def shell_sort(lst):
    G = [5, 3, 1]
    m = len(G)
    for i in range(0, m):
        insertion_sort_with_gap(lst, G[i])
        print(G[i])


if __name__ == "__main__":

    lst = [10, 9, 5, 6, 8, 3, 2, 1, 4, 7]
    shell_sort(lst)
    print(lst)

    lst = [0, 1, 2, 3]
    shell_sort(lst)
    print(lst)
