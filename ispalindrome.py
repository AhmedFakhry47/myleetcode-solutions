"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome_alternative(self, x: int) -> bool:
        if x <0:
            return False
        return str(x) == str(x)[::-1]

    def isPalindrome(self,x:int) -> bool:
        # We don't need to compare the whole string ( Only half matters )
        x = str(x)

        for i in range(len(x)//2):
            if x[i] == x[~i]:continue # Don't write x[i] == x[len(x) -1 -i] this is bad 
            else:
                return False 
            
        return True 

