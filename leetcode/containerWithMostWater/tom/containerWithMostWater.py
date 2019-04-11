"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""


"""
The basic idea is we find largest one and second large one, and we calculate its area and use two pointers,p1 and p2 to mark. Then, we find the third large one.
If its location is between largest one and second large one, we can ignore it and keep finding fourth large one.
If the location of fourth large one is not between first large one and second large one.

we can just calculate its area and move the nearest mark to its location. 


repeat above procedure and find out the maximum area


"""






class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sorted_height = sorted(height,reverse=True)   ### Sort array in descending order
        memo = {}        
        for i , n in enumerate(height) :
            if n in memo :
                memo[n].append(i)
            else :
                memo[n] = [i]           ###   use hash table to memory index location  

        pt1 = -1          #### pt1 is first pointer     pt2 is second pointer
        pt2 = -1
        tmp_pt = -1       #### tmp_pt is third point which need to be checked if it is larger than pt2 or smaller than pt1
        tmp_ans = 0
        for i, n in enumerate(sorted_height) :
            if pt1 == -1 :
                pt1 = memo[n].pop(0)
                continue
            elif pt2 == -1 :
                pt2 = memo[n].pop(0)
            
            if pt1 > pt2 : 
                tmp = pt1
                pt1 = pt2
                pt2 = tmp
            if i >=2 :
                tmp_pt = memo[n].pop(0)
                if tmp_pt > pt2 :
                    pt2 = tmp_pt
                elif tmp_pt < pt1 :
                    pt1 = tmp_pt               
            tmp_ans = max(tmp_ans,min(height[pt1], height[pt2]) * (pt2-pt1))
        return (tmp_ans)
