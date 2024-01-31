class Solution:
    def climbStairs(self, n: int) -> int:
        # Similar to the concept of fib series
        # O(N) solution 

        fib = [1,1]
        for i in range(2,n+1):
            fib.append(fib[i-1]+fib[i-2])
        
        return fib[n]
