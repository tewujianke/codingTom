"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
 """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Use pre-order DFS but always go right first.
One trick to use: we track the current depth and the number of result array element.
Each level can only have one (right most) node. If the size of list is smaller than depth, we push. Otherwise, skip
"""
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preOrderDFS_rightFirst(node,result,depth):
            if not node: return #reached end or empty root
            if len(result)<depth: #the size of result reflects whether current level has a node viewed to the right
                result.append(node.val)
            preOrderDFS_rightFirst(node.right,result,depth+1) #go right first
            preOrderDFS_rightFirst(node.left ,result,depth+1)
            
        result = list()
        preOrderDFS_rightFirst(root,result,1)
        return result
