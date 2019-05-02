"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
See C++ version for stack solution

Using inorder dfs in the constructor. Store the numbers in order in a deque

"""
from collections import deque

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodesInOrder = deque() #use deque for fast operations on both ends

        def dfsInOrder(node,result): #DFS in order
            if not node: return
            dfsInOrder(node.left,result)
            result.append(node.val)
            dfsInOrder(node.right,result)
        dfsInOrder(root,self.nodesInOrder)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.nodesInOrder.popleft() #pop from left
       


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.nodesInOrder)!=0 #return false when deque is empty


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
