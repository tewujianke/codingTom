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

basic idea: because we go left and then go right.

we will go through the leaf node from left to right. Therefore, we find the max depth first, and start to check if each null node meet the requirement of complete tree.

 */
class Solution {
    private int maxDepth = -1;
    private boolean alreadyFinished = false;   
    public boolean isCompleteTree(TreeNode root) {
        return this.DFS(root,0);
    }
    private boolean DFS(TreeNode node, int depth) {
        if (node == null) {
            if (maxDepth == -1) {maxDepth = depth; }    // we meet the first null node, so we record the max depth first. 
            
            if (maxDepth == depth && alreadyFinished == false) { 
                return true ;
            } else if (maxDepth > depth + 1 ) {     // obviously, this is not the complete node if we found the null node and its depth + 1 < maxDepth.
                return false;
            } else if (maxDepth == depth + 1) {       // if we found the null node which its depth + 1 == maxDepth, this means the last level is not completely full.
                if (alreadyFinished == false ) {
                    alreadyFinished = true;         
                }
                return true;
            } else {
                return false;
            }    
        } else {
            return this.DFS(node.left,depth+1) && this.DFS(node.right,depth+1);
        }
    } 
}
