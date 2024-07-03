#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:08:56 2024

@author: bing
"""


def max_profit(prices):

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for i in range(1, len(prices)):
        current_price = prices[i]
        current_profit = current_price - min_price
        max_profit = max(max_profit, current_profit)
        min_price = min(min_price, current_price)

    return max_profit


if __name__ == "__main__":

    prices = [800, 300, 600, 200, 100]
    # print(max_profit(prices))
    print(max_profit(prices))

    prices = [800, 300, 200, 100, 0]
    # print(max_profit(prices))
    print(max_profit(prices))
