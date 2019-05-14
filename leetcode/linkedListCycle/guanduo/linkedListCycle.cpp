/*
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


/*
Using two pointers. Regular pointer and fast_pointer.
while fast_pointer is not null, each time fast_pointer proceeds two nodes, but regular pointer proceeds one node.
For any operations (either fast_ptr move or regular ptr move)  we need to check for NULL and Equal.
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
      if(!head) return false;              //empty list. non cyclc
      ListNode* fast_ptr = head->next;     //initialize fast_ptr to the next one directly

      while(fast_ptr) {                    //use fast_ptr for exit check as it will reach to the end (non-cyclic) first.
	if (fast_ptr==head) return true;   //catch up. cyclic
	fast_ptr = fast_ptr->next;         //move fast_ptr first time
	if (!fast_ptr) break;              //non cyclic case
	if (fast_ptr==head) return true;   //catch up. cyclic
	fast_ptr = fast_ptr->next;         //move fast_ptr second time
	head = head->next;                 //move regular ptr
      }
      return false;
    }
};
