/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

/*
  Iterate through the array. Record the number. If a complement exists, return the vector
*/

#include <unordered_map>
#include <vector>

class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int,int> mem; //hash table that stores value as we go
    vector<int> result;//as the result array
    
    for(int i=0;i<nums.size();i++) {//iterator through the array
      if(mem.count(target-nums[i])) {//if an existed complement, push to the array
	result.push_back(mem[target-nums[i]]);
	result.push_back(i);
      }
      mem[nums[i]] = i;//otherwise record the element
    }
    return result;

  }
};
