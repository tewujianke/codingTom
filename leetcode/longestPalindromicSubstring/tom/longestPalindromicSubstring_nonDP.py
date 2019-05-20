import pysnooper

class Solution(object):
    @pysnooper.snoop()
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def find(front,end) :                          ### find the longest substring based on the front and end points
            if front == 0 or end == totalLen -1 :      ### we already arrive the first or final element.
                return s[front:end+1]
            while True :
                front -= 1
                end += 1
                if s[front] == s[end] :
                    if front == 0 or end == totalLen - 1 :
                        return s[front:end+1]
                    else :
                        continue
                else :
                    return s[front+1 : end]
        totalLen = len(s)
        if totalLen == 0  :     ### we skip the first and last element, so we need to take care of it if the string length is less than 3
            return ""
        if totalLen == 1 :
            return s[0]
        if totalLen == 2 :
            if s[0] == s[1] :
                return s[:]
            else :
                return s[0]
        ans = ""
        tmpAns = ""
        for i in range(totalLen) :
            if len(tmpAns) >= len(ans) :
                ans = tmpAns
            tmpAns = ""
            front = i
            end = i

            if i > 0 and i < (totalLen - 1) :    ### skip the fist element and last element
                if s[i] != s[i+1] and s[i-1] == s[i+1] :    ### like case "aca" , we start at "c" and start to find the maximum substring
                    front = i
                    end = i
                elif s[i] != s[i+1] and s[i] != s[i-1] and s[i-1] != s[i+1] : ### like "abc", there is no palindromic substring, just skip to next element
                    continue
                elif s[i] == s[i+1] and s[i-1] != s[i+1] :    ### like "acc", in this case we start with "cc" and keep finding 
                    front = i
                    end = i+1
                elif s[i] == s[i+1] and s[i-1] == s[i+1] :  ###  like "acccc",  special case.  there are two cases like "cc" or "ccc" 
                    ### two case to consider
                    tmp = find(i,i+1)
                    tmp2 = find(i,i)
                    if len(tmp) >= len(tmp2) :
                        tmpAns = tmp
                    else :
                        tmpAns = tmp2
                    continue
                elif s[i] == s[i-1] and s[i-1] != s[i+1]  :  #basically, we cover all cases except the "ccba", because we skip the fist element. 
                    front = i-1
                    end = i
                if front == 0 or end == totalLen -1 :       # if the front is 0 idex or end is final element.
                    tmpAns = s[front:end+1]                 # we dont need to keep finding, just return it
                    continue
                tmpAns = find(front,end)                    
        if len(ans) != 0 :     ### if we dont find any answer, it means every char appear once, so we just pick anyone we want.
            return (ans)
        else :
            return s[0]

sol =  Solution() 
stringA = "ccd"
sol.longestPalindrome(stringA)

