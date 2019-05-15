"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Follow up:

Can you solve it using O(1) (i.e. constant) memory?

"""


"""
basic idea :
we use two pointer to track the whole list. one point is faster. If the linked list is cycle, 
the fast one will catch up with the slow one.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fastPt = head
        slowPt = head
        first = 1
        while fastPt != None and fastPt.next != None and fastPt.next.next != None :
            if first == 1 :     # first time run, just skip the compare step.
                first += 1
            else :
                if slowPt is fastPt :
                    return True
            slowPt = slowPt.next
            fastPt = fastPt.next.next   
        return False     ### if fast point encounter None, it means the linked list does not have cycle.
