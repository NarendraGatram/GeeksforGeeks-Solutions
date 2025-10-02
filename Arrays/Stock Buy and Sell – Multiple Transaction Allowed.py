'''
    Problem Statement: Given an array of prices where prices[i] is the price of a given stock on the ith day,
    find the maximum profit you can achieve. You may complete as many transactions as you like 
    (i.e., buy one and sell one share of the stock multiple times).
    Note: You may not engage in multiple transactions at the same time
    (i.e., you must sell the stock before you buy again).
    Link: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/stock-buy-and-sell2615
    Difficulty: Medium
    category: Arrays

'''

from typing import List
class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        total_profit = 0
        n = len(prices)
        
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                profit = prices[i]-prices[i-1]
                total_profit=total_profit+profit
        
        return total_profit
