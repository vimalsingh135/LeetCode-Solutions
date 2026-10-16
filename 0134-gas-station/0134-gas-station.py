class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0 
        tank=0
        total_cost=sum(cost)
        total_gas=sum(gas)
        if total_gas<total_cost:
            return -1
        for i in range(len(gas)):
            tank+= gas[i] - cost[i]
            if tank<0:
                start=i+1
                tank=0
        return start
