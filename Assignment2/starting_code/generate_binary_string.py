#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:40:42 2022

@author: bing
"""


def binary_string_without_consecutive_ones(n, binary_string=[], current_str=''):
    if len(current_str) == n:
        binary_string.append(current_str)
    else:
        if current_str == '' or current_str[-1] == '0':
            binary_string_without_consecutive_ones(
                n, binary_string, current_str + '0')
            binary_string_without_consecutive_ones(
                n, binary_string, current_str + '1')
        elif current_str[-1] == '1':
            binary_string_without_consecutive_ones(
                n, binary_string, current_str + '0')
    return binary_string


if __name__ == "__main__":
    n = 3
    binary_string = []
    print(binary_string_without_consecutive_ones(n, binary_string))
    n = 4
    binary_string = []
    print(binary_string_without_consecutive_ones(n, binary_string))
