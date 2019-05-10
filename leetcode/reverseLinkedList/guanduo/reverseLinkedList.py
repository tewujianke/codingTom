"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
Same Idea as iteration. 
Each recursion call extracts the next node, then pass to the recursive call.
If reaching None, return previsou node
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(node,prev):
            if not node: return prev             #reaching the end, return the last node, which will be the new head
            next_node,node.next = node.next,prev #extract the original next node, continue passing 
            return reverse(next_node,node)
        return reverse(head,None)
