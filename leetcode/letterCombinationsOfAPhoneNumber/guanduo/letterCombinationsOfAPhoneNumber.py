"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

"""
Use itertools to get the cartesian product

"""
from itertools import product
class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0: return []           #empty list
        lookup = {'1':'','2':'abc','3':'def',    #my lookup table (dict)
                  '4':'ghi','5':'jkl','6':'mno',
                  '7':'pqrs','8':'tuv','9':'wxyz'}
        list_char = [lookup[x] for x in digits]      #from the input digits, lookup all chars mapped
        result_in_tuple = product(*list_char)                 #return a list of tuple with catesian product
        result = [''.join(x) for x in result_in_tuple]        #combine the tuple into strings
        return result
