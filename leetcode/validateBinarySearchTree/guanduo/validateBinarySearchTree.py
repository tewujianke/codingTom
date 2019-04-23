"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
}
Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
BST: All nodes in the left sub tree are smaller than the current node.
     All nodes in the right sub tree are bigger than the current node.

Therefore, in-order traversal would always give increasing order.
Step1: in-order traverse the tree.
step2: go through the list and if the increasing order is not met, return false
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inOrderTraversal(all_nodes,node):
            if not node: return
            if node.left: inOrderTraversal(all_nodes,node.left)
            all_nodes.append(node)
            if node.right: inOrderTraversal(all_nodes,node.right)

        if not root: return True #empty tree
        all_nodes = [] #list to store all the nodes in order
        inOrderTraversal(all_nodes,root) #recursively traverse the tree in-order
        #for i in all_nodes:
            #print(i.val)
        for i,v in enumerate(all_nodes): #go through the list, find any non-increasing neighbors
            if i == 0: continue
            if v.val <= all_nodes[i-1].val: return False 
        return True
