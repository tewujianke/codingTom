/*
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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
Stupid problem. 
 */
class Solution {
public:
  ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode *head;
    ListNode *result;
    if(!l2) {//return directly if one list is empty
      head = l1;
      return head;
    }
    if(!l1) {//return directly if one list is empty
      head = l2;
      return head;
    }
    if (l1->val <= l2->val) {//construct the list based on order
      head = l1;
      l1 = l1->next;
    } else {
      head = l2;
      l2 = l2->next;
    }
    result = head;
    
    while (l1!=NULL || l2!=NULL) {//continue constucting the LL until all NULL
      if (l1==NULL) {
	head->next = l2;
	return result;
      }
      if(l2==NULL){
	head->next = l1;
	return result;
      }
      if(l1->val <= l2->val) {
	head->next = l1;
	l1 = l1->next;
	head = head->next;
      } else {
	head->next = l2;
	l2 = l2->next;
	head = head->next;
      }
    }
  

  }
};
