# 134. Gas Station

class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
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
