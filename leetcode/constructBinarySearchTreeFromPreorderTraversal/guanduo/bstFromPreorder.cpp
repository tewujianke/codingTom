/*
  Return the root node of a binary search tree that matches the given preorder traversal.

  (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

  Example 1:

  Input: [8,5,1,7,10,12]
  Output: [8,5,10,1,7,null,12]

 

  Note: 

  1 <= preorder.length <= 100
  The values of preorder are distinct.
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
The idea is to create a root node, then iterate through the array -> 
recursively go left if the number is smaller than current node's val
or recursively go right if the number is equal or bigger than current node's val
 */
class Solution {
public:
  TreeNode* bstFromPreorder(vector<int>& preorder) {
    if(preorder.size()==0) return NULL;//empty input, no node created
    TreeNode* root = new TreeNode(preorder[0]);//create the root first
    for(int i=1;i<preorder.size();i++) {//start from the second number
      createNode(preorder[i],root);//calling the function to start tranversing
    }
    return root;
  }

  void createNode(int v,TreeNode* curNode) {
    if(v<curNode->val) {//if v is smaller, go left
      if(curNode->left) createNode(v,curNode->left); //there is a left child. keep going left
      else curNode->left = new TreeNode(v);//no left child. create the new node with the value
    } else {
      if(curNode->right) createNode(v,curNode->right);//there is a right child. keep going right
      else curNode->right = new TreeNode(v);//no right child. create the new node with the value
    }
  }
};
