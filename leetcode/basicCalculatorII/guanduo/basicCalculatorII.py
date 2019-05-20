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
Use linked list to solve.  construct a linked list like 24->'+'->19->'-'->100->'*'->4->'/'
Two passes:
 1. first pass we ignore + and -. Iteratte through the LL, if the next pointer is "*" or "/", del the node, create a new node with result.
 2. second pass no need to edit the linked list because we are only left with "+","-". Just iterate from head to tail and calculate the sum.

 

"""
class Solution(object):
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        class Node:
            def __init__(self,val=None):
                self.val = val
                self.next = None

        head = Node()
        #takes the input string, remove any spaces, construct nodes based on numbers or operands.
        def process_input(s):
            cur = head
            content = []  #use a list for multi-digits numbers. Create a node we meeting a space or operand
            for each_char in s:
                if each_char == ' ' or each_char == '+' or each_char == '-' or each_char == '*' or each_char == '/':
                    if len(content):
                        newOp = ''.join(content)
                        content = []
                        cur.next = Node(newOp)
                        cur = cur.next
                    if not each_char == ' ':
                        cur.next = Node(each_char)
                        cur = cur.next
                else:
                    content.append(each_char)
                
            if len(content):
                cur.next = Node(''.join(content))


        process_input(s)
        cur = head.next
        prev = head
        while cur and cur.next: #first pass. Edit the linkekd list in place. If *or/, remove old node, create new node with new numbers
            if cur.next.val == '*':   #multiply
                result = int(cur.val)*int(cur.next.next.val)  #calculate the new number
                newNode = Node(str(result))   
                newNode.next = cur.next.next.next #remove whatever nodes in between the new node and next number
                prev.next = newNode
                cur = newNode

            elif cur.next.val == '/': #same for divide

                result = int(cur.val)//int(cur.next.next.val)
                newNode = Node(str(result))
                newNode.next = cur.next.next.next
                prev.next = newNode
                cur = newNode
            else: #ignore +/-
                prev = cur
                cur = cur.next
        cur = head.next
        prev = head
        result = None
        while cur.next:  #second pass just go from head to tail and accumulate the result
            if cur.next.val == '+':
                if result == None:
                    result = int(cur.val)+int(cur.next.next.val)
                else:
                    result += int(cur.next.next.val)
                cur = cur.next.next
            elif cur.next.val == '-':
                if result== None:
                    result = int(cur.val)- int(cur.next.next.val)
                else:
                    result -= int(cur.next.next.val)
                cur = cur.next.next
            else:
                cur = cur.next  #for the last number
        return result if result != None else int(head.next.val) #return the first number (single node) or the suum
            
            
            
if __name__ == '__main__':
    a = '2*3* 4'
    
    sol = Solution()

    print("final result=",sol.calculate(a))
