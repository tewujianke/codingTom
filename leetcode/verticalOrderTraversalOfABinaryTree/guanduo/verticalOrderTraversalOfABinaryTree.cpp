/*
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.



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
#include <map>
#include <algorithm>
#include <utility>
using namespace std;

/*

Setup a hash map. The index is X. The value is an array of pairs, whose first element is Y, and
second element is the value of the node.

traverse the tree and populate the hash map.
For each hash[X], we sort the array of pairs based on the first element (Y).
If two nodes have exact same coordinates (X,Y), we sort them based on the node value.

 */
class Solution {
private:
  //map[X] -> pair(Y,node->val)
  map<int,vector<pair<int,int> >> mem;

  //static comp function to help sort the array of same vertical line for std::sort
  //must be static function for std::sort and non-ref type for stable_sort
  static bool comp(pair<int,int>a,pair<int,int>b) {
    if(a.first==b.first) return a.second<b.second;    //if same coordinate, sort the array based on node
    return a.first<b.first;                           //else, sort the array based on Y
  }
public:
  vector<vector<int>> verticalTraversal(TreeNode* root) {
    vector<vector<int>> result;
    if (root == NULL) return result;
    findAll(root,0,0);                //populate the hash map. Root coordinates (X,Y) = (0,0)
    for (auto i:mem) {                //go through each vertical line (X), sort the array based on the function above
      vector<int> vertical;
      std::stable_sort(i.second.begin(),i.second.end(),comp);
      for (auto j:i.second)           //go through the sorted array and extract the node value, and push to vector
	vertical.push_back(j.second);
      result.push_back(vertical);
    }
    return result;
  }
  void findAll(TreeNode* node,int x, int y) {
    if(node == NULL) return;
    findAll(node->left,x-1,y+1);      //recursive DFS to populate the hash map. Change coordinates based on problem
    pair<int,int> cur(y,node->val);   //create pair (Y,node->val)
    mem[x].push_back(cur);
    findAll(node->right,x+1,y+1);     //Change coordinates based on problem
  }
  
};
