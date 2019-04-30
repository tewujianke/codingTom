/*

  Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

  Example:
  Given a binary tree 

  1
  / \
  2   3
  / \     
  4   5    
  Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

  Note: The length of path between two nodes is represented by the number of edges between them.

*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

/*
Post order traversal. Every time return two numbers - current depth and the maximum depth (like a global var) for the current node.
In the end, compare between the leftDepth+rightDepth and maximum depth, return the biggger one.
The reason for having a global maximum is because we could have a long diameter not passing through the root.
 */
class Solution {
public:
  int diameterOfBinaryTree(TreeNode* root) {
    if(!root) return 0;
    int maxDepth = 0;//global variable that tracks the maximum diameter so far
    int left = getMaxDepth(root->left,maxDepth);//get left depth
    int right= getMaxDepth(root->right,maxDepth);//get right depth
    return max(maxDepth,left+right);//return the max - eighet through root, or not through root
  }

  int getMaxDepth(TreeNode*node,int &maxDepth) {
    if(!node) return 0;
    int leftDepth  = getMaxDepth(node->left ,maxDepth);//post order traversal while tracking the max depth
    int rightDepth = getMaxDepth(node->right,maxDepth);//same
    maxDepth = max(maxDepth,leftDepth+rightDepth);//update maxDepth encountered from bottom up 
    return max(leftDepth,rightDepth)+1;//the depth of current node is always 1+deeper side
  }
  
};

