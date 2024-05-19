# 3068. Find the Maximun Sum of Node Values
# https://leetcode.com/problems/find-the-maximun-sum-of-node-values/

# Solution by: Javi Barranco

# Problem:
# There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

# Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

# Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
# - nums[u] = nums[u] XOR k
# - nums[v] = nums[v] XOR k

# Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.

from typing import Optional, List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = [ (n ^ k) - n for n in nums]
        delta.sort(reverse = True)
        res = sum(nums)

        for i in range(0, len(delta), 2):
            if i + 1 < len(delta) and delta[i] + delta[i+1] > 0:
                res += (delta[i] + delta[i+1])

        return res
    

exercise = Solution()

input = [
    [1,2,1],
    3,
    [[0,1],[0,2]]
    ]

expected_output = 6

output = exercise.maximumValueSum(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")