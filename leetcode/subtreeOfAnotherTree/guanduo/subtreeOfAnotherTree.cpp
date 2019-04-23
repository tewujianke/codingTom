/*
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

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
Traverse the main tree. When found a node with the same value of the subtree root, trigger a preOrder comp function.
In the function, recursively compare between the two trees.
Hidden case: NULL must also match!
 */
class Solution {
public:
  bool isSubtree(TreeNode* s, TreeNode* t) {
    if(s==NULL && t!=NULL) return false;//return false for empty main tree
    if(s==NULL && t==NULL) return true; //return true when both NULL
    if (s->val == t->val) { //if a matching node found, trigger comparison recursively
      if(preOrderTraversalCompare(s,t)) return true; //return true directly when matching
    }
    bool left_match =  isSubtree(s->left,t);//otherwise go left
    bool right_match = isSubtree(s->right,t);//then go right
    return left_match || right_match; //found a match, return it. This could've been optimized since if left subtree match is found, we could return directly without looking at right subtree
      
  }
  bool preOrderTraversalCompare(TreeNode*s, TreeNode*t) {
    if((s==NULL&&t!=NULL) || (t==NULL && s!=NULL)) return false;//not match NULL
    if(s==NULL&&t==NULL) return true;//Matching NULL
    if(s->val!=t->val) return false;//Not matching value
    return preOrderTraversalCompare(s->left,t->left) && preOrderTraversalCompare(s->right,t->right);//both left and right cmp
  }
  
};
