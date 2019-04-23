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

"""

idea : 

we can see the flatten tree is preorder traversal 

To achieve the order, we need to use postorder traversal to deal with this problem without using any other data structure.

if we go left child, we need to return the node which is leftmost. if we go right child, we need to return the node which is last one node after we attch it to the left child.



"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def helper(node) :
            leftEnd = None 
            rightEnd = None
            if not node.left and not node.right:
                return node
            if node.left :
                leftEnd = helper(node.left)
            if node.right :
                rightEnd = helper(node.right)

            if leftEnd  :                   ### if we found the leftEnd, we attach the right subtree to the leftend
                leftEnd.left = node.right
                node.right = None
            else :                          ### if we didnt find the leftEnd, it means the left node is None. we still attach right subtree to the left node.
                node.left = node.right
                node.right = None
            if rightEnd :                  
                return rightEnd  
            else :                         ### if we didn't find the rightEnd, it means we didnt attach anything to the leftEnd.
                return leftEnd             ### so we can directly return leftEnd.

                       
        if not root :
            return []
        else :
            helper(root)
                        ### the root is linked list but it is not right child link list. 
        tmp = root
        while tmp :     ### we just change left to right.
            tmp.right = tmp.left
            tmp.left = None 
            tmp = tmp.right
        return (root)
