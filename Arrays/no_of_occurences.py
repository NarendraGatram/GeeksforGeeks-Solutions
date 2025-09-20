''' 
    Problem : Given an array of integers arr[] of size N and an integer target,
            the task is to find the number of occurrences of target in arr[].
    Link: https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?page=1&category=Arrays,Strings,Stack&status=unsolved&sortBy=submissions
    Difficulty: Easy
    Category: Arrays
 '''

class Solution:
    def countFreq(self, arr, target):
        # code here
        freq_dict={}
        for i in arr:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        
        try:        
            return freq_dict[target]
        except:
            return 0
            
        