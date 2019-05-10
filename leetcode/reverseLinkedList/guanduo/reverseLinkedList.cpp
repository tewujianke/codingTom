/*
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
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
Using Iteration to reverse a linked list.
See python version for the recursive way.
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
      ListNode* prev = NULL; //stores the previous node, since the current node's next will be assigned to the previous one
      ListNode* after;      //store the original next node, since we still iterate through the LL in the original direction

      while(head) {         //while there are still more nodes
	after = head->next; //store the original next node first
	head->next = prev;  //reverse the current node direction
	prev = head;        //store current node as previous node for the next node's reverse operation
	head = after;       //move the current node to the next node (in the original direction)
      }
      return prev;          //since head is NULL now.
    }
};
