"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list


"""

"""

basic idea : we just go through the linked list and create every node,
and store the corresponding node to the hashTable.

Then, we just go through the list and  connnect the random pointer to the corresponding node 


"""



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        memo = {}
        first = 1
        tmp = head
        newHead = None
        newTmp = None
        while tmp :                ### just go throght the list and create every node 
            if first == 1 :
                first += 1
                newHead = Node(tmp.val,None,None)
                newTmp = newHead
                memo[tmp] = newTmp
                tmp = tmp.next
                continue
            else :
                newTmp.next = Node(tmp.val,None,None)
                newTmp = newTmp.next
                memo[tmp] = newTmp
                tmp = tmp.next

        tmp = head
        newTmp = newHead
        while tmp : ### go through the list again, and connect the random pointer
            if tmp.random :
                newTmp.random = memo[tmp.random]
            else :
                newTmp.random = None
            newTmp = newTmp.next
            tmp = tmp.next
        return (newHead)


