/*
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
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
#include <iostream>
#include <stack>

/*
The problem is basically to traverse the binary search tree (in order) using non-recursion. 
A stack is the typical way of doing this.
 */
class BSTIterator {
private:
  stack<TreeNode*> stk;
  
public:
  BSTIterator(TreeNode* root) {
    while(root) {//initilize stack to push all the way to the left most node (smallest value in the tree)
      stk.push(root);
      root = root->left;
    }
  }
    
  /** @return the next smallest number */
  int next() {
    auto curNode = stk.top();//get the top
    stk.pop();//deleete the top
    if(curNode->right) {//if there is a right child, go right, then all the way to the left
      auto n = curNode->right;
      while (n) {
	stk.push(n);
	n = n->left;
      }
    }
    return curNode->val;
  }    
    
  /** @return whether we have a next smallest number */
  bool hasNext() {
    return stk.size() != 0; //straightforward
  }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
