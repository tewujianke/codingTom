"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
post-order traversal is needed since we need to swap lowest nodes first without affecting the topology.
when both children are present, recursively move right children to the left subtree's end on the right. Then move left child to right. Then assign None to the left.

When only right child is present, do nothing.
When only left child is present, move to the right
"""
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
      
        if not root or (not root.left and not root.right): return root#return null or current node if bottom node
        left_node = self.flatten(root.left) #get left node. (recursion post-order)
        right_node = self.flatten(root.right)#get right node.
        if left_node: #if there is left node, move right node to the bottom of the left node on the right.
            self.assign_right2left(left_node,right_node)#call helper function to achieve above functionality
            root.right = left_node#swap nodes
            root.left = None#invalidate left node
        return root
    def assign_right2left(self,left,right):
        while left.right:#whiile not bottom, keep going right
            left = left.right
        left.right = right
        
