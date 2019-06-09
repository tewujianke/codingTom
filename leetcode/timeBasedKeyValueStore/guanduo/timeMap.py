"""
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
 

Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
 

"""
"""
Use a dictionary for lookup. Datastructure is dict[key] = list((value,timestamp))
Whenever set is called, just push value and timestamp to the list based on key. 

When get is called, perform a binary search based on the timestamp. return the index that either is the exact match or the first element that is smaller  than the timestamp. If the given timestamp is smaller than the first event, return an empty string.
"""
from collections import defaultdict

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.mem = defaultdict(list)                   #mem[key] = list(tuple(str,int))

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.mem[key].append((value,timestamp))       #implicit tuple in the ()
        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        def binary_search(arr,target):                #could have used bisect.bisect. But try to implement the key algorithm for binary search
            low,high = 0,len(arr)-1               
            while low<=high:
                mid = (low+high)//2
                if arr[mid][1] == target: return mid  #note that the array is a list of tuple(value, timestamp). So arr[mid][1] is the timestamp
                if arr[mid][1] < target: low = mid+1
                if arr[mid][1] > target: high = mid-1
            return low-1                              #if never found, return the smaller one. or -1 for non-matching case
            
        if not key in self.mem: return ''             #what the heck are you searching for?
        search = binary_search(self.mem[key],timestamp) 
        if search < 0 : return ''                     #the first timestamp is later than the specified one
        return self.mem[key][search][0]               #return the value
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
