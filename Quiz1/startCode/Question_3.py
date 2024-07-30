#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:22:25 2020

@author: xianbingu
"""



def maximum(A):
    # Base case: if the list has only one element, return that element
    if len(A) == 1:
        return A[0]
    
    # Recursive case: compare the first element with the maximum of the rest of the list
    rest_max = maximum(A[1:])
    if A[0] > rest_max:
        return A[0]
    else:
        return rest_max
    



##---test---##
##You can comment out them when you write and test your code.  

if __name__ == "__main__":
    
    A = [8]
    print(maximum(A))
    A = [3, 2, 5, 7, 9, 7]
    print(maximum(A))
    
