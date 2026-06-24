class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total=0
        res=0
        if sum(gas)<sum(cost):
            return -1
        for i in range(0,len(gas)):
            total=total+(gas[i]-cost[i])
            if total<0:
                total=0
                res=i+1
        return res
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
result=Solution().canCompleteCircuit(gas, cost)
print(result)