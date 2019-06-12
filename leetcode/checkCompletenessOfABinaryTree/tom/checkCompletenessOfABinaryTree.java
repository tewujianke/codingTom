/*

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Note:

The tree will have between 1 and 100 nodes.



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

basic idea : just use BFS go through all node, and check if there are null node between first and last non null node.

*/

class Solution {
    public boolean isCompleteTree(TreeNode root) {
        List<Integer> finalList= new ArrayList<Integer>();    // this array is used to store all node
        List<TreeNode> currList= new ArrayList<TreeNode>();   // these two arrays are used to run BSF 
        List<TreeNode> nextList = new ArrayList<TreeNode>();
        currList.add(root);
        while (currList.size()>0 || nextList.size() > 0) {
            if (currList.size()==0) {
                List<TreeNode> tmpList = currList;
                currList = nextList;
                nextList = tmpList;
            }
            TreeNode tmp = currList.remove(0);
            if (tmp==null) {
                finalList.add(null);
                continue;
            } else {
                finalList.add(tmp.val);
                nextList.add(tmp.left);
                nextList.add(tmp.right);
            }
        }                                       
        boolean meetNull = false;             // finally, check if the tree is complete. 
        for (Integer a : finalList) {         // if we already meet null and we meet non null element again. it must be not complete tree    
            if (meetNull == true && a != null) {
                return false;
            }
            if (a == null) {
                meetNull = true;
            }
        }
        return true;
    }
}
