def shipWithinDays(self, weights, D):
    """
    :type weights: List[int]
    :type D: int
    :rtype: int
    """
    maxWeight = sum(weights)
    minWeight = max(weights)
    
    
    def binarySearch(lo,hi) :   ### using binary search to find the min weight.
        if lo > hi :
            return lo
        mid = (lo + hi) // 2
        if canLoad(mid,D) :
            return binarySearch(lo,mid-1)
        else :
            return binarySearch(mid+1,hi)
        
    def canLoad(weight,days) :    ###  check if we can ship all item within the D days
        i = 0
        
        while days > 0 and i < len(weights):
            tmpWeight = weight
            while tmpWeight >= weights[i] :
                tmpWeight = tmpWeight - weights[i] 
                i = i + 1
                if i == len(weights) :
                    break
            days = days -1
        if i == len(weights) :
            return True
        else :
            return False
    return (binarySearch(minWeight,maxWeight))
        
