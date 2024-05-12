# 329. Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# Solution by: Javi Barranco

# Problem:
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down.
# You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Example 1:
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = {}
        
        def dfs(i: int, j: int):
            if (i, j) in dp: return dp[(i, j)]

            res = 1
            res += max(
                    dfs(i + 1, j) if i + 1 < n and matrix[i][j] < matrix[i + 1][j] else 0,
                    dfs(i - 1, j) if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j] else 0,
                    dfs(i, j + 1) if j + 1 < m and matrix[i][j] < matrix[i][j + 1] else 0,
                    dfs(i, j - 1) if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1] else 0
                )

            dp[(i, j)] = res
            return res

        max_path = 0
        for i in range(n):
            for j in range(m):
                max_path = max(max_path, dfs(i, j))

        return max_path
    

exercise = Solution()

input = [[9,9,4],[6,6,8],[2,1,1]]

expected_output = 4

output = exercise.longestIncreasingPath(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")