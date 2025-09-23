'''
    Problem:Given two arrays, find their union.
    Link: https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?page=1&category=Arrays,Strings&status=unsolved&sortBy=submissions
    Difficulty: Medium
    Category: Arrays
'''

class Solution:
    def findUnion(self, a, b):
        # code here 
        a = list(set(a))
        b = list(set(b))
        
        result = []
        result = a+b
        
        result = set(result)
        
        return sorted(result)