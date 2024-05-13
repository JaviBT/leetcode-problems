# 1293. Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

# Solution by: Javi Barranco

# Problem:
# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

# Example 1:
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6

from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        visit = set()
        q = deque([(0, 0, k, 0)])

        while q:
            i, j, cur_k, dist = q.popleft()

            if (i, j) == (n - 1, m - 1): 
                return dist

            for i_delta, j_delta in directions:
                ni, nj = i + i_delta, j + j_delta
                if ni < 0 or nj < 0 or ni >= n or nj >= m: continue

                new_k = cur_k - grid[ni][nj]
                if new_k >= 0 and (ni, nj, new_k) not in visit:
                    visit.add((ni, nj, new_k))
                    q.append((ni, nj, new_k, dist + 1))

        return -1
    

exercise = Solution()

input = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1

expected_output = 6

output = exercise.shortestPath(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")