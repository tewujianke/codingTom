"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""
class Solution(object):
    #top down approach with memo
    #if we've determined a location is not able to reach the end, mark that location to -1 as an indicator.
    #this avoids repeated search, which reduce the time complexity from 2^n to n^2
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(nums,index):
            if index >= len(nums)-1:
                return True
            if nums[index] == 0:
                return False
            if nums[index] == -1:
                return False
            cur = nums[index]
            while cur>0:
                result = helper(nums,index+cur)
                if result: return True
                else: 
                    if index+cur < len(nums):
                        nums[index+cur] = -1
                cur-=1
            nums[index] = -1
            return False

        return helper(nums,0)

    #bottom up approach. The last index is always valid
    #start from second last to the lestmost index.
    #having a temporay variable that records the last position that can reach the end
    #if current index + num[index] >= the last index, meaning it is able to reach the end
    #then update teh temp variable to the current index
    #in the end, if index 0 can reach the end, then return True
    
    def canJumpBottomUp(self,nums):

        lastValid = len(nums) -1

        for i in range(len(nums)-2,-1,-1):

            if nums[i] + i >= lastValid
            lastValid = i
        return True if not lastValid else False
        
            
