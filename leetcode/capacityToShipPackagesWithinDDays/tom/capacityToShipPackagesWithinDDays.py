class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        weightsLen = len(weights)
        min_Max = max(weights)
        tmpMax = max(weights)
        memo = {}
        if D == 1 :
            return sum(weights)
        elif D == weightsLen:
            return tmpMax
        
        def DP(begin_pt,rest_D,cur_capacity) :
            key = str(begin_pt) + ',' + str(rest_D) + ',' + str(cur_capacity)
            
            if rest_D == 1 :
                tmpLoad = sum(weights[begin_pt:])
                if tmpLoad > cur_capacity :
                    memo[key] = tmpLoad
                    return tmpLoad
                else :
                    memo[key] = cur_capacity
                    return cur_capacity
            if key in memo :
                return memo[key]
            if begin_pt == weightsLen :
                memo[key] = cur_capacity
                return cur_capacity
            else :
                tmpArr = []
                for pt in range(begin_pt,weightsLen) :
                    tmp_load = sum(weights[begin_pt:pt+1])
                    if tmp_load > cur_capacity :
                        tmpArr.append(DP(pt+1,rest_D-1,tmp_load))
                    else :
                        tmpArr.append(DP(pt+1,rest_D-1,cur_capacity))
                tmp_ans = min(tmpArr)
                memo[key] = tmp_ans
                return tmp_ans
        return(DP(0,D,max(weights)))



if __name__ == '__main__' :
    weights = [3,2,2,4,1,4]
    D = 3

    sol = Solution()


    print(sol.shipWithinDays(weights,D))
