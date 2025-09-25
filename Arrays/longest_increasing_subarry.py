'''
    Problem Statement: Given an array of positive integers.
    Find the length of the longest sub-array which is strictly increasing.
    Link: https://www.geeksforgeeks.org/problems/longest-increasing-subarray3811/1?page=1&category=Arrays,Strings&sortBy=difficulty
    Difficulty: Basic    
    Category: Arrays
'''

#User function Template for python3
class Solution:
    def lenOfLongIncSubArr(self, arr):
        #Code here
        n = len(arr)
        max_len = 1
        prev_len = 1
        for i in range(1,n):
            if arr[i-1]<arr[i]:
                prev_len += 1
                max_len = max(max_len,prev_len)
            else:
                prev_len = 1
        
        return max_len
            
    
    
    