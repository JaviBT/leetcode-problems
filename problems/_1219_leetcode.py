# Path with Maximum Gold
# https://leetcode.com/problems/path-with-maximum-gold/

# Solution by: Javi Barranco

# Problem:
# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
# Return the maximum amount of gold you can collect under the conditions:
# - Every time you are located in a cell you will collect all the gold in that cell.
# - From your position, you can walk one step to the left, right, up, or down.
# - You can't visit the same cell more than once.
# - Never visit a cell with 0 gold.
# - You can start and stop collecting gold from any position in the grid that has some gold.

from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(row: int, col: int):
            if (row, col) in visit: return 0
            
            visit.add((row,col))

            res = grid[row][col]
            grid[row][col] = 0

            max_path = 0
            for row_delta, col_delta in directions:
                n_row, n_col = row + row_delta, col + col_delta
                if 0 <= n_row < rows and 0 <= n_col < cols and grid[n_row][n_col] != 0:
                    max_path = max(max_path, dfs(n_row, n_col))
                    visit.remove((n_row, n_col))

            grid[row][col] = res

            return res + max_path
            
        max_gold = 0
        for row in range(rows):
            for col in range(cols):
                visit = set([])
                if grid[row][col] != 0: 
                    max_gold = max(max_gold, dfs(row, col))

        return max_gold
    

exercise = Solution()

input = [[0,6,0],[5,8,7],[0,9,0]]

expected_output = 24

output = exercise.getMaximumGold(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")