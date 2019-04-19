/*
  Given a set of distinct integers, nums, return all possible subsets (the power set).

  Note: The solution set must not contain duplicate subsets.

  Example:

  Input: nums = [1,2,3]
  Output:
  [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
  ]
*/


/*
Use Backtracking to solve.
Iterate through the array. Push back current element, then push back to the final result right away.
Recursively call the function with index+1.
pop back the last element once the iteration is done.

 */
class Solution {
public:
  vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> result;//final result
    vector<int> cur;//used for backtracking operation
    result.push_back(cur);//push back the empty set
    helper(result,nums,cur);//start backtracking
    return result;
  }

  void helper(vector<vector<int>>&result,vector<int>&nums,vector<int>&cur,int index=0) {
    for(int i=index;i<nums.size();i++) {//for each number
      cur.push_back(nums[i]);//push current number
      result.push_back(cur);//push current set to the final result array
      helper(result,nums,cur,i+1);//consider teh next number to be in the same set
      cur.pop_back();//pop the last number for backtracking 
    }
  }
  
};
