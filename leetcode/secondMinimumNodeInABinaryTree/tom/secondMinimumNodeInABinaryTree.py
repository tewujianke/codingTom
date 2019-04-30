"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
 

Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.




"""


"""

idea : we use recursive to find the second minimum value.

we just ignore the root value and start to find the second one.


"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node) :
            if not node.left and not node.right :   ### if the node dont have any child, it means there is no second min,so return -1 as described by question
                return -1
            else :
                if node.val < node.left.val or node.val < node.right.val : ## if we found any child which have larger value than its parent node
                    if node.val == node.left.val :  ### if left node is equal to the node value
                        a = helper(node.left)       ### we keep search the second minimum value
                        if a == -1 :                ### a == -1 means there is no second minimum in that subtree,so we return node.right.val
                            return node.right.val
                        else :                      ### else we return the smaller one
                            return min(a,node.right.val)
                    elif node.val == node.right.val :   ### same as above
                        a = helper(node.right) 
                        if a == -1 :
                            return node.left.val
                        else :
                            return min(node.left.val,a)
                    else :                              ### both children are larger than its parent's node, so we just return the smaller one              
                        return min(node.left.val,node.right.val)
                else :            ### both children are equal to its parent's node, so we keep running the recursive function. 
                    a = helper(node.left)    
                    b = helper(node.right)
                    if a != -1 and b != -1 :
                        return min(a,b)
                    if a == -1 :
                        return b 
                    elif b == -1 :
                        return a 
        return helper(root)
