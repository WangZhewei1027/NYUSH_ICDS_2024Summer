#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:12:38 2017

@author: xg7
"""


def my_print(p, a_str):
    p("hello {}".format(a_str))


# Q1
def order(p, q, n):
    if p[n] > q[n]:
        return True
    else:
        return False


# Q2
def first_max(order_f, l, n):
    temp = (0, 0)
    for i in range(0, len(l)):
        if order_f(l[i], temp, n):
            temp = l[i]
    return temp


# Q3
def last_max(order_f, l, n):
    temp = (0, 0)
    for i in range(len(l)-1, -1, -1):
        if order_f(l[i], temp, n):
            temp = l[i]
    return temp


# testing part.
# You code should pass the tests and give the correst outputs.
# You can comment out them temporarily if you want.
if __name__ == "__main__":
    print("---testing---")
    result = order((1, 2, 3), (2, 1, 4), 0)
    print("order((1, 2, 3), (2, 1, 4), 0) returns:", result)
    result = order((1, 2, 3), (2, 1, 4), 1)
    print("order((1, 2, 3), (2, 1, 4), 1) returns:", result)
    result = order((1, 2, 3), (2, 1, 4), 2)
    print("order((1, 2, 3), (2, 1, 4), 2) returns:", result)
    t = [('X', 5), ('B', 6), ('P', 4), ('X', 3), ('B', 5), ('P', 6)]
    print("t =", t)
    print("first_max(order, t, 1) returns:")
    print(first_max(order, t, 1))
    print("Bonus: last_max(order, t, 1) returns:")
    print(last_max(order, t, 1))
