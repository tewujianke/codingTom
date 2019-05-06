/*
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:

 


 
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

 


 
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.


# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

*/

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/

/*
Use a deque to store inorder traversal result. Then iterate through the array and assign left and right accordingly
See python for a more optimized way (in place change without the aid of extra data struture
 */
#include <deque>
using namespace std;

class Solution {
public:
  Node* treeToDoublyList(Node* root) {
    if(root == NULL) return root; //empty
    deque<Node*> nodes;//create a deque to store in order traversal result
    inOrderTraversal(root,nodes); //call recursive function to traverse the tree
    if(nodes.size()!=1) { //if more than one nodes in the tree
      for(int i=0; i<nodes.size();i++) { //go through each node
	if (i==0) {//first node's left is pointing to the last node
	  nodes[i]->left = nodes[nodes.size()-1];
	  nodes[i]->right = nodes[i+1];
	} else if (i==nodes.size()-1) { //last node' right is pointing to the first node
	  nodes[i]->left = nodes[i-1];
	  nodes[i]->right = nodes[0]; 
	} else { //other nodes are next to each other
	  nodes[i]->left = nodes[i-1];
	  nodes[i]->right = nodes[i+1];
	}
      }
    } else {// sinlge node in the tree. Both left and right are pointing to itself
      nodes[0]->left = nodes[0];
      nodes[0]->right = nodes[0];
    }
    
    return nodes[0];//return the Tom
  }

  //in order traversal to grab all node pointers to the deque.
  void inOrderTraversal(Node* node, deque<Node*> & nodes) {
    if(node == NULL) return;
    inOrderTraversal(node->left,nodes);
    nodes.push_back(node);
    inOrderTraversal(node->right,nodes);
  }
};
