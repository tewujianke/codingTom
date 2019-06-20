/*
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );
*/


/*
Use a hashmap to support key->node O(1) lookup.
Use a double linked list to support LRU check.

 */
#include <unordered_map>
#include <list>
#include <pair>
using namespace std;

class LRUCache {
private:

  int capacity;                                 //max number of element in the cache
  int count;                                    //current number of elements stored
  list<pair<int,int>> LRU;                      //used to track LRU info (head is the oldest)
  unordered_map<int,list<pair<int,int>>::iterator> lookup;
public:
  LRUCache(int capacity) {
    this->capacity = capacity;
    count = 0;
  }
    
  int get(int key) {
    if(lookup.count(key)) {                              //if exist, then we move the node the the tail (most recent)
      list<pair<int,int>>::iterator it = lookup[key];    //get the iterator
      LRU.splice(LRU.end(),LRU,it);                      //move to tail
      return it->second;                                 //return value
    } 
    return -1;                                           //not found
  }
    
  void put(int key, int value) {
    if(lookup.count(key)) {                              //overwrite existing key, and move the node to the tail (most recent)
      auto it = lookup[key];           
      it->second = value;
      LRU.splice(LRU.end(),LRU,it);                      //move to tail
    } else {                                             //else: new key. Construct the pair, push to the tail.
      pair<int,int> newPair = {key,value};
      LRU.push_back(newPair);
      auto last_element = LRU.end();                     //get the last valid node (most recent), and record in the hash map
      --last_element;
      lookup[key] = last_element;
      ++count;                                           //increment counter

      if(count > capacity) {                             //if the previous put exceeds the cache list, get rid of the head of the double linked list
	lookup.erase(LRU.front().first);
	LRU.pop_front();
	--count;
      }
    }
  }
};
