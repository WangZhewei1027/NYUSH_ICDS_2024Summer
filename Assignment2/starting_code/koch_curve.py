#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:30:18 2024

@author: bing
"""

from math import sin, cos, pi
from matplotlib import pyplot as plt


def get_u_coordinates(s, t):
    x = (t[0]-s[0])*cos(pi/3)-(t[1]-s[1])*sin(pi/3)+s[0]
    y = (t[0]-s[0])*sin(pi/3)+(t[1]-s[1])*cos(pi/3)+s[1]

    return (x, y)


def get_s_coordinates(p1, p2):
    x = (2 * p1[0] + 1 * p2[0]) / 3
    y = (2 * p1[1] + 1 * p2[1]) / 3

    return (x, y)


def get_t_coordinates(p1, p2):
    x = (1 * p1[0] + 2 * p2[0]) / 3
    y = (1 * p1[1] + 2 * p2[1]) / 3

    return (x, y)


def koch_curve(p1, p2, n, n_max):
    s = get_s_coordinates(p1, p2)
    t = get_t_coordinates(p1, p2)
    u = get_u_coordinates(s, t)
    if n == 0:
        return ([p1]+koch_curve(p1, s, n+1, n_max)+koch_curve(s, u, n+1, n_max)+koch_curve(u, t, n+1, n_max)+koch_curve(t, p2, n+1, n_max))
    elif n < n_max:
        return (koch_curve(p1, s, n+1, n_max)+koch_curve(s, u, n+1, n_max)+koch_curve(u, t, n+1, n_max)+koch_curve(t, p2, n+1, n_max))
    else:
        return [p2]


if __name__ == "__main__":
    p1 = (0, 0)
    p2 = (100, 0)

    n_max = 3
    coordinates = koch_curve(p1, p2, 0, n_max)
    print(coordinates)

    # Uncomment the following statements
    # They will plot the koch curve
    x = [c[0] for c in coordinates]
    y = [c[1] for c in coordinates]
    plt.axis('equal')
    plt.plot(x, y)
    plt.show()
