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
"""
class Solution(object):
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
