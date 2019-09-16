"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
This is by nature mergeSort. Use two pointer algorithm to find the middle node, then break the list. recursively do so until single node
Then recursively sort & merge from smallest list to the whole list.
"""
class Solution(object):
    #Recursion does not use constant space. Just for a simpler implementation
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #split a linked list into two, return the second half head
        
        #merge two linked list into one, sorted
        def merge(l,r):
            cur = ListNode(0)
            head = cur
            while l and r:
                if l.val <= r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            if l:
                cur.next = l
            if r:
                cur.next = r
            return head.next
                    
        def mergeSort(head):
            if not head or not head.next: return head
            slow = head
            fast = head
            lst  = head  #need another pointer to break the link between the two splitted lists.
            while fast and fast.next: #make sure fast can jump two. this would return either mid one or second half
                lst = slow
                fast = fast.next.next
                slow = slow.next
            lst.next = None
            return merge(mergeSort(head),mergeSort(slow))

        
        
        return mergeSort(head)
