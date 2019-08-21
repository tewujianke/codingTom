/*
  Given a collection of distinct integers, return all possible permutations.

  Example:

  Input: [1,2,3]
  Output:
  [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
  ]

*/

/*
Use backtracking to exhaustively get all permutations.
Use an extra array (visited) to mark the current number that is already in the result.
 */
#include <iostream>
#include <vector>
class Solution {
private:
  void helper(vector<int>&nums, vector<int>&tmp, vector<bool>&visited,vector<vector<int>>&result) {
    if(tmp.size() == nums.size()){  //the exit condition is - we've reached the same number of elements
      result.push_back(tmp);
      return;
    }

    for(int i=0;i<nums.size();i++) {
      if (visited[i]) continue;     //if current number is already in the array, skip it
      tmp.push_back(nums[i]);       //push next number
      visited[i] = true;            //record the index. so it won't be pushed again
      helper(nums,tmp,visited,result);
      tmp.pop_back();               //backtracking
      visited[i] = false;           //backtracking recording 
    }
  }
public:
  vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> result;
    vector<bool> visited;      //extra array of booleans to track which number has been pushed to current result
    for(int i=0;i<nums.size();i++)
      visited.push_back(false); //init the array to all false
    vector<int>tmp;
    helper(nums,tmp,visited,result);
    return result;
  }
};
