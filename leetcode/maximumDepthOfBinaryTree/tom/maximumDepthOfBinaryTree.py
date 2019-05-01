"""

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


"""
"""

idea : Use DFS to traverse the the tree, and return the maximum value




"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node,depth) :
            if not node :  ### leaf node will be None.  we return the depth 
                return depth  
            else :
                leftChild = helper(node.left,depth+1)   
                rightChild = helper(node.right,depth+1)
            return max(leftChild,rightChild)
        return helper(root,0)
