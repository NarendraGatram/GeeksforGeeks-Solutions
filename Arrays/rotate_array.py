'''
    Problem:Given an array, rotate the array by one position in clock-wise direction.
    Link: https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1?page=1&category=Arrays,Strings,Stack&status=unsolved&sortBy=submissions
    Difficulty: Medium
    Category: Arrays
'''


#User function Template for python3
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        
        if n==0 or  d==0:
            return arr
            
        d = d%n
        
        if d==0:
            return arr
        
        def reverse(left,right):
            while(left<right):
                arr[left],arr[right] = arr[right],arr[left]
                left+=1
                right-=1
                
        reverse(0,d-1)
        reverse(d,n-1)
        reverse(0,n-1)
        
        return arr
            