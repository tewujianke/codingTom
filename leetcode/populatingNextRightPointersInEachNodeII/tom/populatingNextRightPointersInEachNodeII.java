/*

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.



*/



/*

basic idea : we just use BFS but we don't use any extra space 


*/


/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val,Node _left,Node _right,Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return root;
        }
        Node cur = root;
        Node nextNode = cur.next;        
        Node nextChild = null;    
        Node firstChild = null;     // this variable is to store the first child node which we encounter when we process the same level node.
        while (cur != null) {     // use while loop to run the BFS 
            if(cur == nextNode) {      
                nextNode = cur.next;
            }
            while (nextNode != null) {      // if nextNode doesn't have any child, we move it to nextNode until we find any child
                if(nextNode.left!=null) {
                    nextChild = nextNode.left;
                    break;
                } else if (nextNode.right != null) {
                    nextChild = nextNode.right;
                    break;
                } else {
                    nextNode = nextNode.next;
                }
            }
            if (cur.left == null && cur.right == null) {     // there are four cases which we will have for current node
                cur = cur.next;                              // current node doesn't have any child, so we move to next node.
                continue;
            } else if (cur.left != null && cur.right != null) {
                firstChild = (firstChild == null) ? cur.left : firstChild;  // current node has both children.
                cur.left.next = cur.right;
                cur.right.next = (nextNode == null) ? null : nextChild;
            } else if (cur.left != null && cur.right == null) {
                firstChild = (firstChild == null) ? cur.left : firstChild;
                cur.left.next = (nextNode == null) ? null : nextChild;
            } else if (cur.left == null && cur.right != null) {
                firstChild = (firstChild == null) ? cur.right : firstChild;
                cur.right.next = (nextNode == null) ? null : nextChild;
            }
            cur = cur.next;
            nextNode = (nextNode == null) ? null: nextNode.next;    
        }
        connect(firstChild);
        return root;    
    }
}

