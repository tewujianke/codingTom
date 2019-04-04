"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        A = [list(str(string)) for string in A]                 ### first, we transfer string to list, so that we can take advantage of built-in function of list
        tmp_ans = []
        run_time = len(A[0])       ### if first string have 5 chars, we only need to run the iteration 5 times  
        string_len = len(A)        ### we need to check every string in the list A, so we need to calculate how many strings 
        for n in range(run_time) :
            seek_char = ''
            foundIndex = -1      
            for i in range(string_len) :
                if i == 0 :
                    seek_char = A[i].pop(0)       ### first string, we just pop the first char and start to check if the char is in the other strings
                else :
                    try :
                        foundIndex = A[i].index(seek_char)
                        A[i].pop(foundIndex)   ### if we found the char in other string, we just remove the char from the string so that we can avoid to find the same char
                    except:
                        foundIndex = -1   ### if not found, we can directly break, and go to second char in the first string
                        break
                if i == len(A) - 1:      ### after we check all strings, we can said this char is in all strings.
                    tmp_ans.append(seek_char)
        return (tmp_ans)
