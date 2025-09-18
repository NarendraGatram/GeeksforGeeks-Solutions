'''
    Problem Statement: Given an array of integers, push all the zeroes to the end of it.
    Link: https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1?page=1&category=Arrays&sortBy=submissions
    Difficulty: Easy
    Category: Arrays
'''

class Solution:
	def pushZerosToEnd(self, arr):
        # code here
        n = len(arr)
        pos = 0
        
        for i in range(n):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
                
        for i in range(pos, n):
            arr[i] = 0      
            
        return arr
		
    	
    	