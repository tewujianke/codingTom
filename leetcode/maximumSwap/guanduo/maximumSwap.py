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
"""

"""
Idea: There is no need to swap if the array is already reversely sorted.
Therefore, use a temp array to store the reverse sorted array. Then iterate through both arrays.
If a mismatch between the two arrays is found, it means current index needs to be swapped with the value of the temp array.
Iterate the array from the end, find the same value shown up in the temp array, swap them. (since we want minimum impact on lower index, always pick from the end)
"""
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        will_swap = 0
        arr = [int(i) for i  in str(num)]#break the int into array of digits
        back_sorted = sorted(arr,reverse=True)#reversed sort the array
        for i,v in enumerate(arr):#iterate through the two arrays simutaneously 
            if v == back_sorted[i]: continue#if current digit matches the reversely sorted element, no need to sway
            will_swap = 1#otherwise, will need to swap
            break
        if not will_wap: return num #return directly if no swap needed
        for j in range(len(arr)-1,-1,-1): #if swap needed, look for the big guy from the end
            if back_sorted[i] == arr[j]:
                arr[i],arr[j]=arr[j],arr[i] #swap them and be done
                break
        return int(''.join([str(s) for s in arr]))#combine the array into int again

if __name__ == '__main__':
    sol = Solution()
    a = 10909091
    
    print(sol.maximumSwap(a))
                
