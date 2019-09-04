"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Recursive way: recursively reach the last element, then return 0.
For each node we trace backwards, return current level+1
When n is equal to the level, we assign previous' next to current's next
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def helper(cur,prev,n):
            if cur == None: #reached the last node
                return 0

            level = helper(cur.next,cur,n) + 1 #plus 1 for each node we return
            if level == n: #found the nth node from right
                if prev == None: return -1 #this means we are still at the first node. return a special number
                prev.next = cur.next #remove current node
            return level
            
        prev = None #initialize prev
        num = helper(head,prev,n) #if return -1, then we need to remove the first element, return next. This also covers the case when there is a single node in the linked-list
        return head if num != -1 else head.next
    
