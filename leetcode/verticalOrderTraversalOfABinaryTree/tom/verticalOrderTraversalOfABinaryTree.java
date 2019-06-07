/*
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.


*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 



 /*

The idea is just like we discuss, I use two hashMap and one List to implement.

The special ponit is I use TreeMap which can sort the key value automatically.
 */


import java.util.*;


class Solution {
    TreeMap<Integer,TreeMap<Integer,List<Integer>>> outerMap = new TreeMap<Integer,TreeMap<Integer,List<Integer>>>();
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        this.traverseTree(root,0,0);
        for (Map.Entry<Integer,TreeMap<Integer,List<Integer>>> entry : outerMap.entrySet()) {
            List<Integer> tmp = new ArrayList<Integer>();
            for (Map.Entry<Integer,List<Integer>> innerEntry : entry.getValue().entrySet()) {
                if (innerEntry.getValue().size() >= 2) {
                    Collections.sort(innerEntry.getValue());
                }
                    tmp.addAll(innerEntry.getValue());
            }
            ans.add(tmp);
        }
        return ans;

    }
    public void traverseTree(TreeNode node, int x, int y) {
        if (node == null) {return ;}
        Integer value = node.val;
        if (outerMap.containsKey(x)) {                     // if the x key exists, it means we already have hash in another hash. 
            if(outerMap.get(x).containsKey(y)) {           // if the y key exsits, we can directly add value in to the list.
                outerMap.get(x).get(y).add(value);        
            } else {                                       // Otherwise, we need to create a new list to add to the inner hash map
                List<Integer> tmpList = new ArrayList<Integer>();
                tmpList.add(value);
                outerMap.get(x).put(y,tmpList);
            }
        } else {                                      // if both key don't exist, we just create a new hash table and list and add them into outer hash.
            TreeMap<Integer,List<Integer>> tmpMap = new TreeMap<Integer,List<Integer>>();
            List<Integer> tmpList = new ArrayList<Integer>();
            tmpList.add(value);
            tmpMap.put(y,tmpList);
            outerMap.put(x,tmpMap);
        }
        this.traverseTree(node.left,x-1,y+1);
        this.traverseTree(node.right,x+1,y+1);
    }
}
