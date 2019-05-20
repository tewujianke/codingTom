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

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        totalLen = len(s)
        if totalLen == 0 :
            return ""
        memo = [["" for n in range(totalLen)] for n in range(totalLen)]          ### nxn matrix 
        def solve(i,j) :                        ### i is start_index,   j is end_index
            if memo[i][j] != "" :                  
                return memo[i][j]
            if j - i == 1 :
                if s[i] == s[j] :              
                    memo[i][j] = s[i:j+1]
                    return s[i:j+1]
                else :
                    memo[i][j] = s[i]
                    return s[i]
            elif j - i == 0 :
                memo[i][j] = s[i]
                return s[i]
            stringLen = j-i+1                 
            tmpAns1, tmpAns2, tmpAns3 = "" , "" , ""
            
            if stringLen - len(solve(i+1,j-1)) == 2 and s[i] == s[j]:    ### this situation means we keep finding palindromic substring 
                tmpAns1 =  s[i:j+1]
                memo[i][j] = tmpAns1
                return tmpAns1                                           ### just return it
            else :
                tmpAns1 = solve(i+1,j-1)        ### the maximun substring we found based on three situation
            tmpAns2 = solve(i+1,j)
            tmpAns3 = solve(i,j-1)
            
            if len(tmpAns1) >= len(tmpAns2) and len(tmpAns1) >= len(tmpAns3) :   ### we compare their length and return the longest one
                memo[i][j] = tmpAns1
                return tmpAns1
            elif len(tmpAns2) >= len(tmpAns1) and len(tmpAns2) >= len(tmpAns3) :
                memo[i][j] = tmpAns2 
                return tmpAns2
            else :
                memo[i][j] = tmpAns3
                return tmpAns3
        return (solve(0,totalLen-1))



if __name__ == "__main__" : 
    sol = Solution()
    stringA = "lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc"
    print (sol.longestPalindrome(stringA))


