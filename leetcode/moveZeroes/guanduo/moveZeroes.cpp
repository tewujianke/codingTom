/*
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
*/

#include <iostream>
#include <vector>
/*
modify the array in place.
Iterate through the array. If equal to zero, skip incrementing the tracking index.
After the entire iteration, assign 0 to all the indices that is covered by the difference between tracking index and size.
 */

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
      int track = 0;//this guy will increment if not 0. Will skip incrementing if 0

      for(int i=0;i<nums.size();i++)
	if (nums[i] != 0)  nums[track++] = nums[i]; //increment track if non-zero

      while(track<nums.size())//add all the zeroes
	nums[track++] = 0;
    }
};
