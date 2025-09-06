'''
    Problem: Reverse Words in a given String separated by dots
    Link: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
    Category: Strings
'''


class Solution:
    def reverseWords(self, s):
        # code here
        s = s.strip('.')
        sList = s.split('.')
        
        sList = [word for word in sList if word]
        
        sList.reverse()
        
        s = '.'.join(sList)
        
        return s