'''
    Problem: Anagram 
    Link: https://www.geeksforgeeks.org/problems/second-largest3735/1
    Category: Arrays
    Difficulty: Easy
'''


class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)<2:
            return -1
            
        maxi = arr[0]
        secondLargest = 0
        
        for i in range(1,len(arr)):
            if arr[i]>maxi:
                secondLargest=maxi
                maxi=arr[i]
            elif arr[i]<maxi and arr[i]>secondLargest:
                secondLargest = arr[i]
                
        
        if secondLargest:
            return secondLargest
        else:
            return -1
        