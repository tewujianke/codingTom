"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: 9973
Output: 9973
Explanation: No swap.
Note:

The given number is in the range [0, 108]


"""
"""

If the number is decreasing sorted, it is already the maximum value.
if we find it is not decresing sorted, we can start to find largest val from the end of that list to the position,
which cause the list not to be a decresing sorted list. and store it to tmpMaxVal

After that, we still need to find the first value which is smaller than the tmpMaxVal value from the begining of the list. 

we just swap them. the value will become maximum value.






"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        list_num = list(str(num))
        tmpMaxInd = 0
        tmpMaxVal = -1
        for i in range(len(list_num)) :
            if i == 0 :
                continue
            else :
                if list_num[i] <= list_num[i-1] :   ### check if the list is decreasing sorted
                    continue                         
                else :                              ### not decressing sorted
                    for j in range(i,len(list_num)) :  ### from the checkpoint to the end 
                        if list_num[j] >= tmpMaxVal :   
                            tmpMaxInd = j               
                            tmpMaxVal = list_num[j]
                        else :
                            continue
                    for j in range(0,i) :           ### from begining point to the checkpoint 
                        if tmpMaxVal > list_num[j] :
                            list_num[tmpMaxInd], list_num[j] = list_num[j], list_num[tmpMaxInd]    ### this is powerful swap way 
                            break                                                                  ### guanduo is best 
                    break
        return( int("".join(list_num)))
