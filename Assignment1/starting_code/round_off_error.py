#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:48:42 2021

@author: bing
"""
import math


def fraction2binary(f, space):
    # complete the code
    b = ''
    for i in range(0, space):
        frac, whole = math.modf(2*f)
        b += str(int(whole))
        f = frac
    return '0.'+b


def binary2fraction(b):
    # complete the code
    frac_part = b.split('.')[1]
    decimal_value = int(frac_part, 2)
    return decimal_value / (2 ** len(frac_part))


if __name__ == '__main__':
    print('2.07 - 2 =', 2.07 - 2)
    f = 0.07
    l = 52
    print('The binary of 0.07 in your machine:')
    print(fraction2binary(f, l))
    print('Influence of the Truncation error')
    print(binary2fraction(fraction2binary(f, l)))
