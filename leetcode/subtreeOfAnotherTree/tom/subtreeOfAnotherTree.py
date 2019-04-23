"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

"""


"""
idea :

First, we use Depth First Search to collect all node from bottom to above.

After that, we start to check if that t is the subtree of current node.

if t.val == node.val, we keep compare t's children with node's children

if t.val != node.val, we stop comparing and switching to next node.

"""





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        tmpNode = []
        def helper(node1,node2) :
            if not node1 or not node2 :
                if not node1 and not node2 :
                    return True
                else :
                    return False
            if node1.val == node2.val :
                return helper(node1.left,node2.left) and helper(node1.right,node2.right)
            else :
                return False

        def DFSTrack(node) :
            if not node :
                return
            else :
                DFSTrack(node.left)
                DFSTrack(node.right)
                tmpNode.append(node)
        DFSTrack(s)
        for node in tmpNode :
            if helper(node,t) :
                return True
            else :
                continue
        return False
