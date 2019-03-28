"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
Example:
Given n = 5, and version = 4 is the first bad version.
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version. 
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

"""
use recursive way to find the first bad one.
Do it using binary search. Exit if current one is bad but previous one is good. Otherwise go the the previous half or the next half depending on the result
"""
import math #use the ceiling
class Solution:

    def util(self,index,lower,higher):

        if isBadVersion(index) and not isBadVersion(index-1):
            return index

        elif isBadVersion(index):
            return self.util(index//2,lower,index)
        else:
            return self.util(math.ceil((higher-index)/2+index),index,higher)#get the ceiling of it
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <=1: return 1

        return self.util(math.ceil(n//2),0,n)
