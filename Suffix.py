class Solution:
    def longestCommonSuffix(self, strs: List[str]) -> str:
        """
        Naive Solution: 
        1- Sort the list
        2- Pick the shortest string 
        3- Search for that string in other strings ( Linear Search )
        4- If not found, decrease the length of the strength by one and keep doing that until nothing is found  
        """

        strs = sorted(strs)
        # O(MN) M: Length of the shortest string, N: Number of words 
        smallest = strs[0]
        for i in range(len(smallest)):
            if all([smallest in i for i in strs[1:]]):
                return smallest 
            else:
                smallest = smallest[:-1] # Strip last character 
        
        return ""
       
 
class PrefixSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Naive Solution: 
        1- Sort the list
        2- Pick the shortest string 
        3- Search for that string in other strings ( Linear Search )
        4- If not found, decrease the length of the strength by one and keep doing that until nothing is found  
        """

        strs.sort(key=lambda x: len(x))
        # O(MN) M: Length of the shortest string, N: Number of words 
        smallest = strs[0]
        pattern = "" 
        for i in range(len(smallest)):
            if len(set([j[i] for j in strs])) > 1:
                break
            pattern += smallest[i]
                
        
        return pattern

