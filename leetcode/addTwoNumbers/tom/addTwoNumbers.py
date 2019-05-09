"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


"""

"""

idea : we just use two pointer and keep track each digit and to check if we need to carry one 
to the next digit

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1                          ### variable p1 p2 are pointer to current node
        p2 = l2     
        head = None                      ### head is permanent head
        tmpHead = None                   ### tmpHead is the node which we processed recently
        plusOne = 0                      ### plusOne is to check if we have carried one from previous digit
        while p1 or p2 :
            if p1 and p2 :
                sumVal = 0
                if plusOne == 0 :                          ### when p1 and p2 are not empty
                    sumVal = p1.val + p2.val               ### if plusOne == 0, it means we dont have carried one
                else :
                    sumVal = p1.val + p2.val + 1            
                if sumVal >= 10 :                          ### if sum >= 10, it means we need to carry one to next node
                    plusOne = 1
                else :
                    plusOne = 0
                if not head :                              ### if head is empty, it is the first node 
                    head = ListNode(sumVal % 10)
                    tmpHead = head
                else :
                    tmpHead.next = ListNode(sumVal % 10)  
                    tmpHead = tmpHead.next
                p1 = p1.next
                p2 = p2.next
            elif p1 and not p2 :
                sumVal = 0                 ### basically same as above
                if plusOne == 0 :             
                    tmpHead.next = p1      ### this situation can help the run time
                    break                  ### if we dont have carried one, we can directly connect the rest of the list 
                else :                     ### and return it
                    sumVal = p1.val + 1
                    if sumVal >= 10 :
                        plusOne = 1
                    else :
                        plusOne = 0    
                tmpHead.next = ListNode(sumVal % 10) 
                tmpHead = tmpHead.next
                p1 = p1.next
            elif p2 and not p1 :
                sumVal = 0
                if plusOne == 0 :
                    tmpHead.next = p2
                    break
                else :
                    sumVal = p2.val + 1
                    if sumVal >= 10 :
                        plusOne = 1
                    else :
                        plusOne = 0    
                tmpHead.next = ListNode(sumVal % 10)
                tmpHead = tmpHead.next
                p2 = p2.next
        if plusOne == 1 :              ### finally, we need to check if we need to add another digit 
            tmpHead.next = ListNode(1)
            tmpHead = tmpHead.next
        return head
