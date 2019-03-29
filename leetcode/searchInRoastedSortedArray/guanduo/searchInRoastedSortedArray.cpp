/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
*/

/*
Optimize for performance -

 Change the way of solving the problem to optimize the performance.
 The goal is to get rid of the second binary search for the pivot point.
 
 1. Compare the mid point with the first element. If bigger than it, it means the left subarray is sorted.
    If target is smaller than the first element (which is smallest on the left), it means we must to right
    Otherwise, the target could be on the left or on the right. e.g. 4,5,6,7,8,9,10,11, target could be 6 or 10
    In this case we need one more comparision with mid to determine whether the target is on the left or right
 2. If mid point is smaller than the first element, it means the right subarray is sorted
    Comopare the target with the rightmost element (biggest on the right). If bigger, then we must go left
    Otherwise, the target could be on the left or on the right. In this case we need one more comparison to determine left or right
 3. be ware of exit condition! Easy to forget [1,2] cases where mid is equal to the left or right case.
 */

class Solution {
public:
  int search(vector<int>& nums, int target) {
    int size = nums.size(); 
    if(size == 0 ) return -1;//corner case: when empty nums, return -1 like a loser
    int low = 0; int high = size -1; //get lower bound and upper bound. ready for binary search

    while (low <= high) { //exit condition when lower bound and upper bound crosses
      int mid = (low+high)/2; //get the middle point

      if(nums[mid] == target) return mid; //exit since we 've found the match!!!

      if(nums[mid] >= nums[low]) { //left array is sorted case
	if(target < nums[low] ) {//the target is on the right since it is smaller than the smallest number on the left
	  low = mid+1;
	}
	else { //is target is bigger, it could be on left array or on the right array
	  if(target < nums[mid]) high = mid-1; //determine whether target is on the left or right
	  else low = mid +1;
	}
      } else { //right array is sorted
	if (target < nums[mid]) { //since target is smaller than the smallest number in the sorted array, the target must be on the left
	  high = mid - 1;
	} else { //otherwise, it depends on the big one. //determine whether target is on the left or right
	  if(target <= nums[high]) {
	    low = mid+1;
	  } else {
	    high = mid-1;
	  }
	}
      }
      
    }
    return -1; //never found the match. return like a loser
    
  }
};
