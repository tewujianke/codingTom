"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""
"""
if current number reduces the local max, 
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <2: return nums[0]
        if len(nums) == 0: return None
        
        global_max = cur = nums[0]

        for i in range(1,len(nums)):
            cur = max(nums[i],cur+nums[i])
            global_max = max(global_max,cur)
        return global_max
