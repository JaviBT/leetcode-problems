# 2812. Find the Safest Path in a Grid
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

# Solution by: Javi Barranco

# Problem:
#You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

# - A cell containing a thief if grid[r][c] = 1
# - An empty cell if grid[r][c] = 0

#You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

#The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

#Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

#An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

#The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

# Example 1:
# Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# Output: 2

from typing import List
from collections import deque
import math
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        visit = set()
        thieves = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: 
                    thieves.append((i, j))
                    visit.add((i, j))
                    grid[i][j] = 0

        cnt = 1
        while thieves:
            qLen = len(thieves)

            for _ in range(len(thieves)):
                i, j = thieves.popleft()

                for i_delta, j_delta in directions:
                    ni, nj = i + i_delta, j + j_delta
                    if ni < 0 or nj < 0 or ni >= rows or nj >= cols or (ni, nj) in visit: continue
                    thieves.append((ni, nj))
                    visit.add((ni, nj))
                    grid[ni][nj] = cnt

            cnt += 1

        visit = set([(0,0)])
        minHeap = []
        heapq.heappush(minHeap, (-grid[0][0], (0,0)))
        safeness_factor = math.inf

        while minHeap:
            safeness, (i, j) = heapq.heappop(minHeap)
            safeness_factor = min(safeness_factor, -safeness)
            

            if (i, j) == (rows - 1, cols - 1):
                return safeness_factor

            for i_delta, j_delta in directions:
                ni, nj = i + i_delta, j + j_delta
                if ni < 0 or nj < 0 or ni >= rows or nj >= cols or (ni, nj) in visit: continue
                heapq.heappush(minHeap, (-grid[ni][nj], (ni, nj)))
                visit.add((ni, nj))


class Solution3:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        thieves = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: thieves.append((i, j))

        def minManhattan(i: int, j: int):
            res = math.inf
            for ti, tj in thieves:
                res = min(res, abs(i - ti) + abs(j - tj))
            return res

        visit = set()
        minHeap = []
        heapq.heappush(minHeap, (-minManhattan(0, 0), (0,0)))
        safeness_factor = math.inf

        while minHeap:
            safeness, (i, j) = heapq.heappop(minHeap)
            safeness_factor = min(safeness_factor, -safeness)
            visit.add((i, j))

            if (i, j) == (rows - 1, cols - 1):
                return safeness_factor

            for i_delta, j_delta in directions:
                ni, nj = i + i_delta, j + j_delta
                if ni < 0 or nj < 0 or ni >= rows or nj >= cols or (ni, nj) in visit: continue
                heapq.heappush(minHeap, (-minManhattan(ni, nj), (ni, nj)))


exercise = Solution()

input = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]

expected_output = 2

output = exercise.maximumSafenessFactor(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")