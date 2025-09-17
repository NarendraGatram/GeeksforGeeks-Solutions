'''
    problem: Check if two arrays are equal or not
    Link : https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?page=1&category=Arrays,Strings,Stack&status=unsolved&sortBy=submissions
    Difficulty : Easy
    Category : Arrays
'''

class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a = sorted(a)
        b = sorted(b)
        
        return a==b
        
        