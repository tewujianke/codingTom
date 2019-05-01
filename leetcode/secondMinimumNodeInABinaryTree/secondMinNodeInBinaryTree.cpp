/*
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
 

Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
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
Using DFS. Stop when seeing a node with val bigger than root.val.
Three cases:
1. Both children are null. return -1 (not found)
2. One of choldren is null. return the other one
3. both children have valid value. return the smaller one, which ensures the second minimum

Note that we can't stop when seeing the first node with value bigger than root, since there might be a smaller one on the other subtree.
 */
class Solution {
public:
  int findSecondMinimumValue(TreeNode* root) {
    if(!root) return -1;
    return helper(root,root->val);//create helper function for the extra argument
  }
  
  int helper(TreeNode*root, int rootVal) {//second argument will always carry the root's value
    if(!root) return -1; //impossible case based on problem description. jsut leave it here
    if(!root->left && !root->right && root->val > rootVal) return root->val;//return current subtree immediately when seeing the first node with val bigger than root
    int left = helper(root->left,rootVal);//get left side
    int right = helper(root->right,rootVal);//get right side
    if(left==-1&&right==-1) return -1;//return not found when both -1
    if(left==-1) return right;//return one of the other when found an at least bigger node
    else if(right==-1) return left;
    else return min(left,right);//if both chilren give values, always pick the smaller one to ensure the second minimum property
  }
};
