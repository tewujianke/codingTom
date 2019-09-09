"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
#[5,7,8,8,8,8]

"""
Binary search - two times, the first binary search finds the leftmost index, the second binary search finds the rightmost index
There is one change to the original binary search:
1. If we are looking for the leftmost index, when we find the target, we need to keep search to the left, since the found one may not be the leftmost one
2. If we are looking for the rightmost index, when we find the target, we need to keep search to the right.
If not match, just return -1.
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def helper(nums,lo,hi,target,left=True):
            found_index = -1            #initialize the found_index to -1 in case of no matching target
            while lo<=hi:               #binary search begins
                mid = (lo+hi)//2
                if nums[mid] < target:  #normal binary search. 
                    lo = mid + 1
                elif nums[mid] > target:#normal binary search.
                    hi = mid - 1
                else:                   #found target. Now let's tell whether to keep searching the leftmost one or rightmost one
                    found_index = mid
                    if left:
                        hi = mid -1
                    else:
                        lo = mid +1
            return found_index
        
        result = []
        result.append(helper(nums,0,len(nums)-1,True))  #find the left most index
        result.append(helper(nums,0,len(nums)-1,False)) #find the right most index
        return result
                      
