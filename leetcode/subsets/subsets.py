"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def helper(arr, i) :
            if i < len(nums):
                tmp = []
                for n in arr :
                    tmp.append(n+[nums[i]])
                arr = arr + tmp
            else :
                return arr 
            return helper(arr,i+1)
        return (helper([[]],0))

