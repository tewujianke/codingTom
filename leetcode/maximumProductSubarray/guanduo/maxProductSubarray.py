"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

#using DP to solve
#need to track both max and min values so far because -
#a negative number could turn the min value into the max value so far and vice versa
#In addition, current number could be a new start of the subarray.
#So a global variable result is needed to keep track the global maximum (inside the for loop instead of outside)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]  #initialize all global variables
        min_so_far = nums[0]
        result = nums[0]     #this guy is needed to keep track the global maximum as we abandon max_so_far if a new start is encountered
        for i in range(1,len(nums)):
            mx = max_so_far  #have tmp variables to hold max and min for calculations below
            mn = min_so_far
            max_so_far = max(nums[i]*mx,nums[i]*mn,nums[i]) #3 cases: same sign, 0 or opposite sign, new subarray start
            min_so_far = min(nums[i]*mx,nums[i]*mn,nums[i]) #update minimum accordingly
            
            result = max(result,max_so_far) #keep track of the global maximum as we abandon max_so_far upon new start
        return result

