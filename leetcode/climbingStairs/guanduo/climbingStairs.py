"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
"""
Use DP to solve. To reach the current index, the number of solution is the sum of 
the number of solutions to the previous index and the number of solutions to the last 2 elements
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp0 = 0
        dp1 = 1
        cur = 0
        for i in range(n):
            cur = dp0+dp1
            dp0 = dp1
            dp1 = cur
        return cur

if __name__ == '__main__':

    n = 5
    sol = Solution()
    print(sol.climbStairs(n))

         
