"""

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


"""

"""
we use DSF to traverse every node and then we plus its left deepest node and its right deepest node

then find out the longest one.

after that, we just return the longest depth to its parent. 

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0 
        def helper(node) :
            if not node :  #### if we encounter leaf node, None, we just return 0
                return 0
            left = helper(node.left)     ### we found out the left deepest length
            right = helper(node.right)   ### and right.    
            self.longest = max(left+ right,self.longest)  ### we check if the longest length is still the longest one
            return max(left,right) + 1
        helper(root)
        return (self.longest)
