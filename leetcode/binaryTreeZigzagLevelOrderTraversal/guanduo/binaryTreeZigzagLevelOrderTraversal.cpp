/*
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
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
#include <deque>
#include <vector>
using namespace std;


class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
      deque<TreeNode*>* currentLevel = new deque<TreeNode*>;
      deque<TreeNode*>* nextLevel = new deque<TreeNode*>;
      vector<vector<int>> result;

      if (!root) return result;
      
      if(root) {
	nextLevel.push_back(root);
      }
      bool left2right = false;

      while(currentLevel.size() || nextLevel.size()) {
	if(!currentLevel.size() && nextLevel.size()) {
	  auto tmp = currentLevel;
	  currentLevel = nextLevel;
	  nextLevel = tmp;
	  left2right = !left2right;
	  continue
	}
	
      }
    }
};
