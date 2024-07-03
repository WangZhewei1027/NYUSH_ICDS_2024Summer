#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:36:21 2024

@author: bing
"""
import math


def search_with_loop_limit(sorted_lst, n, d=0):
    if len(sorted_lst) == 0:
        return f'(False, {d})'
    elif len(sorted_lst) == 1:
        if sorted_lst[0] != n:
            return f'(False, {d})'
        else:
            return f'(True, {d})'
    else:
        mid = math.floor(len(sorted_lst) / 2)
        if sorted_lst[mid] > n:
            return search_with_loop_limit(sorted_lst[:mid - 1], n, d + 1)
        elif sorted_lst[mid] < n:
            return search_with_loop_limit(sorted_lst[mid + 1:], n, d + 1)
        elif sorted_lst[mid] == n:
            return f'(True, {d})'


if __name__ == "__main__":

    integers = [77, 88, 99, 101, 203, 555, 896]
    print(search_with_loop_limit(integers, 101))
    print(search_with_loop_limit(integers, 1001))
