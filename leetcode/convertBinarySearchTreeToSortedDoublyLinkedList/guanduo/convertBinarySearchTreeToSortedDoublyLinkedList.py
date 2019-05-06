"""
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:

 


 
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

 


 
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

"""
Edit the stupid tree in place. Save first node when first reaching the left bottom.
Then for every node, save it to the last_node pointer. After in order traversal, special handling to the first and last node is needed

"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #using dictionary because during recursion, we need last_node and first node to be consistent.
        #if using two parameters instead, they will only be consistent for going down.
        info = {'last_node':None,'first_node':None}
        self.goFuckingTommy(root,info)#inorder traveral and edit tree in place
        if info['first_node']:#in case of empty tree
            info['first_node'].left = info['last_node'] #special handling for first and last node.
            info['last_node'].right = info['first_node']
        return info['first_node']

    def goFuckingTommy(self,cur_node,info):
        if not cur_node: return

        self.goFuckingTommy(cur_node.left,info) #go left first
        if(info['last_node']): #if there is last node already
            info['last_node'].right = cur_node
            cur_node.left = info['last_node']
            info['last_node'] = cur_node
        else: #smallest node in the tree. update both first and last
            info['first_node'] = cur_node
            info['last_node']  = cur_node
        self.goFuckingTommy(cur_node.right,info) #then go right
        
