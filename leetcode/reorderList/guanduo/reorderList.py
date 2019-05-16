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
I considered using dict to solve, but it doesn't utilize linked list property. So quit it

Try to solve directly using linked list property.
The idea is to split the linked list, the later half needs be be reversed, then we assign a pointer pointing to the reversed latter half.
Then we could combine two linked list into one in turn from the two linked list
"""
class Solution(object):
    def reorderList(self, head):
        """
        get the length of a linked list as we have to know how long the linked list is so get the second know (last one)
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
        return the head of nth node,used to get the starting node of the latter half
        """
        def getNthNode(head,n):
            if not n: return head
            return getNthNode(head.next,n-1)

        if not head: return head                      #empty list
        length = getLength_ll(head)+1                 #calculate the total length
        lower_index = length//2                       #plus 1 divided by 2 gives the starting index of the latter half
        lower_head = getNthNode(head,lower_index)     #get a pointer to the starting node of latter half

        Nhead = reverse_LL(lower_head)                #reverse the latter linked list and return the new head (tail of original list)

        cur = head                                    #save the head to return at last
        tail = 0                                      #used as a toggle to know which node to pick in turn from the two lists
        tmp = cur.next                                #tmp variable stores the next node of the first list (latter half no need to store)

        while cur:
            tail ^= 1                                 #change toggle to pick a node in turn 
            if tail:                                  #pick from latter list
                cur.next = Nhead
                Nhead = None if not Nhead else Nhead.next #special case for empty latter list since the latter list always has less nodes than former list
            else:
                cur.next = tmp                        #grab the prveviously saved node
                tmp = tmp.next
            cur = cur.next
        return head
