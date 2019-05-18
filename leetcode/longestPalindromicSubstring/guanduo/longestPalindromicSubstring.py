"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""

"""
Use dynamic Programming to solve.
Dynamic Analysis is the following:

Assume function P(i,j) means s[i:j] (j included) is palindromic. Then we can get the following formula:
1.   P(0,0), P(1,1), P(2,2) ... P(j,j) are all True since single character string is always palindromic.
2.   P(0,1) = (s[0] == s[1]),  P(1,2) =  (s[1] == s[2]), ...,  P(j-1,j) = (s[j-1] == s[j])
3.   P(0,2) = (s[0] == s[2]) && P(1,1),  P(1,3) = (s[1]==s[3]) && P(2,2) , ... 
4.   P(0,3) = (s[0] == s[3]) && P(1,2), ...
5.   P(0,j) = (s[0] == s[j]) && P(1,j-1)

This gives the following way to calculate if an index range gives a palindromic string:
1. The leftmost and rightmost characters must be the same.
2. The inner part must be palindromic (which we can use DP to avoid repeated calculation)
"""

class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not len(s): return ''    #empty string
        mem = dict()                #use dict to record the previously covered result
        final_i = -1                #store the final longest palidromic string index
        final_j = -1                #store the final longest palidromic string index 

        #helper function to know previously covered palindromic string index
        def isPalindromic(i,j):
            if i>=j: return True #special case when i and j are adjacent like i=1,j=2. We don't need to tell, just return True
            if str(i)+"+"+str(j) in mem: return True
            return False
        #if we've found a new longer palindromic string, record the index
        def setPalindromic(i,j):
            mem[str(i)+'+'+str(j)] = 1

        #this diff means - we cover smaller length first, then bigger substring
        #first  iteration we cover  [0,1],[1,2],[2,3],...[j-1,j]
        #second iteration we cover  [0,2],[1,3],[2,4],...[j-2,j]
        #third  iteration we cover  [0,3],[1,4],[2,5],...[j-3,j]
        #final  iteration we cover  [0,j]
        for diff in range(1,len(s)):
            i=0
            j=i+diff #make the spread
            while j<len(s): #exit condition is the right index  
                if s[i]==s[j] and isPalindromic(i+1,j-1):  #if the outer two char are the same, AND the inner string is palindromic
                    final_i=i              #record both indices
                    final_j=j
                    setPalindromic(i,j)    #record the answer for this substring
                i+=1
                j+=1
        return s[final_i:final_j+1] if final_i!=-1 else s[0]  #return the longest substring if there is one. otherwise, return first char

