/*
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

*/


/*

// Definition for a Node.
class Node {
public:
  int val;
  Node* next;
  Node* random;

  Node() {}

  Node(int _val, Node* _next, Node* _random) {
    val = _val;
    next = _next;
    random = _random;
  }
};
*/


//Use recursion to solve the problem
//If there is next, keep copying nodes till end. Then if there is random, keep copying nodes till end

class Solution {
private:
  unordered_map<Node*,Node*> mappingT;              //make it a private member to keep code clean.key is original list, item is the new list node
public:
  Node* copyRandomList(Node* head) {
    if(head == NULL) return NULL;                   //empty list or we have reached end
    if(mappingT.count(head)) return mappingT[head]; //if current node has been constructed before (either through random or next, no need to copy again
    Node* newNode = new Node(head->val);            //got a new node. construct it 
    mappingT[head] = newNode;                       //record the node to the map.
    newNode->next = copyRandomList(head->next);     //recursively copy next nodes
    newNode->random = copyRandomList(head->random); //recursively copy random nodes
    return newNode;
  }

};
