"""

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)



Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]



Note:

1 <= preorder.length <= 100
The values of preorder are distinct.


"""


"""
we use recursive method to create binary search tree.

Because the array is preorder traversal order

it is 
(
print 
leftTree
rightTree
)

we use the same order to implement the recursive function.

create the left element first, and then we go to its left subtree to create the left subtree again as long as the next element 
meet the criteria of binary search tree. If it does not meet the rule, we check how many level we should go back, and create right subTree.

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        def recursive(node,isRoot,maxVal,root,isRight) :
            if len(preorder) == 0 :
                return
            if preorder[0] < node.val :
                node.left = TreeNode(preorder[0])
                preorder.pop(0)
                if isRoot == 1 :
                    recursive(node.left,0,node.val,root,0)   ### everytime we create a left node, we remember the maximum value
                else : 
                    recursive(node.left,0,node.val,root,0)   
            if len(preorder) == 0 :
                    return
            if maxVal < preorder[0] and isRoot != 1 :    ####  this is the condition which we need to check and break to the correct subtree.
                if isRight != 1:                         ####  we also use isRight label to track most right hand side node.
                    return                               ####  if preorder[0] > maxVal, we dont need to check other things and directly create a right node as long as it is most right hand side path
            if preorder[0] > node.val :                            ####   create right node, and keep passing the maxVal until we switch to left node.
                node.right = TreeNode(preorder[0])
                preorder.pop(0)   
                if isRoot == 1:
                    recursive(node.right,0,node.val,root,1)
                else :
                    recursive(node.right,0,max(node.val,maxVal),root,isRight)
                   
        root = TreeNode(preorder.pop(0))
        recursive(root,1,root.val,root,0)
        return root
                
