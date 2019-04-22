"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]



"""

"""
basic idea : 

The zigzag level order is 
first level from left to right
second level from right to left,
third level from left to right, etc.

we can use Broad first search to traverse the tree, and print each level from different direction.

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tmp = [root,'|']     ### we use '|' as marker to indicate this level ends
        ans = []
        tmpVal = []
        leftToRight = 1             ### First level is from left to right
        while tmp :     
            node = tmp.pop(0)
            if node == None :
                continue
            elif node == '|' :      ### if we encounter '|', we start next level order traversal
                if len(tmp) != 0 :
                    tmp.append('|')
                else :
                    continue
                if leftToRight == 1 :
                    ans.append(tmpVal)
                    leftToRight = 0
                else :
                    ans.append(tmpVal[-1::-1])
                    leftToRight = 1
                tmpVal = []
            else :
                tmpVal.append(node.val)
                tmp.append(node.left)
                tmp.append(node.right)
        return (ans)

