class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Solution using hash-table 
        """
        roman_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        total = 0
        str_len = len(s)

        # Loop until str_len-1 and get rid of the extra if condition
        for i in range(str_len-1):  
            if roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        total += roman_map[s[-1]] 
        return total
