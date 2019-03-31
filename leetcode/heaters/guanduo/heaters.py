"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
 

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
 

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
""" 

"""
Iterate through each house.
Use binary search to find the closest radius to current house.
return max radium among all hosues
"""
class Solution(object):
    def findRadius(self,houses,heaters):
        """
        :type hosues: list[int]
        :type heaters:list[int]
        :rtype: int
        """

        #return the minimum distance to a heater
        def binarySearch(arr,target):
            print('searching house ',target)
            if len(arr) == 1: return abs(target-arr[0]) #return the difference directly if only one heater
            lower_bound = 0
            upper_bound = len(arr)-1
            while 1: #binary search
                mid = (lower_bound+upper_bound)//2
                if target == arr[mid]: return 0#return radius of 0 if exact heat is on this house
                if target > arr[mid]: lower_bound = mid+1 
                else: upper_bound = mid
                if lower_bound == upper_bound: break

            if mid == len(arr)-1: return min(abs(target-arr[-1]),abs(target-arr[-2]))#house is to big. return difference
            elif mid == 0: return min(abs(target-arr[0]),abs(target-arr[1])) #hosue too small
            else: return min(abs(target-arr[mid]),abs(target-arr[mid-1]),abs(target-arr[mid+1])) #house in the middle
                                             
            print('found closest heater index ',mid, 'min radius=',res)
            return res


                                                                     
        houses.sort()#sorting array is needed for binary search
        heaters.sort() #same
        print(heaters)
        result = [binarySearch(heaters,x) for x in houses]#return the max radium found
        return max(result)

if __name__ == '__main__':


    a = [581030105,557810404,146319451,908194298,500782188,657821123]
    heat = [102246882,269406752,816731566,884936716,807130337,578354438]

    sol = Solution()
    print(sol.findRadius(a,heat))
        
