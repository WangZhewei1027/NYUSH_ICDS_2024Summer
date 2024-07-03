#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 12:17:19 2022

@author: bing
"""


def sum_a_list(lst):
    if len(lst) == 2:
        return lst[0]+lst[1]
    else:
        return lst[0]+sum_a_list(lst[1:])


if __name__ == "__main__":

    print(sum_a_list([5, 4, 3, 2, 1]))
