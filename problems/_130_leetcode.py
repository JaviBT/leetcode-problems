# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/

# Solution by: Javi Barranco

# Problem:
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

class Solution:
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        save = set()

        def dfs(i, j):
            if (i < 0 or j < 0 or i >= m or j >= n or board[i][j] == 'X' or (i, j) in save): return

            save.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for j in range(n): 
            dfs(0, j)
            dfs(m - 1, j)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in save: board[i][j] = "X"


exercise = Solution()

input = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

expected_output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

exercise.solve(input)
output = input
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")