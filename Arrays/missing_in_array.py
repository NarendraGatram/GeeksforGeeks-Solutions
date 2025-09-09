'''
    Problem: Missing element in array
    Link: https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&category=Arrays,Strings&sortBy=submissions
    Category: Arrays
    Difficulty: Easy
'''

class Solution:
    def missingNum(self, arr):
        # code here
        sum_arr = 0
        n = len(arr)+1
        for i in range(n-1):
            sum_arr += arr[i]
        
        total_sum =  (n*(n+1))//2
        
        return total_sum- sum_arr