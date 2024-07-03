#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:50:19 2020

@author: xg7
"""
nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rome = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


def convert_to_Roman_numeral(n):
    r = ""
    for i in range(len(nums)):
        while n >= nums[i]:
            r += rome[i]
            n -= nums[i]
    return r


    # test
if __name__ == "__main__":
    n = 3999
    print(convert_to_Roman_numeral(n))
