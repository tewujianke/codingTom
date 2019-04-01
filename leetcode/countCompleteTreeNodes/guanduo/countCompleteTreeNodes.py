"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Basic Idea:
For current node - if depth of left equals to the depth of right, then we can safely say the number of nodes is pow(2,depth)-1
Otherwise, we need to dive into the node's left and right.
Since the tree is guarenteed to be a complete tree, we expect many small complete trees. This algorithm can safe time for nodes in between.

One way to optimize further is to use dynamic programming to memorize a node, so there won't be repetitive search. Will try in C++ version
"""
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leftD = self.checkLeft(root) #get the depth of left child
        rightD = self.checkRight(root) #get the depth of right child
        if leftD == rightD: #if proven to be a complete tree, then the number of nodes = 2^n -1
            return 2**leftD-1

        return self.countNodes(root.left)+self.countNodes(root.right)+1 #otherwise continue going down
        
    def checkLeft(self,node,depth=0):#initialize depth to 0
        if not node: return depth #if a node itself is none, don't add 1 to depth
        depth+=1 #one more valid level on the left
        if node.left == None:
            return depth
        return self.checkLeft(node.left,depth)#recursively calculate the depth
    def checkRight(self,node,depth=0):#initialize depth to 0
        if not node: return depth #if a node itself is none, don't add 1 to depth
        depth+=1 #one more valid level on the right
        if node.right == None:
            return depth
        return self.checkRight(node.right,depth)


