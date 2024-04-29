# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs

# Solution by: Javi Barranco

# Problem:
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example:
# Input: cost = [10, 15, 20]
# Output: 15

class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        dp = [None] * (len(cost) + 1)
        cost = [0] + cost

        def backtrack(i: int):
            if i >= len(cost):
                return 0
            
            if dp[i] == None:
                dp[i] = cost[i] + min(backtrack(i+1), backtrack(i+2))
            
            return dp[i]

        backtrack(0)
        return dp[0]
    

exercise = Solution()

input = [10, 15, 20]

expected_output = 15

output = exercise.minCostClimbingStairs(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")