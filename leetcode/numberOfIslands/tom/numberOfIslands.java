/*

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


*/


/*

basic idea : we can consider this 2D array as a graph.

therefore, we use BFS to go through every node which is 1, and add the island number by one, and then mark the nodes as visited

(after finishing this I noticed that using DFS can greatly reduce the codes line)

*/

import java.util.*;
class Solution {
    int ans = 0;
    public int numIslands(char[][] grid) {
        if (grid.length == 0) return 0;
        int row = grid.length;
        int col = grid[0].length;
        for (int x = 0; x<row; x++) {
            for (int y = 0; y<col; y++) {
                if (grid[x][y] == '1' ) {
                    this.BSF(x,y,grid);
                }
            }
        }
        return ans;
    }
    private void BSF(int rowNum, int colNum,char[][] grid) {
        if (grid[rowNum][colNum]==0) {
            return ;
        } 
        grid[rowNum][colNum] = 0 ;
        List<Integer> tmp = new ArrayList<Integer>();
        tmp.add(rowNum);
        tmp.add(colNum);
        List<List<Integer>> bfsList = new ArrayList<List<Integer>>();
        bfsList.add(tmp);                    // put the firt pair(x,y) into the BFS list
        while (bfsList.size() != 0) {
            List<Integer> tmpPoints = bfsList.remove(0);
            int tmpx = tmpPoints.get(0);
            int tmpy = tmpPoints.get(1);                                        
            if (tmpx < grid.length -1 && grid[tmpx+1][tmpy]=='1') {    // we go through four directions to check if there is any other island
                tmp = new ArrayList<Integer>();                        // which connect to the current center island
                tmp.add(tmpx+1);                                       // if we found it, we just put the island to the BFS list and mark it as visited (0) 
                tmp.add(tmpy);                                        
                bfsList.add(tmp);
                grid[tmpx+1][tmpy] = 0 ;
            }
            if (tmpy < grid[0].length -1 && grid[tmpx][tmpy+1]=='1') {
                tmp = new ArrayList<Integer>();
                tmp.add(tmpx);
                tmp.add(tmpy+1);
                bfsList.add(tmp);
                grid[tmpx][tmpy+1] = 0; 
            }
            if (tmpx > 0 && grid[tmpx-1][tmpy] == '1') {
                tmp = new ArrayList<Integer>();
                tmp.add(tmpx-1);
                tmp.add(tmpy);
                bfsList.add(tmp);
                grid[tmpx-1][tmpy] = 0 ;
            }
            if (tmpy > 0 && grid[tmpx][tmpy-1] == '1') {
                tmp = new ArrayList<Integer>();
                tmp.add(tmpx);
                tmp.add(tmpy-1);
                bfsList.add(tmp);
                grid[tmpx][tmpy-1] = 0;
            }
        } 
        ans += 1 ;     // after one round BFS, we can add one to total island number.
    }
}   
