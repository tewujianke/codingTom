"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0                     #### tmp adds every element in nums
        maxVal = float('-inf')
        for n in nums :
            if n >= 0 and tmp < 0 :
                tmp = n             ### if we find tmp < 0, it means tmp + n < n which is not largest sum. Therefore, we reset the tmp to n
            elif n < 0 and tmp < 0 :
                tmp = max(n,tmp)    ### if n and tmp are all negative, we need to store the larest one 
            else :
                tmp = tmp + n       
            maxVal = max(maxVal,tmp)
        return (maxVal)
