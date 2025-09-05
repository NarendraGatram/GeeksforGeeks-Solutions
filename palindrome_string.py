"""
Problem: Palindrome String
Link: https://www.geeksforgeeks.org/problems/palindrome-string0817/1?page=1&category=Strings&sortBy=submissions
Category: Strings
Difficulty: Easy
"""

class Solution:
    def isPalindrome(self, s):
        # code here
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("abba"))  # True
    print(sol.isPalindrome("abc"))   # False

        


