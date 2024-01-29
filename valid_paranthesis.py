class Solution:
    """
    Solution using stack 
    """
    def isValid(self, s: str) -> bool:
        if not len(s) >1:
            return False 

        brackets = {'(':')','{':'}','[':']'}
        total = []

        for i in s:
            if i in brackets: # open bracket 
                total.append(brackets[i])
            else:
                if not len(total):
                    return False 
                else:
                    last = total.pop(-1)
                    if last != i:
                        return False 
            
        return not len(total)
