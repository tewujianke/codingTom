"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

"""
The idea is to use backtracking. Since the length of the string is fixed to 2xN, we keep appending '('
until N, then backtrack, append ')' when valid (number of ')' smaller than number of '('.
Push a result once reaching 2xN length of the string
"""
import pprint

class Solution:
    def generateParenthesis(self, n):

        result = [] #return this 
        left = 0 #count number of left parenthesess
        right = 0#count number of right parenthesess
        self.helper(n,result,left,right,'') #backtracking start
        return result

    def helper(self,n,result,left,right,cur):

        if len(cur) == 2*n: #if reaching target length, append current string
            result.append(cur)
            return #nothing else to be done. return

        if left < n: #if I still can add left parenthesess, add it

            self.helper(n,result,left+1,right,cur+'(')
        if right < left: #after left parenthesess done, add right

            self.helper(n,result,left,right+1,cur+')')
        return




if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)

    n = 4

    sol = Solution()
    result = sol.generateParenthesis(n)

    pp.pprint(result)
