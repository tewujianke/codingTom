"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""

"""

basic idea :

we need to connect the linked list to the last element and go back to the first element.
Therefore, we just put the node into array, and use two pointer to connect each node's next pointer.




"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head :
            return None
        arr_list = []
        tmpHead = head.next     ### we dont put the head to the array
        front = 0
        while tmpHead :         ### put each node in to array 
            arr_list.append(tmpHead)
            tmpHead = tmpHead.next
        currHead = head
        start = 0 
        end = len(arr_list) - 1
        while end - start != -1 :   ### just move two pointers to connect their next pointer
            if front == 0 :
                currHead.next = arr_list[end]
                front = 1
                end -= 1
            else :
                currHead.next = arr_list[start]
                front = 0
                start += 1
            currHead = currHead.next
        currHead.next = None
        return head
            
