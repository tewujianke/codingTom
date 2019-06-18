"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
Accepted
"""

"""
use DFS. iterate through each element of the 2d array.
If current element is 1, kick-off the sanitation process -
which clears the current location, then recursively goes towards
each of the four directions until a point without 1.
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def sanitizeIsland(row,col,grid):
            if row >= len(grid)    or row<0:   return  #exit condition
            if col >= len(grid[0]) or col<0:   return
            if grid[row][col] != '1': return           #exit when no longer '1' (boundary of the island)
            grid[row][col] = '0';                      #clear current location
            sanitizeIsland(row-1,col,grid);            #DFS to all directions
            sanitizeIsland(row+1,col,grid);
            sanitizeIsland(row,col+1,grid);
            sanitizeIsland(row,col-1,grid);
        result = 0
        for row in range(len(grid)):                   #iterate through all elements in the 2D array
            for col in range(len(grid[row])):
                if grid[row][col] == '1':              #found a new island
                    result +=1
                    sanitizeIsland(row,col,grid)       #kick off the sanitation process to clear current encountered island
        return result
                
