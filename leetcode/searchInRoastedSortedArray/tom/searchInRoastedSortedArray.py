"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

#### define two function, binarySearch  and  FindPivot




class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 :
            return -1

                
        def binarySearch(arr,lo,hi,target) :
            if hi < lo :
                return -1
            mid = (lo + hi) // 2
            if arr[mid] == target :
                return mid
            else :
                if arr[mid] > target :
                    return binarySearch(arr,lo,mid-1,target)
                else :
                    return binarySearch(arr,mid+1,hi,target)
        

        findPivotArr = []           """put slice point into this array in case we slice the pivot point """
        def findPivot(arr,lo,hi) :
            if hi < lo :
                return -100
            findPivotArr.append([lo,hi])
            if hi-lo <= 5 :
                tmp = arr[lo]
                for n in range(lo,hi+1) :
                    if arr[n] < tmp :
                        return n
                    else :
                        tmp = arr[n]
                return -100

            else :

                mid = (lo + hi) // 2

                a = findPivot(arr,lo, mid)
                b = findPivot(arr,mid+1,hi)

                return max(a,b)
        tmp = findPivot(nums,0,len(nums)-1)    """if tmp == -100, we dont find the pivot point  there are two cases which will cause this situation"""
        PivotInd = -1                          """first one the array is sorted correctly  """
        if tmp == -100 :                       """second we slice the array by following situation 9,10,12,1,4,5,7 -> 9,10,12 & 1,4,5,7 """
            for lo, hi in findPivotArr :       """that's why we need to store the slice index and find again """
                if lo > 0 :
                    if nums[lo-1] > nums[lo] :
                        PivotInd = lo 
                        break
        else :
            PivotInd = tmp
        if PivotInd != -1 :                                                          """ after find the pivot point, I tear them into two parts and do binary search"""
            front = binarySearch(nums[:PivotInd],0, len(nums[:PivotInd])-1,target)
            end = binarySearch(nums[PivotInd:],0, len(nums[PivotInd:])-1,target)
        
            if front != -1 :
                return front
            elif end != -1 :
                return PivotInd + end
            else :
                return -1
        else :                                                          
            return binarySearch(nums[:],0,len(nums)-1,target)
