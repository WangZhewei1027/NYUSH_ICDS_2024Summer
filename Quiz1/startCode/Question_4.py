#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:12:38 2017

@author: xg7
"""

# Q1
def order(p, q, n):
    ##delete the following pass 
    ##and complete the function
    if p[n]>q[n]:
        return True
    else:
        return False



# Q2
def first_max(order_f, l, n):
    ##delete the following pass 
    ##and complete the function
    t=(0,0)
    for e in l:
        if order_f(e,t,1):
            t=e
    return t


# Q3 
def last_max(order_f, l, n):
    ##delete the following pass 
    ##and complete the function
    t=(0,0)
    for e in l[::-1]:
        if order_f(e,t,1):
            t=e
    return t


##testing part. 
##You code should pass the tests and give the correst outputs.
##You can comment out them temporarily if you want. 
if __name__ == "__main__":
    print("---testing---")
    result = order((1, 2, 3), (2, 1, 4), 0)
    print("order((1, 2, 3), (2, 1, 4), 0) returns:", result)
    result = order((1, 2, 3), (2, 1, 4), 1)
    print("order((1, 2, 3), (2, 1, 4), 1) returns:", result)
    result = order((1, 2, 3), (2, 1, 4), 2)
    print("order((1, 2, 3), (2, 1, 4), 2) returns:", result)
    t = [('X', 5), ('B', 6), ('P', 4), ('X', 3), ('B', 5),('P', 6)]
    print("t =", t)
    print("first_max(order, t, 1) returns:")
    print(first_max(order, t, 1))
    print("Bonus: last_max(order, t, 1) returns:")
    print(last_max(order, t, 1))
    
