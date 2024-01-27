"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""

import copy 

class Solution:
    # O(N) T O(1) S Using two pointers 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two pointers solution 

        # Sort the array and store the index of elements 
        sorted_ = sorted([(elem,index) for index,elem in enumerate(nums)])
        f,l = 0,len(sorted_) - 1

        while f<l: 
            sum_ = sorted_[f][0] + sorted_[l][0]
            if sum_ > target:
                l -=1
            elif sum_ < target:
                f +=1 
            else:
                break
        return [sorted_[f][1],sorted_[l][1]]
