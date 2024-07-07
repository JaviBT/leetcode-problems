# 62. Unique Paths
# https://leetcode.com/problems/unique-paths

# Solution by: Javi Barranco

# Problem:
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid.
# How many possible unique paths are there?

# Example:
# Input: m = 3, n = 7
# Output: 28

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1: return 1

        prev = [0] * n
        prev[0] = 1
        cur = [1] * n

        for _ in range(m - 1):
            for i in range(1, n):
                prev[i] = prev[i - 1] + cur[i]
            cur = prev
            prev = [0] * n
            prev[0] = 1

        return cur[n - 1]
    

exercise = Solution()

input = 3, 7

expected_output = 28

output = exercise.uniquePaths(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")