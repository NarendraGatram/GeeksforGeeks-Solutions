'''
    Problem: String rotation by each char 
    Link: https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1?page=1&category=Strings&sortBy=submissions
    Category: Strings
    Difficulty: Medium
'''

class Solution:
    def areRotations(self, s1, s2):
        # code here        
        if len(s1) != len(s2):
            return False
        
        s3 = s1+s1
        
        if s2 in s3:
            return True
        else:
            return False
        