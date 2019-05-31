"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
"""
There could be three cases - cut is in nums1, cut is in num2 and cut is between.

e.g. nums1=1,4,6,8, nums2 = 2,4,5,8,9
The combined list is 1,2,4,4|6,8,8,9, so the median is 4+6   /2 = 5
Use binary search to find where exactly the cut is.
Notice we know the total length of the two arrays. So if I cur nums 1 this way = 1|4,6,8, then nums2 has to be 2,4,5|8,9, because the 
number of numbers on the left of the cut needs to sum to total length /2.

Whenever we find a cut, to know whether we have a right cut, we can compare the MAX value of two numbers on the left, and MIN val of two numbers on the right. If the condition is not met, we shift the binary search range to the left or right accordingly.


"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #make sure length of num1 is always smaller or equal to nums2 for easy later processing
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2,nums1)
        total_length = len(nums1)+len(nums2)

        #pointerL,R defines the range we perform binary search, as I am shifting searching range instead of changing pointer location
        #pointer1,2 defines the current guessed cut location on num1 and num2
        pointer1,pointer2,pointerL,pointerR = 0,0,0,len(nums1)

        while pointer1 <= len(nums1):
            pointer1 = (pointerR-pointerL)//2+pointerL #use binary search to determine current cut  for the smaller array
            pointer2 = total_length//2-pointer1 #as soon as we know where we cut in the smaller array, we can instantly derived the location on the bigger array - since the number of numbers of the left of the cut must be equal to total length /2

            #if out of bound (needs to cut only one of the array), we don't need to cut nums1. So use inf to aid the calculation
            left1  = float('-inf') if pointer1==0 else nums1[pointer1-1]
            left2  = float('-inf') if pointer2==0 else nums2[pointer2-1]
            right1 = float('inf')  if pointer1==len(nums1) else nums1[pointer1]
            right2 = float('inf')  if pointer2==len(nums2) else nums2[pointer2]

            
            if   left1 > right2: pointerR = pointer1 -1; #need to shift left since the cut condition is not met
            elif left2 > right1: pointerL = pointer1 +1; #need to shift right since the cut condition is not met
            else: #found the match! The MAX of left nubmers must be smaller than MIN of right numbers!
                if total_length % 2==0: #if total length is even, needs to take the middle two
                    left1 = left1 if left1 > left2 else left2
                    right1 = right1 if right1 < right2 else right2
                    return (left1+right1) /2.0
                else: #if odd, just return the bigger one of right
                    right1 = right1 if right1 < right2  else right2
                    return right1
        return -1

        
            
