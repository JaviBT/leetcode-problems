# 695. Max Area of Island
# https://leetcode.com/problems/max-area-of-island/

# Solution by: Javi Barranco

# Problem:
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#                [0,0,0,0,0,0,0,1,1,1,0,0,0],
#                [0,1,1,0,1,0,0,0,0,0,0,0,0],
#                [0,1,0,0,1,1,0,0,1,0,1,0,0],
#                [0,1,0,0,1,1,0,0,1,1,1,0,0],
#                [0,0,0,0,0,0,0,0,0,0,1,0,0],
#                [0,0,0,0,0,0,0,1,1,1,0,0,0],
#                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6

class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(i:int, j:int):
            if (i < 0 or j < 0 or
                i >= m or j >= n or
                (i, j) in visited or
                grid[i][j] == 0): return 0 

            visited.add((i, j))
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if (i, j) in visited: continue
                maxArea = max(maxArea, dfs(i, j))

        return maxArea
    

exercise = Solution()

input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

expected_output = 6

output = exercise.maxAreaOfIsland(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")