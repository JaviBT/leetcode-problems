# 2373. Largest Local Values in a Matrix
# https://leetcode.com/problems/largest-local-values-in-a-matrix/

# Solution by: Javi Barranco

# Problem:
# You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
# Return the generated matrix.

# Example 1:
# Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Output: [[9,9],[8,6]]

from typing import List
import math

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        l, u = 0, 0
        r, d = 3, 3

        res = []

        while d <= n:
            new_row = []
            while r <= n:
                max_val = -math.inf
                for i in range(l, r):
                    for j in range(u, d):
                        max_val = max(max_val, grid[j][i])
                new_row.append(max_val)
                l, r = l + 1, r + 1
            l, r = 0, 3
            u, d = u + 1, d + 1
            res.append(new_row)

        return res
    

exercise = Solution()

input = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]

expected_output = [[9,9],[8,6]]

output = exercise.largestLocal(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")