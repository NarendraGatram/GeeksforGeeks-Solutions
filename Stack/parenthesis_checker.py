
"""
Problem: Parenthesis Checker
Link:https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&category=Strings&sortBy=submissions
Category: Stack
Difficulty: Easy
"""


class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        n = len(s)
        
        braces_dict = {')':'(', '}':'{', ']':'['}
        
        for i in range(n):
            if s[i] in braces_dict.values(): 
                stack.append(s[i])
            elif stack and stack[-1]==braces_dict[s[i]]:
                stack.pop()
            else:
                return False
                
        if len(stack)==0:
            return True
        else:
            return False
        
        
        
        
        