"""
Problem: Remove Spaces
Link: https://www.geeksforgeeks.org/problems/remove-spaces0128/1?page=4&category=Strings&sortBy=submissions
Category: Strings
Difficulty: Basic
"""

#User function Template for python3
class Solution:
    def modify(self, s):
        # code here
        result = ''
        for i in s:
            if i and i!=' ':
                result += i
        return result