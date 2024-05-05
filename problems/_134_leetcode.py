# 134. Gas Station
# https://leetcode.com/problems/gas-station/

# Solution by: Javi Barranco

# Problem:
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
# You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if (sum(gas) < sum(cost)): return -1

        diff = [gas[i] - cost[i] for i in range(len(gas))]
        total = 0
        cur_idx = 0
        for idx, num in enumerate(diff):
            if total == 0 and total + num > 0: cur_idx = idx
            total = total + num if total + num > 0 else 0

        return cur_idx


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if (sum(gas) < sum(cost)): return -1

        # Visit the most promosing indexes first
        index_order = [(i,gas[i]) for i in range(len(gas))]
        index_order.sort(key=lambda x:x[1], reverse=True)
        index_order = [index_order[i][0] for i in range(len(index_order))]

        for i in index_order:
            tank = gas[i]
            j = i % n
            while True:
                if tank < cost[j % n]:
                    break
                tank = tank - cost[j % n] + gas[(j + 1) % n]
                j = (j + 1) % n

                if j == i: return i
        
        return -1
    

exercise = Solution()
input = [1,2,3,4,5]
cost = [3,4,5,1,2]
expected_output = 3
output = exercise.canCompleteCircuit(input, cost)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
