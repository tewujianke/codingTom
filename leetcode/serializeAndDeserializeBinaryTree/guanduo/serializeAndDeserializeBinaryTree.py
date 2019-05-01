"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serializeDFS(node,result):
            if not node:
                result.append('None')
                return
            result.append(str(node.val))
            serializeDFS(node.left,result)
            serializeDFS(node.right,result)
            
        serializedArray = list()
        serializeDFS(root,serializedArray)
        return ','.join(serializedArray)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def buildTreeDFS(node,nodeArray):
            if not nodeArray.size(): return
            newNode = TreeNode(int(nodeArray.pop()))
            
        nodeArray = data.split(',')
        nodeArray.reverse()
        if not nodeArray.size() or not nodeArray[0]: return None
        root = None
        buildTreeDFS(root,nodeArray)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':

    root = TreeNode(1)
    n = TreeNode(2)
    root.left = n
    n = TreeNode(4)
    root.right = n
    n = TreeNode(3)
    root.left.left = n
    n = TreeNode(5)
    root.left.right = n
    n = TreeNode(6)
    root.left.right.left = n

    codec = Codec()
    print(codec.serialize(root))
