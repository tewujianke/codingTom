"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
"""

"""
A more efficent way - using stack.

GO through the nubmers. 
If seeing + or -, we can't calculate them directly, so push onto the stack
If seeing * or /, we calculate the number with the top number of stack, then push onto the stack
Then go through all items, do the sum.

A tip:
If seeing a minus (-), we just push the negative numbers onto the stack. Then we could just do sum at the end.

"""

import math
class Solution(object):
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        import re
        stack = []

        no_space = ''.join(filter(lambda x:x!=' ',s))  #use filter to get rid of all spaces
        input_array = []
        tmp = []
        for i in no_space:     #parse the input string, put every number and operand into a list
            if i=='+' or i=='-' or i=='*' or i=='/':  #if seeing operand, push just operand and digits so far (for multi-digits)
                if len(tmp):
                    input_array.append(''.join(tmp))
                    tmp = []
                input_array.append(i)
            else:
                tmp.append(i)

        if len(tmp): input_array.append(''.join(tmp))

        multiply =0  #these are toggles
        divide = 0
        minus = 0
        plus = 1

        for i in input_array:
            if minus:    #if a minus sign, for the next number, flip the sign and push on to the stack
                minus = 0
                stack.append(-int(i))
            if multiply: #if a multiply sign, calculate the multiplication with top of stack and next number. no need to push
                multiply = 0
                stack[-1] = stack[-1] * int(i)  #edit the top of stack directly
            if divide:   #if a divide sign, calculate the the quotient with top of stack and next number. no need to push
                divide = 0
                tmp = stack[-1] / int(i)
                if tmp>0: tmp = math.floor(tmp)
                else: tmp = math.ceil(tmp)  #negative number using // will round down. We need to round up in this case
                stack[-1] = int(tmp)  #edit the top of stack directly
            if plus: #if plus, just append the number
                plus = 0
                stack.append(int(i))
            if i == '*':    #seeing oprands. turn on corresponding toggles
                multiply = 1
            if i == '/':
                divide = 1
            if i == '-':
                minus = 1
            if i == '+':
                plus = 1

        return sum(stack) #return the sum
        

        
        
if __name__ == '__main__':
    a = "14-3/2"
    sol = Solution()
    print("final=",sol.calculate(a))
