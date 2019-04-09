/*Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

  */

 /* idea is to sort the array. Iterate through each element, 
    for each element, having two pointers pointing to the current elemtn +1 and the last element in the array.
    if the sum of three numbers == 0, push back
    if the sum is bigger than 0, we need to reduce the bigger number (by left shifting the right pointer)
    if the sum is smaller than 0, we need to enhance the smaller number (by right shifting the left pointer)
    (since we have sorted the array)

    COrner case: [0,0,0,0] - if the current iterated elemetn is the same as the previous element, no need to redo the process
                           - for the left pointer, if we push back to the result, and the next number is the same, no need to redo the process

  */
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
      vector<vector<int>> result;//result array (2d)
      if (nums.size()<3) return result;//not valid case

      std::sort(nums.begin(),nums.end());//need to sort the array, so we know whatever on the left is smaller or equal, same for right
      for(int i=0;i<nums.size()-2;i++) {//iterate through the array. No need to cover teh last two elements
	if(i!=0 && nums[i]==nums[i-1]) continue; //if current number is the same as previous one, no need to re do process
	int j = i+1;//left pointer 1 bigger than current number
	int k = nums.size()-1;//right pointer starting from the end
	while (j!=k) { //exit conditino - when two pointers cross
	  int tmp = nums[j]+nums[i]+nums[k]; //calculate the sum
	  if (tmp == 0) {//got an answer. push back
	    result.push_back({nums[i],nums[j],nums[k]});
	    ++j;
	    while(nums[j-1]==nums[j] && j!=k) ++j;//corner case - [0,0,0,0]. If the left pointer moves to the next number, which is the same as the previous number, no need to redo the process
	  }
	  else if(tmp > 0) --k;//if current sum is bigger than 0, we lower the upper ceiling
	  else ++j; // if the current sum is smaller than 0, we raise the lower floor
	}
      }
      return result;
    }
};

int main() {

  Solution sol;

  vector<int> arr = {0,0,0};

  vector<vector<int>> re;

  re = sol.threeSum(arr);
  return 0;
}
