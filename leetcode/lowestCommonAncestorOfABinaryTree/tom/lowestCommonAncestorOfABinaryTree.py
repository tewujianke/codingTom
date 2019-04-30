"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
idea : we go throught the whole tree and use hash_map to record every node's parent

After that we start trace back from node p to the root, and mark every node as visited.

we trace again from node g to the root, and if we encounter any node which is already marked as visited

That will be lowest common ancestor.


"""




class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        memo = {}
        visited = {}
        def helper(parent,child) :
            if not child :
                return
            else :
                if parent :
                    memo[child.val] = parent
                else :
                    memo[child.val] = None
                visited[child.val] = 0
            helper(child,child.left)
            helper(child,child.right)

        helper(None,root)
        tmp = p
        while tmp :                           ## first time trace node p to the root
            visited[tmp.val] = 1
            tmp = memo[tmp.val]        
        tmp = q
        while tmp :                           ### trace node q to the root
            if visited[tmp.val] == 1 :
                return tmp
            else :
                visited[tmp.val] = 1
            tmp = memo[tmp.val]
