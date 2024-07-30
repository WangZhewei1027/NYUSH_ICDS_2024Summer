#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:52:06 2021

@author: bing
"""

def slope(x1, y1, x2, y2):
    if (x2-x1)!=0:
        m = (y2-y1)/(x2-x1)
        return m
    else:
        return x1

def intercept(x1, y1, x2, y2):
    c = y1 - slope(x1, y1, x2, y2)*x1
    return c


##Testing of your code
if __name__ == "__main__":
    print(slope(1, 1, 2, 2))
    print(intercept(1, 1, 2, 2))
    print(slope(0, 0, 4, 3))
    print(intercept(0, 0, 4, 3))
    print(slope(0, 0, 0, 3))
    print(intercept(0, 0, 0, 3))
    
    
