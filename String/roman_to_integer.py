'''
    Problem: Roman to Integer 
    Link: https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1?page=1&category=Strings&sortBy=submissions
    Category: Strings
    Difficulty: Easy
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I' : 1  , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 ,  'D' : 500 , 'M' : 1000}
        
        result = 0
        n = len(s)-1

        for i in range(n):
            if i<n-1 and roman_dict[s[i]]<roman_dict[s[i+1]]:
                result -=roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        
        return result