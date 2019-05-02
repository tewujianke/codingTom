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

"""
Using DFS to serialize and de-serialize. 
"""
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
                result.append('None')#convert to string for None
                return
            result.append(str(node.val)) #convert to string for valid node. Only push the value to it
            serializeDFS(node.left,result) #this is post order. in order would also work
            serializeDFS(node.right,result)
            
        serializedArray = list()
        serializeDFS(root,serializedArray)
        return ','.join(serializedArray)#join the array into a string "1,2,3,None,None,5,6"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def buildTreeDFS(nodeArray):
            if not len(nodeArray): return None #empty list. no more node
            newNode = nodeArray.pop() #pop from back (since reserved already)
            if newNode=='None': return None #got a none. return none
            newNode = TreeNode(int(newNode)) #construct a new node with value
            newNode.left = buildTreeDFS(nodeArray)  #DPS
            newNode.right= buildTreeDFS(nodeArray)
            return newNode #don't forget to return the node in the end
            
        nodeArray = data.split(',') #split the string into list of nodes and Nones
        nodeArray.reverse() #reverse the string since popping from front is time consuming. Could have used a deque or queue in this case
        if not len(nodeArray) or not nodeArray[-1]: return None

        return buildTreeDFS(nodeArray) #recursively build the tree
        

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
    print(codec.serialize(codec.deserialize(codec.serialize(root))))
