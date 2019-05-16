"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
I considered using dict to solve, but it doesn't utilize linked list property and it has very low efficiency

Try to solve directly using linked list property. The idea is to split the linked list, the later half needs be be reversed.
Then we could combine two linked list into one in turn from the two linked list
"""
class Solution(object):
    def reorderList(self, head):
        """
        get the length of a linked list
        """
        def getLength_ll(head):
            leng = 0
            while head:
                leng+=1
                head = head.next
            return leng
        """
        reverse a linked list and return the new head (the original tail)
        """
        def reverse_LL(head,last=None):      #return the new head (the tail of original list)
            #1->2->3->4->None
            if not head:
                return last
            tmp = head.next
            head.next = last
            return reverse_LL(tmp,head)

        """
        return the head of nth node
        """
        def getNthNode(head,n):
            if not n: return head
            return getNthNode(head.next,n-1)
            
        if not head: return head
        length = getLength_ll(head)+1
        lower_index //= 2
        lower_head = getNthNode(head,lower_index)
        Nhead = reverse_LL(lower_head)
        """
        1->2->3->4->5
        
        5->4->none

        reverseH = 3
        reverseT = None
        1->5->2->4->3
        """
        tmp0 = 
        
