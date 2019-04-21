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

/
#include <deque>
#include <vector>
using namespace std;

/*
The idea is to use two deque (actually two pointers of deque). When iterating current level,
push the node's children to the nextLevel deque. Each time we pop one item from currentLevel, until empty, 
then swap the pointers - the nextLevel will be currentLevel, and the empty currentLevel will be the new next level.
Keep doing until the end of the tree.
Using a flag (left2right) to determine whehter left child or right child to be pushed onto the nextLevel deque
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
      //declare two deque pointers (using pointers are more efficient than swapping the entire deque elements
      deque<TreeNode*>* currentLevel = new deque<TreeNode*>;
      deque<TreeNode*>* nextLevel = new deque<TreeNode*>;
      vector<vector<int>> result;

      if (!root) return result;//empty tree. return directly
      
      //push the root to the nextLevel deque. So currentLevel will be empty, and will be swapped in the first iteration
      if(root) {
	nextLevel->push_back(root);
      }
      bool left2right = false;//the second level would be right to left. Thus initialized to false

      //as long as either deque has something in it, we keep going
      while(currentLevel->size() || nextLevel->size()) {
	//when currentLevel is exausted, meaning we need to swap the two pointers for the next level
	//the reason is we want to push all nodes in the same level as a vector
	if(!currentLevel->size() && nextLevel->size()) {
	  vector<int> curResult;
	  for(auto i:*nextLevel) curResult.push_back(i->val);//fetch all nodes for the next level, push to a vector of final result
	  result.push_back(curResult);
	  //now we swap the two deque. The current deque will be used as the future nextLevel, and the current
	  //nextLevel will become current level
	  auto tmp = currentLevel;
	  currentLevel = nextLevel;
	  nextLevel = tmp;
	  left2right = !left2right;//change the order for next level
	  continue;//need to continue since there is nothing on previous level!
	}
	TreeNode* cur = currentLevel->front();//grab the first node
	currentLevel->pop_front();
	
	if(left2right) {//if going from left to right, we push the left child first
	  if(cur->left) nextLevel->push_front(cur->left);
	  if(cur->right)nextLevel->push_front(cur->right);
	} else {//if going from right to left, we push the right child first
	  if(cur->right) nextLevel->push_front(cur->right);
	  if(cur->left)nextLevel->push_front(cur->left);
	}
	
      }
      return result;
    }
};
