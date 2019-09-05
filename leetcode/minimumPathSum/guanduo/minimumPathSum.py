"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

"""
Two ways:
brutal force - 2^(m+n) will definitely exceed time limit
DP: work from the down-right corner. Popluate one row at a time
if last row, then the current number is just the sum of it and its right neighbor
If last col, then the current number is just the sum of it and its down neighbor
otherwise, the current number is min of it plus right and current number plus down
return the [0][0] element at last
"""
class Solution(object):
    def minPathSumTLE(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #this would exceed time limit as we are doing 2^(m+n) times
        def helper(grid,row,col):
            sum0,sum1 = float('inf'),float('inf')
            if row == len(grid)-1 and col == len(grid[0])-1: #just return last number
                return grid[row][col]
            if row+1 <= len(grid)-1: #go down
                sum0 = grid[row][col]+helper(grid,row+1,col)
            if col+1 <= len(grid[0])-1:#go right
                sum1 = grid[row][col]+helper(grid,row,col+1)
            return min(sum0,sum1)
        return helper(grid,0,0)
    #a better approach
    def minPathSum(self,grid):
        
        row = len(grid)-1
        col = len(grid[0]) -1
        #work from last row, then row-1, row-2...
        while 1:
            if col == -1:
                if row == 0: break #break the forever loop when we are at [0][0]
                col = len(grid[0]) -1 #recharge col and reduce row 
                row -= 1
            if row == len(grid)-1 and col == len(grid[0]) -1: #last number. do nothing
                col-=1
                continue
            if row == len(grid)-1: #last row
                grid[row][col] += grid[row][col+1]
                col-=1
                continue
            if col == len(grid[0])-1: #last col
                grid[row][col] += grid[row+1][col]
                col-=1
                continue
            #regular slot
            grid[row][col] = min(grid[row][col]+grid[row+1][col],grid[row][col]+grid[row][col+1])
            col-=1
        return grid[0][0]
