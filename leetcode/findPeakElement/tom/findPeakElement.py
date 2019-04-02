"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 :
            return 0
        elif nums[0] > nums[1] :
            return 0
        elif nums[len(nums)-1] >  nums[len(nums)-2] :
            return len(nums)-1
        ### check if first point or endpoint is peak
        nums = [float('-inf')] + nums + [float('inf')]
        lo = 0
        hi = len(nums) - 1
        def binarySearch(lo,hi) :
            if lo > hi :
                return -100
            mid = (hi + lo) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1] :  ### peak finder
                return (mid - 1)
            elif nums[mid+1] > nums[mid] and nums[mid] > nums[mid-1] : ### if slope is positive, we keep finding peak from right
                return binarySearch(mid+1,hi)
            elif nums[mid] > nums[mid+1] and nums[mid-1] > nums[mid] :  ### if slope is negative, find peak from left
                return binarySearch(lo,mid-1)
            else :                                   ### in the bottom, like guanduo,  such a loser             we can go both way 
                return binarySearch(lo,mid-1)

        return binarySearch(0,len(nums)-1)
