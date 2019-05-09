"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


"""



"""

idea : use two pointer to compare which one is bigger.
       After that, just switch the node's next pointer

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2 :   ### when both lists are empty, return empty
            return
        elif not l1 and l2 :     ### if one of them is empty, just return other one
            return l2
        elif not l2 and l1 :
            return l1
        else :
            tmp = ""
            first = 1
            p1, p2 = l1, l2
            while p1 or p2 :
                if first == 1 :             ### find the first element, and move the pointer to next node
                    first += 1              ### variable tmp is current node
                    if l1.val <= l2.val :
                        tmp = l1
                        p1 = p1.next
                    else :
                        tmp = l2
                        p2 = p2.next
                if p1 and p2 :             ### if both are not empty, we start to compare their value
                    if p1.val <= p2.val :
                        tmp.next = p1      ### we move the pointer based on their value
                        p1 = p1.next
                        tmp = tmp.next
                    else :
                        tmp.next = p2
                        p2 = p2.next
                        tmp = tmp.next
                else :
                    if not p1 :          ### if one of them are already none, it means we just need to move
                        tmp.next = p2    ### the current node's next to the rest of the list
                    else :
                        tmp.next = p1
                    break
        if l1.val <= l2.val :    ###  finally, return the overall head node
            return l1
        else :
            return l2
