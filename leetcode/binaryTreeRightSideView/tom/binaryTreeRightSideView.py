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

"""
idea :
we can consider "from right side of the tree" as last element of each level.
Therefore, we can use BFS to find the last element of each level

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root :
            return
        tmp = [root,'|'] ### we use '|' to mark that level ends
        while tmp :
            node = tmp.pop(0)
            if node == '|' :  ### if we encounter '|', it means we are gonna start to do the next level.
                if len(tmp) != 0 :
                    tmp.append('|')
            else :
                if tmp[0] == '|' :   ### if tmp[0] is '|', it means this is last element for current level
                    ans.append(node.val)
                if node.left :
                    tmp.append(node.left)
                if node.right :
                    tmp.append(node.right)
        return ans
