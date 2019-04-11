"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.


"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pt1 = 0      
        pt2 = 0

        def swap(pt1,pt2):
            tmp = nums[pt1]
            nums[pt1] = nums[pt2]
            nums[pt2] = tmp

        while pt2 < len(nums) :      ### pt1 will not increment when it encounters zero.
            if nums[pt2] != 0 :    
                if pt2 == pt1 :
                    pt2 += 1         #if pt2 == pt1, it means pt1 doesnt meet zero yet. therefore keep moving forward
                    pt1 += 1
                else :
                    swap(pt1,pt2)    # if pt2 != pt1, swap them, and then moving pt1 to the next zero value.
                    pt2 += 1
                    while nums[pt1] != 0 :
                        pt1 += 1
            else :             ### pt1 will not increment when encountering zero. pt2 will keep incrementing until it meet non-zero value
                pt2 += 1
        return nums
