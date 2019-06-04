"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 """
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
Use recursive way to solve.
Traverse the entire tree. For each node, I assume the next connection has fully been established.

Need to traverse the right tree first, then left tree, as the tree may not be complete and a node's next pointer could skip 
some nodes on the same level. Traversing the right tree first ensures the complete next nodes connection on the previous level.

Then we check the node's children. If both children exist, I assign left child's next ptr to the right child
There is a case when there is only one child. In this case we need to find the rightmost node,
then I assign the rightmost node's next through its parent's "next"'s leftmost child.
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def help(node):
            if not node: return #empty tree or end
            if node.left==None and node.right==None: return   #no more to assign
            if node.left and node.right: node.left.next = node.right #both children exist. left.next -> right
            rightmost = node.right if node.right else node.left #find the rightmost node.
            if node.next:  #if the rightmost child's parent has a valid next, find the leftmost child
                cur = node.next
                while cur.next and (cur.left==None and cur.right==None):  #since tree may not be complete, there are cases where a child's next needs to bypass several nodes in the same level. Just keep going right as long as a parent has empty child
                    cur = cur.next
                rightmost.next = cur.left if cur.left else cur.right
            
            help(node.right) #MUST GO RIGHT FIRST! Since we need to make sure the parent's level's next assignment is done.
            help(node.left )
        help(root)
        return root
