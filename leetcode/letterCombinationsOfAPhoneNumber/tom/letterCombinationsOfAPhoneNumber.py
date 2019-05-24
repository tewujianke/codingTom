"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

"""


"""

basic idea :
    we build the string by going through the input integer string
    and then store them to next memo. 
    After, we take next integet string and change to all its possible character and append to the current all possible combination.


"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = { 2:['a','b','c'], 3:['d','e','f'],4:['g','h','i'], 5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        memo = {}
        if len(digits) == 0 :
            return ""
        for i in range(len(digits)) :
            tmp = ""
            if i == 0 :
                memo[i] = table[int(digits[i])]
            else :

                memo[i] = []
                if i >= 2 :
                    memo[i] = []
                for string_set in memo[i-1] :
                    for char in table[int(digits[i])] :
                        memo[i].append(string_set+char)
        return (memo[len(digits)-1])
