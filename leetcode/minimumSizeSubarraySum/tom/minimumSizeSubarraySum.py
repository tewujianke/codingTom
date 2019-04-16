"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

"""


"""
basic idea: we use two pointers to track the array.

we just keep moving forward pointer and leave previous pointer stand if the sum from previous pt to forward pt is smaller than s

when the sum is equal or larger than s, we just remember how many element we need,
and start to substract the sum from the previous pointer element and check again if the sum is still larger or eqaul to s

and repeat the above procedure.

"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        minVal = float('inf')
        previousPt = 0
        sumVal = 0
        for i in range(len(nums)) :   ### i is forward pointer
            sumVal += nums[i]
            while sumVal >= s :
                minVal = min(minVal,i - previousPt + 1)
                sumVal -= nums[previousPt]
                previousPt += 1
        if minVal == float('inf') :   ### if minVal is still infinite, it means, the sum is always smaller than s 
            return 0
        else :
            return (minVal)
