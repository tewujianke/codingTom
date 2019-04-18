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
        
        def recursive(node,isRoot,maxVal,root,isRight,isLeft) :
            if len(preorder) == 0 :
                return
            if preorder[0] < node.val :
                node.left = TreeNode(preorder[0])
                preorder.pop(0)
                if isRoot == 1 :
                    recursive(node.left,0,node.val,root,0,1)
                else : 
                    recursive(node.left,0,node.val,root,0,isLeft)   
                    
            if len(preorder) == 0 :
                    return
            if maxVal < preorder[0] and isRoot != 1 :
                if isRight != 1:
                    return   
            if isLeft == 1 and root.val < preorder[0] :
                return 
            if isLeft == 1 and maxVal < preorder[0] :
                return

            if preorder[0] > node.val :
                node.right = TreeNode(preorder[0])
                preorder.pop(0)
                if isRoot == 1:
                    recursive(node.right,0,node.val,root,1,0)
                else :
                    recursive(node.right,0,max(node.val,maxVal),root,isRight,isLeft)
                   
        root = TreeNode(preorder.pop(0))
        recursive(root,1,root.val,root,0,0)
        return root
                
