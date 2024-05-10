# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

# Solution by: Javi Barranco

# Problem:
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid.
# How many possible unique paths are there?

# Example 1:
# Input: m = 3, n = 7
# Output: 28

import math

class Solution: # Using combinatorial formula
    def uniquePaths(self, m: int, n: int) -> int:
        manhattan = abs(m - 1 - 0) + abs(n - 1 - 0)

        res = math.factorial(manhattan) / ( math.factorial(m - 1) * math.factorial(manhattan - m + 1) )

        return int(res)
    

class Solution: # Using dynamic programming
    def uniquePaths(self, m: int, n: int) -> int:
        next_row = [1] * n

        for _ in range(m - 1):
            cur_row = [1] * n
            for i in range(len(cur_row) - 1):
                cur_row[-2 - i] = cur_row[-1 - i] + next_row[-2 - i]
            next_row = cur_row
        
        return next_row[0]
    

exercise = Solution()

input = [3, 7]

expected_output = 28

output = exercise.uniquePaths(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")