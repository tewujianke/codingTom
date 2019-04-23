"""

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.



"""

"""
idea :

we use recursive function to check each node to make sure its left child should be smaller than the node, and its right child should be larger than the node.

In addition, every node has its maximum and minimum value. if the value of left child or right child are out of that range.

It would not be a valid BST.



"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node,largest,smallest) :
            if not node  :
                return True
            else :
                if node.left :
                    if not (node.left.val < node.val and node.left.val > smallest) :
                        return False    
                if node.right :
                    if not (node.right.val > node.val and node.right.val < largest) :
                        return False
                return helper(node.left,node.val,smallest) and helper(node.right,largest,node.val)   ### if we go left, we need to update the largest value to current val. On the other hand, if we go right, we need to update the smallest value to current val.
        return (helper(root,float('inf'),float('-inf')))
