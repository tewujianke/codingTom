"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Single pass. Use a temporary variable to store the carry (if any) and propagate to the next number (node).
"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #create the first node. return a node with val of 0 if empty on both lists
        cur = ListNode(0)
        head = cur #store the head as we iterate 
        carry = 0 #tmp variable that carrys the carry
        while l1 or l2 or carry: #don't miss the carry! The most significant number could still yield to a number > 9
            if l1:
                carry+=l1.val
                l1 = l1.next
            if l2:
                carry+=l2.val
                l2 = l2.next
            if carry>9: #if the current digits give a number 10+, create current node -10
                cur.next = ListNode(carry-10)
            else: #if the current digits give a number 9-, create the node directly
                cur.next = ListNode(carry)
            carry//=10 #get rid of the sum of current digit and only keep the carry (if any)
            cur = cur.next
        return head.next
