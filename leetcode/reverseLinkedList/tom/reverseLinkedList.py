"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmpPre = None            
        while head :
            tmpNext = head.next
            head.next = tmpPre
            tmpPre = head
            head = tmpNext
        return tmpPre

        ### below are recursive method

        """
        def reverseL(previousNode,node) :
            if node == None :           # this case is when there is only one node in the list 
                return previousNode
            if node.next == None :
                node.next = previousNode
                return node
            else :
                newHead = reverseL(node,node.next)  ### we need to keep the new head, so we just keep return it
                node.next = previousNode
                return newHead
        if head :
            firstNode = head
            ans = reverseL(head,head.next)
            firstNode.next = None
            return ans

        else :
            return None

