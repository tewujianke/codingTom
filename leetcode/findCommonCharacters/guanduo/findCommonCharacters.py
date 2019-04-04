"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

"""
The idea is to get character count for each string. Compare among all the string for each character, return the 
minimum, which is the number of repetition for that char
"""

from collections import Counter

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        list_of_counter = [Counter(x) for x in A] #this is a list of counters for each string in the array
        result = []#initialize result array
        for i in range(26): #go through each character in the world
            current_char = chr(ord('a') + i) #get from a->b->c->...->z
            result += [current_char]*min([cnt[current_char] for cnt in list_of_counter]) #append result if the minimum is not 0
        return result

if __name__ == "__main__":

    sol=Solution()
    A = ["cool","lock","cook"]

    print(sol.commonChars(A))

        

        
