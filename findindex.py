class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window = len(needle)
        found  = False 

        for i in range(len(haystack)):
            if needle == haystack[i:(i+window)]:
                found = True 
                break

        if found:
            return i
        else:
            return -1         
