'''
    Problem:Array Leader
    Link: https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?page=1&category=Arrays,Strings&sortBy=submissions
    Category: Arrays
    Difficulty: Easy
'''

class Solution:
    def leaders(self, arr):
        # code here
        result = []
        n = len(arr)
        leader = arr[-1]
        result.append(leader)
        
        for i in range(2,n+1):
            if arr[-i]>= leader:
                result.append(arr[-i])
                leader = arr[-i]
        
        result.reverse()
        
        return result
                