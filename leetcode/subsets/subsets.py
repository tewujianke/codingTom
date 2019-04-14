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

"""
For this question, we can use recursive function to solve. but it will cost (2^n) time complexity. 

I use bottom up solotion. 
the idea is we can go through the list with the empty set.

we can add first element to the empty set to form a tmp set. 

After that, we just add the empty set and tmp set together to tmp set. 

Repeat above, we can just get all possible sets.

the complexity will become 2+4+8+16+.....   it will be O(n^2) which is less than O(2^n)

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

