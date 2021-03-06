"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:

The tree will have between 1 and 100 nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
"""
Using TWO methods to solve.
1. 
Use BFS. Push all nodes to a queue, including all NULL ptr children
Once we see a None, then the following object in the queue must not be a valid node. 
Otherwise, it is not a complete tree.

2.
Use DFS. Get max valid depth by peaking into left-end.
When we have reached the first None at depth, raise a flag. With a raised flag, if a valid node appears at same
level (depth), return False.
Corner cases to deal with: all previous levels must be full. If there is a deeper right branch(level > depth), return false
"""
from collections import deque
class Solution(object):
    def isCompleteTreeBFS(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        que = deque()           #use deque as queue for BFS
        que.append(root)        #push the root. ready for BFS
        NO_MORE_NODE = False    #a flag used to determine if the following valid nodes are legal or not
        
        while len(que):
            cur = que.popleft()
            if not cur:         #if seeing the first NULL ptr, set the flag to true and forbid any following valid node
                NO_MORE_NODE = True
                continue
            if NO_MORE_NODE and cur: return False  #see a valid node after a null ptr. return false
            que.append(cur.left )
            que.append(cur.right)
            
        return True

    """
    Use DFS to solve.
    """
    def isCompleteTreeDFS(self, root):
        if not root: return True
        depth = 0

        node = root            #calculate the max depth on the left
        while node:
            depth+=1
            node = node.left
            
        def DFS(node,level=0,flag=False):
            """
            return (flag,isComplete)
            """
            if not flag and not node and level==depth: return(True,True)  #first None at depth. Raise flag
            if not node: return (flag,True)                               #regular NULL ptr, jsut return a complete result
            if level <=depth-2:                                           #all previous levels must be full
                if not node.left or not node.right: return (flag,False)   #means both children present at depth-2 and above
            if level > depth: return(flag,False)                          #a deeper right branch
            if flag and level==depth and node: return(flag,False)         #invalid node as flag has been raised
            if not node.left and node.right: return(flag,False)           #go left first
            flag,isComplete = DFS(node.left,level+1,flag)
            if not isComplete: return (flag,False)
            flag,isComplete = DFS(node.right,level+1,flag)                #then go right
            return (flag,isComplete)
        flag,isComplete = DFS(root,1)
        return isComplete
