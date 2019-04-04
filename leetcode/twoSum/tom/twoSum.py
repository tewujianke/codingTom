"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

#### we create a dictionay to memory every element in nums because it only cause O(1) to check if the element is in the list


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmpDict = {}
        for n in nums :
            tmpDict[n] = 1                    ##### we store every element in the list to the dictionary

        for i, n in enumerate(nums) :     ### by enumerate, we can get the first one index
            if (target - n) in tmpDict :
                x = nums.index(target-n)      ###  if the element is in the dictionary, we can find its index by built-in fuction index()
                if i != x :                   ### because we cannot use the same element twice, we have to check this rule 
                    return i, nums.index(target-n)   
                else :
                    continue

if __name__ == '__main__' :
    sol = Solution()
    a = [1,3,4,5]
    target = 7
    print(sol.twoSum(a,target))

